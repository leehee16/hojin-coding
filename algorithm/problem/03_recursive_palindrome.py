def is_palindrome(string:str)->bool:
    for i in range(len(string)//2-1):
        if string[0+i] != string[-1-i]:
            return False
    return True

def is_palindrome_recursive(string:str)->bool:
    if len(string) == 1:
        return True
    if string[0] == string[-1] :
        return is_palindrome_recursive(string[1:-1])
    else : return False
    

print(is_palindrome_recursive("우영우영우djd"))