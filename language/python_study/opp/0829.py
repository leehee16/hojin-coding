class Book :
    def __init__(self,title:str, author:str) :
        self.title = title
        self.author = author
        self.is_checked_out : bool = False #여기는 타입명시 안해줘도 되나?

    def check_out(self) -> None:
        if self.is_checked_out :
            raise ValueError("이미 대출중입니다!")
        self.is_checked_out = True #메세지를 추가해도 되나?

    def return_book(self) -> None:
        if not self.is_checked_out :
            raise RuntimeError("대출된 책이 아닙니다!")
        self.is_checked_out = False
    
class Library :
    def __init__(self) -> None:
        self.books: list[Book] = []
    
from typing import Any
class Stack :
    #스토리지
    def __init__(self) -> None:
        self.items = []
    #푸시
    def push(self,k) -> None:
        self.items.append(k) #k라고 쓰면되나? 변수 정하는게 제일 힘들다.
    #팝
    def pop(self) -> Any:
        return self.items.pop()
    #peek
    def peek(self) -> Any:
        return self.items[-1]
    #is_empty
    def is_empty(self) -> bool:
        return True if not self.items else False
    #__len__()
    # 이런 언더바는 뭔지 모르겠다. 무슨 숨기는 함수였던거같은데
    def __len__(self) -> int:
        return len(self.items)