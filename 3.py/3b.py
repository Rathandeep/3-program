Module A (sub_function_module.py): 
def sub_function(x, y): 
    return x + y 
Module B (code_module.py): 
from sub_function_module import sub_function 
result = sub_function(3, 5) 
print("Result obtained from sub-function:", result) 