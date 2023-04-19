# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:37:51 2023

@author: jskre
"""

'''ch1연습문제'''

import turtle

t=turtle.Turtle() #라이브러리의 Turtle()라이브러리의 함수를 실행하여 거북이 하나 생성
t.shape("turtle") #거북이의 모양 설정 화살표 등 4가지 모양지원
#기본적으로 오른쪽을 향해 있음
t.forward(100) #앞으로 100만큼 이동
t.left(90) #왼쪽으로 90도 회전
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90) #왼쪽으로 90도 회전
t.forward(100)


#turtle을 종료하는 문장
turtle.mainloop()
turtle.bye()
