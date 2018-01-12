#如何在运行时导入一个module

import importlib
module = 'hello'

# __import__ Found at: builtins
# __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module
#     
#     Import a module. Because this function is meant for use by the Python
#     interpreter and not for general use it is better to use
#      to programmatically import a module.
#     
#     The globals argument is only used to determine the context;
#     they are not modified.  The locals argument is unused.  The fromlist
#     should be a list of names to emuimportlib.import_module()late ``from name import ...'', or an
#     empty list to emulate ``import name''.
#     When importing a module from a package, note that __import__('A.B', ...)
#     returns package A when fromlist is empty, but its submodule B when
#     fromlist is not empty.  Level is used to determine whether to perform 
#     absolute or relative imports. 0 is absolute while a positive number
#     is the number of parent directories to search relative to the current module.

# mod = __import__(module)
mod = importlib.import_module(module)
#奇怪的是gunicorn直接用内建函数，而不是按照说明文档。

print(mod)

mod.hello()
