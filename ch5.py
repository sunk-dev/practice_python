#01
def get_peri(r=5.0):
    return r*2*3.14

print(get_peri())
print(get_peri(4.0))

#02

#03
def cal(x,y):
    return x+y,x-y,x*y,x/y

n1=int(input('첫번째 정수 입력'))
n2=int(input('두번째 정수 입력'))
print(cal(n1,n2))