for i in range(2,101,2):
    print(i, end=" ")
year = 0
balance = 1000
 
while balance >= 2000 :
    year = year + 1
    interest = balance * 0.07
    balance = balance + interest
print(year, "년 걸립니다.")
n = 1234
sum = 0
while n > 0 :
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)
import random
 
a = random.randint(1,10)
b = random.randint(1,10)
com = a*b
 
while True:
    usr = int(input(str(a) + "*" + str(b) + "는 "))
    if (usr == com):
        print("맞았습니다.")
        break;
    sum = 0
while True:
    a = int(input("정수를 입력하시오: "))
    if (a == 0):
        print("합은 ", sum, "입니다.")
        break
 
    sum += a
import random

count = 0

while True:
    i = random.randint(1, 7)
    j = random.randint(1, 7)
    print("첫 번째 주사위 : ", i, "두 번째 주사위 : ", j)
    count += 1
    if(count == 5):
        break
