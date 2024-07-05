print("########################################welcome in my calculator#####################################")
print("press 1 for addition ")
print("press 2 for substraction ")
print("press 3 for division ")
print("press 4 for multiplication ")
print("press 5 for trignometry ")
print("press 6 for logarithm ")
print("press 7 for square root ")
print("press 8 for square ")
print("press 9 for convert radian to degree ")
select=int(input("choose one option"))
if(select==1):
    a=int(input("enter your first number-->"))
    b=int(input("enter your second number-->"))
    print(a+b)
elif(select==2):
    a=int(input("enter your first number-->"))
    b=int(input("enter your second number-->"))
    print(a-b)
elif(select==3):
        a=int(input("enter your first number-->"))
        b=int(input("enter your second number-->"))
        print(a/b)  
elif(select==4):
        a=int(input("enter your first number-->"))
        b=int(input("enter your second number-->"))
        print(a*b)
elif(select==5):
    import math
    #press 1 for sin
    #press 2 for cos
    #press 3 for tan
    result=int(input("enter your choice-->"))
    angle=int(input("enter your angle-->"))
    if(result==1):
      print(math.sin(angle))
    elif(result==2):
      print(math.cos(angle))
    elif(result==3):
      print(math.tan(angle)) 
elif(select==6):
    import math
    number=int(input("enter your number"))
    print(math.log(number))
elif(select==6):
    import math
    number=int(input("enter your number"))
    print(math.log(number))  

elif(select==7):
    import math
    number=int(input("enter your number"))
    print(math.sqrt(number))
elif(select==8): 
    num2=int(input("enter your number")) 
    c=num2*num2
    print(c) 
elif(select==9):
    import math
    num3=int(input("enter your angle to convert radian into degree")) 
    print(math.degrees(num3))













