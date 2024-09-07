check = 0
num = int(input("Enter the number"))
x = num
while num>0:
    flag = num%10
    check += flag*flag*flag
    num = num//10

if check == x:
    print(f"{x} is an armstrong number")