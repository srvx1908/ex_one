#def print_numbers(*args):
#    for number in args:
#        print(number)
#print_numbers(1,2,3) 


def print_info(**kwargs):
    for key, value in kwargs.items ():
        print(f"(key):(value)") 
print_info(name="alice",age=30)        