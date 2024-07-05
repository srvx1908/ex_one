str1="anand dhaygude"
print(str1*8)
a=str1[-1]
print(a)
b=len(str1)
print(b)
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.find("dhaygude"))
print(str1.replace("anand","Harsh"))
str2="  hello,world"
#stripping whitespaces

print(str2.strip())
print(str2.lstrip())
print(str2.rstrip())
print(str2.lstrip())
#spitting and joining
print(str2.split())
#formatting 
#using % operator
name ="niranjan"
age=25
message="My name is %s and I am %d years old"
print(message)
#usinf str formating
print(f"my age is {age} and my name is {name}")



string="hello123"
print(string.isalnum())
print(string.isalpha())
print(string.isdigit())


#basic sliccing
str4="hello,world"
#extract hello
slice =str4[0:5]
print(slice)

#extract world
slice =str4[6:12]
print(slice)

#extract hello world
slice =str4[:]
print(slice)


