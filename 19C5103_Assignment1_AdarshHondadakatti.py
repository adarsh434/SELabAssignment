# Answer to question asked in class
'''
In Slicing it does not matter if the index given if out of range or not because, slicing is used to create a new list. If the indices don't fall within the range of the number of elements in the list, we can return an empty list. So, we don't have to throw an error.
But if we excess a single emelent from a list and that index is not available in the list then it will throw index out of bond exception.
eg: list = [1, 2, 3, 4, 5]
print(list[100]) # It will throw a exception
print(list[-100]) # it will throw a exception
print(list[0:100]) # no exception will be thrown, output will be [1, 2, 3, 4, 5]
print(list[-100:100]) # no exception will be thrown, output will be [1, 2, 3, 4, 5] 
'''


# LIST
# FEATURES
# - Lists are ordered.
# - Lists can contain any arbitrary objects.
# - List elements can be accessed by index.
# - Lists are mutable.
list1=['Adarsh', 1, 22.7, -1]
list2=[22, "Hello", 7]
print(list1) #output ['Adarsh', 1, 22.7, -1]

list1.append('World')
print(list1) #output ['Adarsh', 1, 22.7, -1, World]

list1.extend(list2)
print(list1) #output ['Adarsh', 1, 22.7, -1, World, 22, 'Hello', 7]

list1.insert(3,'Some Value') #insert()
print(list1) #output ['Adarsh', 1, 22.7, 'Some Value', -1, 'World', 22, 'Hello', 7]

print(list1.count(22)) #output 1

list1.remove(22.7)
print(list1) # output ['Adarsh', 1, 'Some Value', -1, 'World', 22, 'Hello', 7]


# TUPLES
# FEATURES
# - Tuples are defined in the same way as lists.
# - They are enclosed within parenthesis and not within square braces.
# - Elements of the tuple must have a defined order.
# - Tuples are immutable
tuple1 = ('computer', 'IT', 'CSB')
tuple2 = tuple(("apple", "banana", "cherry"))

print(tuple2) # output ["apple", "banana", "cherry"]

print(len(tuple1)) # output 3


# DICTIONARY
# FEATURES
# - Dictionaries are unordered.
# - Dictionaries have keys and value pairs.
# - Keys are unique.
# - Keys must be immutable.

# Creating a dictionary using empty brackets
dict1 = {1: 'A', 2: 'B', 3: 'C'}
print(dict1) # output {1: 'A', 2: 'B', 3: 'C'}

# Creating a dictionary by using dict constructor
dict2 = dict( Hello = 7, hi = 10, there = 45, at = 23, this = 77)
print(dict2) # output {'Hello': 7, 'hi': 10, 'there': 45, 'at': 23, 'this': 77}
print(dict2.keys())
print(dict2.get('Hello'))
 
# Creating dictionary by Dict Comprehension
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = [1, 2, 3, 4, 5]
decoding = {alphabet: number for alphabet, number in zip(list1, list2)}
print(decoding) # output {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}



# SETS
# FEATURES
# - Sets are unordered.
# - Set elements are unique. Duplicate elements are not allowed.
# - A set itself may be modified, but the elements contained in the set must be of an immutable type.

set1 = set([1, 1, 1, 2, 3, 4, 2, 3])
print(set1) #output {1, 2, 3, 4} 

set1.add(10)
print(set1) #output {1, 2, 3, 4, 10}

set1.remove(10)
print(set1) #output {1, 2, 3, 4} 

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #output {1, 2, 3, 'c', 'b', 'a'}
