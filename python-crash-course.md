---
id: python-crash-course
title: Python Crash Course
---

## Chapter 1 Notes - Getting Started

## Chapter 2 Notes - Variables and Simple Data Types

## Chapter 3 Notes - Introducing Lists

A list is a collection of items in a particular order.  

In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:

The simplest way to add a new element to a list is to append the item to the list.

You can add a new element at any position in your list by using the insert() method.

If you know the position of the item you want to remove from a list, you can use the del statement.

The pop() method removes the last item in a list, but it lets you work with that item after removing it.

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
