# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:46:17 2023

@author: jskre
"""

'''#4
h=int(input('시간을 입력하시오'))
m=int(input('분을 입력하시오'))
s=60*m+3600*h
print(f'{h}시간{m}분은{s}초입니다')

#6
m=int(input('음식비용'))
tip=input('팁비율')
tip_num=''
i=0
#람다식 배우면 쓸수 있을 듯. 
while(tip[i].isdigit()):#.isdigit():문자가 숫자로 이루어져있는지 아닌지 검사
#tip[i]가 숫자가 아닐때까지
        tip_num+=tip[i]#tip_num문자열에 tip[i]를 더함
        i+=1
        
tip_num=int(tip_num)#정수로 변환 

total=int(m*(1+(tip_num/100)))
print(f'총액{total}달러')

#9
#a1
num=input('정수네자리수를 입력하시오')
sum=0
for i in num:
    sum+=int(i)
print(sum)
#a2
num=int(input('정수네자리수를 입력하시오'))
sum=0
for i in range(4):
    sum+=num%10
    num=num//10
print(sum)
'''

#12
#a1
n=input('숫자를 입력하시오')
show_num=''
for i in range(len(n)):
    if((i+1)%3==0):
        if(i==len(n)-1):#만약 6자리 숫자인경우 마지막은 쉼표 안찍게 하기 위해서 
            show_num+=n[i]
        else:
            show_num+=n[i]
            show_num+=','
    else:
        show_num+=n[i]
print(show_num)
#a2 천재의 풀이....
a=int(input('숫자를 입력하시오'))
print(f'{a:,}')






    

    