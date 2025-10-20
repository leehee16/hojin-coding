# Q. 60에서 0까지 숫자를 출력하시오.
def print_number(number):
    if number == -1:
        return 0
    print(number)
    return print_number(number-1)

print_number(60)