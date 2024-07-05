def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str=str(input("enter your your string "))
print("the original string is:",str)
print("the reverse string is ",reverse_string(str))    