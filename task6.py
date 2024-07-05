def my_max(number):
    ""
    numbers = new_func(number)
    if not numbers:
        return None #return none for an empty list
    max_num=number[0]#assume the first number is the maximum
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num 

def new_func(number):
    finds the maximum number in a list.
    Args:
    numbers:A list of numbers.
    Returns:
    the maximum number in the list.
    ""
    return numbers
number=[5,12,3,8,1] 
print (my_max(numbers))      
