


"""
Utilities for creating and working with context managers.




Context manager is enabled by the "with" statement. The API has to have two methods:
"__enter()__" and "__exit__()". The "__enter__()" method is run when execution 
flow enters in "with" block. When execution flow leaves the "with" block 
"__exit__()" method is activated to clean up the resources.


Combaining context managers with "with" statement is more compact way to 
declare "try:finally" block, since context manager's "__exit__()" method 
will always run even when there is exception.

"""





# Context Managers as Function Decorators


import contextlib

class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print("__init__({})".format(how_used))
    
    def __enter__(self):
        print("__enter__({})".format(self.how_used))
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__({})".format(self.how_used))
    

@Context('as decorator')
def func(message):
    print(message)


print()
with Context('as context manager'):
    print("Doing work in the context")

print()
func("Doing work as decorator")




