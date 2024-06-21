# Hashable list Python Library
A new class that allows you to create a `HashtableList` object that repeats the functionality of the built-in list type, but is hashed.

Due to this, objects of the `HashtableList` class can be used as a key in `dict` and a member in `set`.

### Example
```
>> import HashableList

>> hashable_list  =  HashableList([1, 2, 3])
>> dictionary  = {hashable_list: "value"}  
>> dictionary
{[1, 2, 3]: "value"}

>> id(hashable_list)
4429867792
>> hashable_list.append(4)
>> id(hashable_list)
4429867792  # this is the same object after append

>> dictionary
{[1, 2, 3, 4]: "value"}
```