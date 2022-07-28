### TASK
'''
WAF to replace all the multiple spaces into single space
'''
def mul_spaces(my_string):
    result = " ".join(my_string.split())
    return(result)
    
if __name__ == "__main__":
    my_string = "this    is     a    string     with    multiple    spaces"
    print(mul_spaces)