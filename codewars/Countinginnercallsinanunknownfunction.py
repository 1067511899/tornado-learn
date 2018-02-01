'''
Description:
The aim of this kata is to determine the number of sub-function calls made by an unknown function.

You have to write a function named count_calls which:

takes as parameter a function and its arguments (args, kwargs)
calls the function
returns a tuple containing:

the number of function calls made inside it and inside all the sub-called functions recursively
the function return value.
NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.
完全不会。

'''
import sys

def count_calls(func, *args, **kwargs):
    """Count calls in function func"""

    calls = [ -1 ]
    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer
    sys.settrace(tracer)
  
    rv = func(*args, **kwargs)
  
    return calls[0], rv

'''
sys.settrace(tracefunc)
Set the system’s trace function, which allows you to implement a Python source code debugger in Python. The function is thread-specific; for a debugger to support multiple threads, it must be registered using settrace() for each thread being debugged.

Trace functions should have three arguments: frame, event, and arg. frame is the current stack frame. event is a string: 'call', 'line', 'return' or 'exception'. arg depends on the event type.

The trace function is invoked (with event set to 'call') whenever a new local scope is entered; it should return a reference to a local trace function to be used that scope, or None if the scope shouldn’t be traced.

The local trace function should return a reference to itself (or to another function for further tracing in that scope), or None to turn off tracing in that scope.

The events have the following meaning:

'call'
A function is called (or some other code block entered). The global trace function is called; arg is None; the return value specifies the local trace function.
'line'
The interpreter is about to execute a new line of code or re-execute the condition of a loop. The local trace function is called; arg is None; the return value specifies the new local trace function. See Objects/lnotab_notes.txt for a detailed explanation of how this works.
'return'
A function (or other code block) is about to return. The local trace function is called; arg is the value that will be returned, or None if the event is caused by an exception being raised. The trace function’s return value is ignored.
'exception'
An exception has occurred. The local trace function is called; arg is a tuple (exception, value, traceback); the return value specifies the new local trace function.
Note that as an exception is propagated down the chain of callers, an 'exception' event is generated at each level.

For more information on code and frame objects, refer to The standard type hierarchy.

CPython implementation detail: The settrace() function is intended only for implementing debuggers, profilers, coverage tools and the like. Its behavior is part of the implementation platform, rather than part of the language definition, and thus may not be available in all Python implementations.
'''
if __name__ == '__main__':
    pass