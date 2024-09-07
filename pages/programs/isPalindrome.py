i = int(input("Enter the number"))
x = i
rev = 0
while i > 0:
    rev = rev*10 + i%10
    i = i//10

if rev == x:
    print(f"{x} is a Palindrome number")
else:
    print(f"{x} is not a Palindrome number")
