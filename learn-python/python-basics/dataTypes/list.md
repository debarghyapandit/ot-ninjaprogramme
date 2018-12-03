# Python Basics : Data Types (List)

Theory Assignment: Read about Lists and its built-in functions.

**List**

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

```python

fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)

```

**Accessing items in List**

List items can be accessed by referring to the index number:

```python

fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[1])

```

**Change item value in list**

To change the value of a specific item, refer to the index number and update the value:

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "mango"
print(fruit_list)

```

**Looping Through a List**

We can loop through the list items by using a for loop:

```python

fruit_list = ["apple", "banana", "cherry"]
for x in fruit_list:
  print(x)

```

**Check if an Item Exists in List**

To determine if a specified item is present in a list use the in keyword:

```python

item = 'apple'
fruit_list = ["apple", "banana", "cherry"]
if item in fruit_list:
    print("Yes, item '{0}' is in the fruits list".format(item))

```

**Get Length of List**

We can use len() method, to determine no. of items in a list:

```python

fruit_list = ["apple", "banana", "cherry"]
print('No of items in fruits list: {0}'.format(len(fruit_list)))

```

**Add an Item to List**

To add an item to the end of the list, use the append() method:

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list.append("mango")
print(fruit_list)

```

To add an item at the specified index, use the insert() method:

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list.insert(1, "orange")
print(fruit_list)

```

**Remove an Item from List**

There are multiple methods to remove an item

- Using remove() method, removes the specified item:

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list.remove("banana")
print(fruit_list)

```

- Using pop() method, removes the specified index, (or the last item if index is not specified):

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list.pop()  # will remove item at last index: "cherry"
print(fruit_list)
fruit_list.pop(1) # will remove the item at index 1: "banana"
print(fruit_list)

```

- Using del keyword, removes the specified index:

```python

fruit_list = ["apple", "banana", "cherry"]
del fruit_list[0]
print(fruit_list)

```

- del keyword can also delete the list completely:

```python

fruit_list = ["apple", "banana", "cherry"]
del fruit_list
print(fruit_list) #this will cause an error because "thislist" no longer exists.

```

- Using clear() method, empties the list:

```python

fruit_list = ["apple", "banana", "cherry"]
fruit_list.clear()
print(fruit_list)

```

**Python Built in methods for List**

/***
<table class="tg">
<tr>
<th class="tg-yw4l"><b>Method<b></th>
<th class="tg-yw4l"><b>Description<b></th>
</tr>
<tr>
  <td class="tg-yw4l">append()</td>
  <td class="tg-yw4l">Adds an element at the end of the list</td>
</tr>
<tr>
  <td class="tg-yw4l">clear()</td>
  <td class="tg-yw4l">Removes all the elements from the list</td>
</tr>
<tr>
  <td class="tg-yw4l">copy()</td>
  <td class="tg-yw4l">Returns a copy of the list</td>
</tr>
<tr>
  <td class="tg-yw4l">count()</td>
  <td class="tg-yw4l">Returns the number of elements with the specified value</td>
</tr>
<tr>
  <td class="tg-yw4l">extend()</td>
  <td class="tg-yw4l">Add the elements of a list (or any iterable), to the end of the current list
  </td>
</tr>
<tr>
  <td class="tg-yw4l">index()</td>
  <td class="tg-yw4l">Returns the index of the first element with the specified value</td>
</tr>
<tr>
  <td class="tg-yw4l">insert()</td>
  <td class="tg-yw4l">Adds an element at the specified position</td>
</tr>
<tr>
  <td class="tg-yw4l">pop()</td>
  <td class="tg-yw4l">Removes the element at the specified position</td>
</tr>
<tr>
  <td class="tg-yw4l">remove()</td>
  <td class="tg-yw4l">Removes the item with the specified value</td>
</tr>
<tr>
  <td class="tg-yw4l">reverse()</td>
  <td class="tg-yw4l">Reverses the order of the list</td>
</tr>
<tr>
  <td class="tg-yw4l">sort()</td>
  <td class="tg-yw4l">Sorts the list</td>
</tr>
</table>

***/
