
'''
#원의 면적 구하기
radius=float(input('원의 반지름을 입력하시오'))
p=3.14
area=(radius**2)*p
print(f'반지름이 {radius}인 원의 면적은 {area}')'''


#삼각형 면적 구하기
'''base=10
height=10
area=base*height/2
print(area)'''

'''
p199 10
def sum_double():
    n=int(input('n의 값을 입력하십시오'))
    sum=0
    for i in range(n+1):
        sum+=i**2
    return sum
    
print(sum_double())
'''

'''import turtle
t=turtle.Turtle()
t.shape("turtle")
radius=100
t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
turtle.mainloop()
turtle.bye()'''

'''x=3
y=5
x,y=y,x
print(x,y)'''

'''#원기둥의 부피 구하기
r=5 #반지름
h=10 #높이
p=3.14 #파이
v=p*r*r*h #부피
print(v)

#입력버전
r,h=map(float,input('반지름과 높이를 각각입력하시오').split())
p=3.14 #파이
v=p*r*r*h #부피
print(v)'''
print('''import math as m
a=1.75
print(m.ceil(a))
print(m.floor(a))
print(round(a,1)) #round는 math모듈에 들어가지 않음
''')

#문자열을 쌍따옴표로 통일


