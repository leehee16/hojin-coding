class Calculator:
    def __init__(self) -> None:
        pass
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b == 0:
            raise ValueError
        return a/b
    
if __name__ == "__main__":
    cal = Calculator()
    mode = input("모드를 입력해주세요:")
    a,b = input("값을 두개 입력해주세요:").split(",")
    if mode == "더하기":
        print(f"{a}+{b}: {cal.add(int(a),int(b))}")
    elif mode == "빼기":
        print(f"{a}-{b}: {cal.sub(int(a),int(b))}")
    elif mode == "곱하기":
        print(f"{a}X{b}: {cal.mul(int(a),int(b))}")
    elif mode == "나누기":
        print(f"{a}%{b}: {cal.div(int(a),int(b))}")
    else:
        raise KeyError()