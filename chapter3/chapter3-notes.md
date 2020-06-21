# Chapter 3 - Introducing Lists Notes

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
