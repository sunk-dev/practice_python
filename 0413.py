# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:09:32 2023

@author: jskre
"""
#구분자가 없을경우
'''numbers=input('사용자숫자를 입력하시오')

for i in numbers:
    i=int(i)
    print('*'*i)
    

   
#구분자가 있을경우  
#numbers_1=list(map(int,input('사용자 숫자를 입력하시오').split(' ')))
#for j in numbers_1:
    #print('*'*j)
def get_area(radius):
    area=3.14*(radius**2)
    return area



def main():
    print('20cm 2개 피자의 면적',get_area(20)*2)
    print('30cm 피자 1개의 영역',get_area(30))
main()

def get_sum(start,end):
    sum=0
    if(start<end):
        for i in range(start,end+1):
            sum+=i
    else:
        for i in range(end,start+1):
            sum+=i
        
    return sum

x=int(input('시작숫자'))
y=int(input('끝숫자'))
value=get_sum(x,y)
print(value)

def sub(x,y,z):
    print(f'x={x} y={y} z={z}')


def add(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    return sum
print(add(10,20))
print(add(10,20,30,40,50))

alist=[1,2,3]
print(*alist)

adict={'1':'one','2':'two','3':'three'}



def display_1(count,msg='반갑습니다'):
    for i in range(count):
        print(msg)

display_1(5)

def display(msg,count=1):
    for i in range(count):
        print(msg)

display('환영합니다',5)'''

def calculator(x,y,z):
    result=0
    operator=''
    if z==1:
        result=x+y
        operator='+'
        
    elif z==2:
        result=x-y
        operator='-'
        
    elif z==3:
        result=x*y
        operator='x'
    elif z==4:
        result=x/y
        operator='÷'
    else:
        print('제시한 항목번호를 숫자를 적어주세요')
        
        
    return result,operator
z=int(input('어떤 연산을 수행할지 숫자를 적으시오 1.덧셈,2.뺄셈,3.곱셈,4.나눗셈'))
x=int(input('첫번째 수를 입력하시오'))
y=int(input('두번째 수를 입력하시오'))


result,operator=calculator(x, y, z)

print(f'{x}{operator}{y}={result}')















