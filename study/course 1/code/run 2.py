from asyncore import loop
from cgitb import text


email = "Hi everyone There will be a cash investment in our school next week for dollars If you would like to participate in this investment, kindly bring some spare cash The amount will go towards building a new casino in our school Looking forward to your participation in this dollars SEE YOU ALL AT THE CASH INVESTMENT"
print(email.count('cash'))
print(email.count('dollars'))
print(email.count('casino'))
print(email.count('investment'))

circle = 12.566
square = 36

answer1 = circle > square
answer2 = circle < square
answer3 = circle == square

print(answer1)
print(answer2)
print(answer3)



a=5

if a==2:
    print('I am 2')
elif a==5:
    print('I am 5')
else:
    print('you dont know my age')

option = input('What was your score in the test?: ')
p = int(option)

if p >= 50:
    print('YOU PASS!')

else:
    print('YOU FAIL LOSER!')


t = "hello this is an example"
"this" in t




