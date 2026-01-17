# Answers To Questions

## Chapter 2

- What is the Python INterpreter ?
The python interpreter is a software program that runs python codes.
It is made of many components that help to compile the source code to byte code and then interpret the code to machine code
during execution.

- What is source Code ?
Source code is the code that is written by the programmer of engineer. It consists of texts in text files and normaly the files end in .py extension.

- What is byte code ?
Byte code is the code that is compiled by the interpreter and it is platform independent. It is also the portable form of python code.
It is later translated into machine code by the PVM.

The byte code are automatically stored in a .pyc file if your interpreter has the persion to write on the disk.

- What is the PVM ?
It stands for Python Virtaul Machine and it is a machine that interpretes python bytecode to machine langauge of the mahcine where it is being runned.
It is the runtime engine for ptyon that interpretes you compiled bytes codes.

- Name two Python's standard execution model.
    - CPython (standard or mostly used)
    - Jython

### Correction

CPython and Jython are alternaltive compilers for python and not execution models.
The execution models include Psyco, Shedskin and frozen binaries.


- How are Cpython, Jython and IronPython different ?
CPython is the defactor mode for the python interpreter that translates Source code to byte code and byte code to Machine Code by the PVM.

Jython on the other hand is similar to CPython but is more for java devs. It provides a way to script java codes. It uses the JVM in the place of PVM in the CPython setup.

IronPython is particular for C# and .NET applications. 