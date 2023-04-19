# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:15:04 2023
@author: jskre
"""
'''target=2000
money=1000
year=0
rate=0.07

while money<target:
    money=money*1.07
    year+=1
print(f'{year}년 후 {money:.2f}')'''


'''total=0
hol=1


while (total<100):
    total+=hol
    print('total',total)
    hol+=2
    print('hol',hol)

    
print(total,hol)

i=0
while i<3:
    print("루프안쪽")
    i+=1
else:
    print("else 부분")
    
j=0

while j<3:
    print("무한루프")'''


'''dan=int(input('몇단을 출력하시겠습니까?'))
i=1
while(i<=9):
    print(f'{dan}*{i}={dan*i}')
    i+=1
    
import random as r
while True:
    x=r.randint(1, 100)
    y=r.randint(1, 100)
    answer=int(input(f'{x}+{y}=?'))
    if answer==(x+y):
        print('정답입니다')
    else:
        print('오답입니다.')
        
        
        


answer=r.randint(1, 100)
try_num=0
while True:
    try_num+=1
    if try_num>3:
        print('3번이 넘었습니다 실패하셨습니다')
        break
    n=int(input('1부터 100까지의 정수를 입력하세요!'))
    if n==answer:
        print(f'정답입니다 시도횟수{try_num}')
    elif n>answer:
        print('너무 높음')
    else:
        print('너무 낮음')

for y in range(5):
    for x in range(10):
        print("*",end='')
    print('')


for y in range(1,6):
    for x in range(y):
        print("*",end='')
    print('')

n=int(input('별을 몇줄을 그릴건가요?'))
for i in range(n,0,-1):
    for y in range(i):
        print('*',end='')
    print('')

for i in range(n,0,-1):
    print('*'*i)
    
for i in range(n+1):
    print(' '*(n-i),'*'*(2*i-1))


for i in range(n+1):
    print(' '*(n-i),'*'*(2*i-1))  
for i in range(1,n):
    print(' '*i,'*'*(2*(n-i)-1))

#주사위합이 6이되는경우
for i in range(1,6):
    for j in range(1,6):
        if i+j==6:
            print(f'첫번째 주사위{i}두번째 주사위{j}')
    

person=['jennie','peter','lesia','jcob']
restaurants=['korean','american','french','chinese']
for i in person:
    for j in restaurants:
        print(f'{i}이(가) {j}식당을 방문')

  
while True:
    light=input('신호등색상을 입력하세요').upper()
    if light=='GREEN':
        break
print('전진')    
'''

for i in range(3,100):
    for j in range(2,i):
        if i%j==0:
            break
        elif j==i:
            print(i)
   
        























