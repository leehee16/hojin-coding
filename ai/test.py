import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model="openai/gpt-4o",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("openrouter_key"),
)

def classifier(state: MessagesState):
    """질문 유형을 분류"""
    messages = state["messages"] + [
        SystemMessage(content="이 질문이 시간에 관한 것이면 'times', 그 외는 'general'이라고 답변해주세요.")
    ]
    response = llm.invoke(messages)
    return {"messages": [response]}

def time_bot(state: MessagesState):
    """시간 전문 봇"""
    # 현재 시간 정보
    now = datetime.now()
    current_time = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    weekday = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"][now.weekday()]
    
    messages = state["messages"][:-1] + [  # classifier 응답 제외
        SystemMessage(content=f"""당신은 시간 알리미입니다. 친절하게 답변하세요.

        현재 시간 정보:
        - 날짜/시간: {current_time}
        - 요일: {weekday}

        이 정보를 바탕으로 사용자에게 답변하세요.""")
    ]
    return {"messages": [llm.invoke(messages)]}

def general_bot(state: MessagesState):
    """일반 질문 봇"""
    messages = state["messages"][:-1]  # classifier 응답 제외
    return {"messages": [llm.invoke(messages)]}

def route_question(state: MessagesState):
    """분기 결정 함수"""
    last_message = state["messages"][-1].content.lower()
    if "times" in last_message:
        return "time_bot"
    else:
        return "general_bot"

# 그래프 구성
graph = StateGraph(MessagesState)
graph.add_node("classifier", classifier)
graph.add_node("time_bot", time_bot)
graph.add_node("general_bot", general_bot)

graph.add_edge(START, "classifier")
graph.add_conditional_edges(
    "classifier",
    route_question,  # 조건에 따라 다음 노드 결정
    {
        "time_bot": "time_bot",
        "general_bot": "general_bot"
    }
)
graph.add_edge("time_bot", END)
graph.add_edge("general_bot", END)

graph = graph.compile()

# 실행
content = input("질문 입력: ")
result = graph.invoke({
    "messages": [HumanMessage(content=content)]
})

# 결과 출력
print("\n=== 최종 응답 ===")
print(result["messages"][-1].content)