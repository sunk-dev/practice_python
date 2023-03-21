# 50 평균 높이
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# total_height=sum(student_heights)
# numberofStudent=len(student_heights)
# average_height=total_height/numberofStudent
# print(average_height)
#Write your code below this row 👇

#51 높은 점수
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
# highest_score=0
# for i in student_scores:
#     if highest_score<i:
#         highest_score=i
# print('the highest scores in the class is',highest_score)
    

#53 짝수 더하기
#Write your code below this row 👇
#sol1
# for i in range(1,100+1):
#     if i%2==0:
#         sum+=i
# print(sum)
# #sol2
# sum=0
# for i in range(2,100+1,2): #이렇게 하면 애초에 짝수만 나옴
#     sum+=i
# print(sum)

#54 FizzBuzz
#sol1
# for i in range(1,100+1):
#     if i%3==0 and i%5!=0:
#         print('Fizz')
#     elif i%5==0 and i%3!=0:
#         print('Buzz')
#     elif i%3==0 and i%5==0:
#         print('FizzBuzz')
#     else:
#         print(i)
# #sol2 둘다 되는게 아니면 순서대로 내려오게 코딩 :좀더 깔끔!
# for i in range(1,100+1):
#     if  i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%5==0 :
#         print('Buzz')
#     elif i%3==0 :
#         print('Fizz')
#     else:
#         print(i)

# 5일차 최종프로젝트 비밀번호 생성기
#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pw=r.sample(letters,nr_letters)+r.sample(symbols,nr_symbols)+r.sample(numbers,nr_numbers)
# for i in pw:
#     print(i,end='')
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw=r.sample(letters,nr_letters)+r.sample(symbols,nr_symbols)+r.sample(numbers,nr_numbers)
r.shuffle(pw) #이렇게 하면 새로운 리스트 만들지 않고도 리스트를 섞을 수 있음!
#shake_pw=r.sample(pw,len(pw))
for i in pw:
    print(i,end='')
    
#강의에서 제시한 답
#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(r.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += r.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += r.choice(numbers)

print(password_list)
r.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
    