---
id: python-crash-course
title: Python Crash Course
---

## Chapter 1 Notes - Getting Started

## Chapter 2 Notes - Variables and Simple Data Types

### Strings

f-strings - the f is for format, because Python formats the string by replacing the name of any variable in braces with its value.  
Example: `print(f"This is a string with a variable called {variable} in it!")`  
It is possible to format variables with functions within strings with f-strings  

- lower()
  - {variable.lower()}
- upper()
  - {variable.upper()}
- title()
  - {variable.title()}

## Chapter 3 Notes - Introducing Lists

A list is a collection of items in a particular order.  

In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:

The simplest way to add a new element to a list is to append the item to the list.

You can add a new element at any position in your list by using the insert() method.

If you know the position of the item you want to remove from a list, you can use the del statement.

The pop() method removes the last item in a list, but it lets you work with that item after removing it.  

when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

If you only know the value of the item you want to remove, you can use the remove() method.

- the remove method only removes the first instance of the value you specify. If a value appears more than once in a list, you would need to use a loop to remove all instances.  

List Sorting Methods:  
sort() - permanently sorts a list  
sorted() - displays a list as if it were sorted, but does not alter the list  

## Chapter 4 Notes - Working with Lists

When you want to do the same action with every item in a list, you can use Python's for loop.  

Python's use of indentation makes code very easy to read.  

The range() function makes it easy to generate a series of numbers.  

**slice** - a specific group of items in a list

**tuples** - allow for creation of lists with items that cannot change  
Python refers to values that cannot change as immutable, and an immutable list is called a tuple.  
To define a tuple, create a list using parenthesis rather than square brackets.  
You can access individual elements using the index, just as you would a list.  

Tuples are defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma.  

### Styling Your Code

Ideas about how to style your code are worthwhile to know. Take the time to make your code as easy as possible to read. Writing easy-to-read code helps you keep track of what your programs are doing and helps others understand your code as well.

