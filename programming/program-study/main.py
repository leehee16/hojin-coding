"""
객체지향 To-Do 리스트 애플리케이션
클래스를 사용하여 할 일을 관리하는 프로그램
"""
from datetime import datetime
from typing import List, Optional


class Todo:
    """개별 할 일을 나타내는 클래스"""
    
    def __init__(self, task: str):
        self.task = task
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def complete(self):
        """할 일을 완료 상태로 변경"""
        self.completed = True
        self.completed_at = datetime.now()
    
    def __str__(self):
        """할 일의 문자열 표현"""
        status = "✅" if self.completed else "⬜"
        return f"{status} {self.task}"


class TodoList:
    """할 일 목록을 관리하는 클래스"""
    
    def __init__(self):
        self.todos: List[Todo] = []
    
    def add_todo(self, task: str) -> bool:
        """새로운 할 일을 추가"""
        # TODO(human): task 문자열을 받아서 새로운 Todo 객체를 생성하고 
        # self.todos 리스트에 추가하는 로직을 구현하세요
        # 빈 문자열이나 공백만 있는 경우는 False를 반환하고,
        # 성공적으로 추가된 경우 True를 반환하세요
        pass
    
    def display_todos(self):
        """모든 할 일 목록을 표시"""
        if not self.todos:
            print("\n📭 할 일이 없습니다. 새로운 할 일을 추가해보세요!")
            return
        
        print("\n📋 현재 할 일 목록:")
        print("-"*40)
        for i, todo in enumerate(self.todos, 1):
            print(f"{i}. {todo}")
        print("-"*40)
    
    def complete_todo(self, index: int) -> bool:
        """특정 인덱스의 할 일을 완료 처리"""
        if 0 <= index < len(self.todos):
            self.todos[index].complete()
            return True
        return False
    
    def delete_todo(self, index: int) -> Optional[Todo]:
        """특정 인덱스의 할 일을 삭제"""
        if 0 <= index < len(self.todos):
            return self.todos.pop(index)
        return None
    
    def get_statistics(self):
        """통계 정보 반환"""
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo.completed)
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }


class TodoApp:
    """To-Do 리스트 애플리케이션의 메인 클래스"""
    
    def __init__(self):
        self.todo_list = TodoList()
    
    def display_menu(self):
        """메인 메뉴를 화면에 표시"""
        stats = self.todo_list.get_statistics()
        print("\n" + "="*40)
        print("       📝 To-Do 리스트 관리")
        print(f"  (전체: {stats['total']} | 완료: {stats['completed']} | 대기: {stats['pending']})")
        print("="*40)
        print("1. 할 일 추가")
        print("2. 할 일 목록 보기")
        print("3. 할 일 완료 체크")
        print("4. 할 일 삭제")
        print("5. 종료")
        print("-"*40)
    
    def handle_add_todo(self):
        """할 일 추가 처리"""
        task = input("\n새로운 할 일을 입력하세요: ")
        if self.todo_list.add_todo(task):
            print(f"✨ '{task}'가 추가되었습니다!")
        else:
            print("❌ 할 일을 입력해주세요.")
    
    def handle_complete_todo(self):
        """할 일 완료 처리"""
        if not self.todo_list.todos:
            print("\n할 일이 없습니다!")
            return
        
        self.todo_list.display_todos()
        try:
            index = int(input("\n완료할 할 일 번호를 입력하세요: ")) - 1
            if self.todo_list.complete_todo(index):
                print(f"✅ '{self.todo_list.todos[index].task}'를 완료했습니다!")
            else:
                print("❌ 잘못된 번호입니다.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
    
    def handle_delete_todo(self):
        """할 일 삭제 처리"""
        if not self.todo_list.todos:
            print("\n할 일이 없습니다!")
            return
        
        self.todo_list.display_todos()
        try:
            index = int(input("\n삭제할 할 일 번호를 입력하세요: ")) - 1
            deleted = self.todo_list.delete_todo(index)
            if deleted:
                print(f"🗑️  '{deleted.task}'를 삭제했습니다.")
            else:
                print("❌ 잘못된 번호입니다.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
    
    def run(self):
        """애플리케이션 실행"""
        print("\n🎉 To-Do 리스트 앱에 오신 것을 환영합니다!")
        
        while True:
            self.display_menu()
            choice = input("\n선택하세요 (1-5): ")
            
            if choice == "1":
                self.handle_add_todo()
            elif choice == "2":
                self.todo_list.display_todos()
            elif choice == "3":
                self.handle_complete_todo()
            elif choice == "4":
                self.handle_delete_todo()
            elif choice == "5":
                print("\n👋 프로그램을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("\n❌ 잘못된 선택입니다. 1-5 사이의 숫자를 입력하세요.")


def main():
    """메인 함수"""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()