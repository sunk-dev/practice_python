# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:10:53 2023

@author: jskre
"""
"""region=input('경기장은 어디 입니까?')
win_team=input('이긴 팀은 어디입니까')
lose_team=input('진 팀은 어디입니까')
mvp=input('우수 선수는 누구입니까')
score=input('스코어는 몇대몇입니까')
print(f'''
---------------------------------------------------
오늘{region}에서 야구 경기가 열렸습니다.
{win_team}과{lose_team} 은 치열한 공방전을 펼쳤습니다.
{mvp}가맹활약을 하였습니다.
결국 {win_team}가{lose_team} 를 {score}로 이겼습니다.
---------------------------------------------------''')

#sol1
x=int(input('첫번째 정수를입력'))
y=int(input('두번째 정수를입력'))
print(x+y)
#sol2
x=input('첫번째 정수를입력')
y=input('두번째 정수를입력')
x=int(x)
y=int(y)
"""
'''#sol3
x,y=map(int,input('첫번째 두번째 정수를입력').split())
print(x+y)'''

'''print('안녕하세요?')
name=input('이름이어떻게 되시나요?')
print(f'만나서 반갑습니다.{name}씨')
print('이름의 길이는 다음과 같군요',len(name))
age=int(input('나이가 어떻게 되시나요?'))
print(f'내년이면{age+1}살이 되시는군요')'''

'''물건금액=int(input('물건값을 입력하시오'))
print('입력금액')
천원=int(input('1000원 지폐개수'))
오백원=int(input('500원 지폐개수'))
백원=int(input('100원 지폐개수'))
총지불한돈=천원*1000+오백원*500+백원*100
거스름돈=총지불한돈-물건금액
반환오백원=거스름돈//500
거스름돈=거스름돈%500
반환백원=거스름돈//100
거스름돈=거스름돈%100
반환십원=거스름돈//10
print(f'500원{반환오백원} 100원{반환백원} 10원{반환십원}')
'''
#3 조건문

'''score=int(input('자신의 점수를 입력하시오'))
if score>=80:
    print('합격하였습니다')
else:
    print('불합격하였습니다.')'''


'''import random as r
n1=r.randint(1, 100)
n2=r.randint(1, 100)

a=int(input(f'{n1}+{n2}='))
if a==n1+n2:
    print('정답')
else:
    print('오답')'''

'''n1=int(input('정수를 입력하시오'))
print('3의배수'if n1%3==0 else '3의 배수아님')
if n1%3==0:
    print(f'{n1}은 3의 배수 입니다')
else:
    print(f'{n1}은 3의 배수가 아닙니다')'''

'''price=int(input('정가를 입력하시오'))
if price>=100:
    print('10층에서 사은품을 받아가시오')
    sale_price=price*0.85
    
else:
    sale_price=price*0.90

print('할인된 가격',sale_price) '''



'''age=int(input('나이입력'))
major=input('전공입력')

if age>=20 and (major=='컴퓨터공학과'or major=='컴공과'):
    print('장학금을 지급합니다')'''
    
'''import random as r
print('동전던지기 게임을 시작합니다')
coin=r.randint(0, 1)
#coin=r.rndrange(2) :정수중하나를 무작위하게 반환
if coin==1:
    print(coin,'앞면입니다')
else:
    print(coin,'뒷면입니다')'''

'''import turtle

t=turtle.Turtle()
t.shape("turtle")
t.color("blue")

while(True):
    d=input('방향을 입력하시오')
    if d=='l':
        #왼쪽
        t.left(90)
        t.fd(100)
    elif d=='r':
        t.right(90)
        t.fd(100)
    elif d=='q':
        break
turtle.bye()'''

'''n1=int(input('첫번째 수를 입력'))
n2=int(input('두번째 수를 입력'))
Operator=input('연산자 입력')
if Operator=='+':
    result=n1+n2
elif Operator=='-':
    result=n1-n2
elif Operator=='*':
    result=n1*n2
elif Operator=='/':
    result=n1/n2
    
print(f'{n1}{Operator}{n2}={result}')'''

import random as r
n1=r.randint(1, 100)
n2=r.randint(1, 100) 
Operators=['+','-','*','/']
random_operator=r.choice(Operators)
if random_operator=='+':
    result=n1+n2
elif random_operator=='-':
    result=n1-n2
elif random_operator=='*':
    result=n1*n2
elif random_operator=='/':
    result=n1/n2
answer=float(input(f'{n1}{random_operator}{n2}=?'))
if result==answer:
    print('정답입니다')
else:
    print('오답입니다')
    print(f'{n1}{random_operator}{n2}={result}')

































    