[PEP 8](https://www.python.org/dev/peps/pep-0008/) (Python Enhancement Proposal) - instructs programmers on how to style their code.  

#### High Level Styling

Indentation - Use four spaces per indentation level.  
Line Length - Keep lines to less than 80 characters. Keep comments to less than 72 characters per line.  
Blank Lines - to group parts of your program visually, use blank lines.  

## Chapter 5 Notes - If Statements

The technique of using a series of simple if statements with no elif or else blocks makes sense when more than one condition could be True and you want to take action on every condition that is True.

## Chapter 6 Notes - Dictionaries

Dictionaries allow you to connect pieces of related information.  
A dictionary in python is a collection of key value pairs.  
To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line.  

```python
dictionary_name = {}  
dictionary_name['color'] = 'green'  
dictionary_name['number'] = 5  

print(dictionary_name)  
{'color': 'green', 'number': 5}
```

To update an item in a dictionary, assign a new value to the key in the dictionary.  
`dictionary_name['color'] = 'yellow'`  

To delete a piece of information stored in a dictionary, use the del statement to completely remove a key-value pair.  
`del dictionary_name['points']`  

The get() method can be used to get a value in dictionary as well as handle instances when a key doesn't exist.  
`dictionary_name.get('size', 'size is not assigned')`  

If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value.  

the items() method will display all key value pairs in a dictionary.  
the keys() method will display all the key values in a dictionary.  
the values() method will display all the values in a dictionary without the keys.  
the sorted() method will display all keys in a dictionary in alphabetical order.  
the set() method will display all values in a dictionary without the keys and remove duplicates.  

You can build a set directly using braces and separating the elements with commas. It is easy to mistake sets for dictionaries as they both are defined with curly braces and separated with commas. You know it's a set if there are no key value pairs visible.  

**nesting** - store multiple dictionaries in a list, or a list of items as a value in a dictionary.  
You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.  

You should not nest lists and dictionaries too deeply. If you’re nesting items deeply or you’re working with someone else’s code with significant levels of nesting, most likely there is a simpler way to solve the problem.  

## Chapter 7 - User Input and While Loops

input()
The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.  
The input() function interprets everything as a string.  

int()  
use the int() function to convert string numbers to integers.  

**modulo** - (%) divides one number by another number and returns the remainder.  

**while loops** - the for loop takes a collection of items and runs code once for each item in the collection. The while loop runs as long as (or while) a specified condition is true.  

**flag** - a variable that acts as a signal to the program.  
**break** - a keyword used to immediately exit out of a loop.  

The break statement can be used in any of Python's loops.  

**continue** - a statement used to return to the beginning of the loop based on the result of a conditional test.  
Avoid infinite loops. Every while loop needs a way to stop running so it won’t continue to run forever.  
To avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to.  

You shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop.  

## Chapter 8 - Functions

**modules** - files separate from the main program that often contain functions that can be used in your main program.  
**function definition** - tells Python the name of the function and any information required to perform its duty.  
**docstring** - a description of what the function does encased in triple quotes.  
**parameter** - a piece of information a function needs to perform its duty.  
**argument** - a piece of information that’s passed from a function call to a function.  

Note: People sometimes speak of arguments and parameters interchangeably. Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.  

**positional arguments** - arguments that need to be in the same order as the function parameters.  
**keyword arguments** - a name-value pair that you pass to a function. Each argument consists of a variable name and a value; and lists and dictionaries of values.  
Note: When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.  

**return value** - the value returned from a function.  

It is possible to have optional arguments.  

A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.  

You can send a copy of a list to a function with slice notation `function_name(list_name[:])`  

A function can accept several kinds of arguments(positional and arbitrary). The parameter that accepts an arbitrary number of arguments must be placed last in the function definition.  

A double asterisks before a parameter (**parameter_name) will create an empty dictionary called parameter_name and pack whatever key-value pairs it receives into the dictionary.

The best practice for importing functions is to import the function or functions you want or to import the entire module and use dot notation. This leads to clear code that’s easy to read and understand.

### Styling Functions

Functions should have descriptive names and these names should use lowercase letters and underscores.  

Every function should have a comment that explains concisely what the function does.  

If you specify a default value for a parameter, no spaces should be used on either side of the equal sign.  

[PEP 8](https://www.python.org/dev/peps/pep-0008/) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window.

## Chapter 9 - Classes

**classes** - classes combine functions and data into one neat package that can be used in flexible and efficient ways.  

Object-oriented programming is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes.  
Making an object from a class is called instantiation, and you work with instances of a class.  

**method** - a function that is a member of a class  

Any variable prefixed with `self` is available to every method in the class, and also able to be accessed through any instance created from the class.

**attributes** - variables that are accessible through instances  
**inheritance** - allows a class (child class) to have access to (inherit) all attributes, methods, and properties from another class (parent class)  

The parent class __init__() method is often needed to be called by a child class to initialize any attributes defined in the parent class.  
Child classes must be defined in the same file as the parent class.  
Example: `class ChildClass(ParentClass):`  

**super()** - the super function allows for calling a method from the parent class. The name "super" comes from a convention of calling the parent class a *superclass* and the child class a *subclass*  

**Override methods from the parent class** - Any method from the parent class can be overridden if it does not fit the model of the child class. To override a method inherited from the parent class, define a method in the child class with the same name as the method in the parent class you wish to override. Python will disregard the parent class method and only pay attention to the method defined in the child class.  

### Importing Classes

Python allows for storing classes in modules and importing them as needed into a program.  

### Importing Multiple Classes from a Module

As many classes as needed can be imported into a program file. If more than one class is needed, both classes will need to be imported into your file.  
Multiple classes from a module are imported by separating each class with a comma.  
Example: `from module_name import Class1, Class2`  

You can import every class from a module by using an asterisk (*)  
`from module_name import *`  
This method is not recommended for a few reasons:  

1. It's helpful to be able to read the import statements to gain an understanding of which classes a program uses.  
1. This approach can lead to confusion with names in the file.  

### Importing a Module into a Module

When classes are stored in several modules, a class in one module depends on a class in another module. When this is the case, you can import the required class into the first module.  

### Using Aliases

An alias can be used when importing classes. This is helpful if class names are long.  
Example: `from module_name import LongClassName as LCN`  

### The Python Standard Library

The Python Standard Library is a set of modules included with every Python installation. Any function or class in the standard library may be used by importing it into your code.  

### Styling Classes

Class names should be written in CamelCase and should not use underscores.  

Instance and module names should be written in lowercase with underscores between words.  

Every class should have a docstring immediately following the class definition giving a brief description of what the class does.  
Every module should also have a docstring to describe what the classes in a module can be used for.  

Blank lines should be used to organized code, but should not be used excessively.  
Within a class, use one blank line between methods and within a module, use two blank lines to separate classes.  

## Chapter 10 - Files and Exceptions
