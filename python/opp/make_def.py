import time

def print_name(age=None, name:str='unknown'):
    if age is None:
        print('age is None')
    else:
        print('age: {}'.format(age))
        print('name:'+ name)
    
def is_even_number(num:int):
    if num%2 :
        print(f'{num}은 홀수입니다.')
    else :
        print(f'{num}은 짝수입니다.')

"""
args
"""
def first_names(*names):
    for name in names :
        print(name)




def logging_duration(fn):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fn(*args,**kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return 
    return wrapper

"""
kwargs
"""
@logging_duration
def name_values(**kwargs):
    for key, val in kwargs.items():
        print(key,val)

#---실행모듈---
name_values(name='호진', age=30)
