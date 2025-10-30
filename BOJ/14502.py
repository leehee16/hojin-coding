# 연구소 / 백트래킹 + BFS
"""
BFS (Breadth-First Search, 너비 우선 탐색)은 
그래프나 2차원 배열(지도, 미로 등)을 탐색할 때 
가장 기본이 되는 알고리즘 중 하나

BFS는 가까운 노드부터 차례대로 탐색하는 알고리즘이다.
즉, “최단 거리”를 구할 때 가장 자주 쓰인다.

1. 시작 노드를 큐(Queue)에 넣는다.
2. 큐에서 하나 꺼내서(pop) 방문 처리한다.
3. 그 노드에 인접한 노드(아직 방문 안 한 노드) 를 큐에 넣는다.
4. 큐가 빌 때까지 2~3 반복.
"""
import sys
from io import StringIO

# 테스트 입력을 코드 안에 직접 작성
test_input = """\
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

# ↓ 아래 두 줄은 테스트 전용 (백준 제출 시 제거)
sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    print(graph, flush=True)

if __name__ == "__main__":
    solution()