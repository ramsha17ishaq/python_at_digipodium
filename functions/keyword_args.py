# we have another way in python that will
# allow us to pass named args to a function 
# **kwargs
# kwargs is the name of the parameter and
# ** before it means that it can accept
# any number of named values in the function

def student_report(**kwargs):
    total = 0
    for k,v in kwargs.items():
        print(k,v)
        total += v
    return len(kwargs), total/len(kwargs) 

# example call:
print(student_report(rohan = 50, rani = 30, alka = 50))
print(student_report(rohan = 50, rani = 30, anup = 20, vijay = 20, abhay = 40))