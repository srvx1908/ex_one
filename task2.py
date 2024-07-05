n= int(input("enter upto which-->"))  # Number of terms
num1, num2 = 0, 1
count = 0

while count < n:
    print(num1, end=" ")
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count += 1