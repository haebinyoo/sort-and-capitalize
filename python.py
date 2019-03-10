Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = ["Grace Yoo", "Joshua Harrison", "Matthew Marrison", "Jacob Spanjer"]
>>> list1.sort()
>>> list1
['Grace Yoo', 'Jacob Spanjer', 'Joshua Harrison', 'Matthew Marrison']
>>> def SortBySec(element):
	return element[1]

>>> list1
['Grace Yoo', 'Jacob Spanjer', 'Joshua Harrison', 'Matthew Marrison']
>>> def SortBySec(element):
	return element[1]

>>> list1.sort(key=SortBySec)
>>> list1
['Jacob Spanjer', 'Matthew Marrison', 'Joshua Harrison', 'Grace Yoo']
>>> list1 = ["Grace, Yoo", "Joshua, Harrison", "Matthew, Marrison", "Jacob, Spanjer"]
>>> list1
['Grace, Yoo', 'Joshua, Harrison', 'Matthew, Marrison', 'Jacob, Spanjer']
>>> list1.sort()
>>> list
<class 'list'>
>>> list1
['Grace, Yoo', 'Jacob, Spanjer', 'Joshua, Harrison', 'Matthew, Marrison']
>>> list1.sort(key=len)
>>> list1
['Grace, Yoo', 'Jacob, Spanjer', 'Joshua, Harrison', 'Matthew, Marrison']
>>> def SortBySec(element):
	return element[1]

>>> list1.sort(key=SortBySec)
>>> list1
['Jacob, Spanjer', 'Matthew, Marrison', 'Joshua, Harrison', 'Grace, Yoo']
>>> list1.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list1.sort(reverse=true)
NameError: name 'true' is not defined
>>> list1
['Jacob, Spanjer', 'Matthew, Marrison', 'Joshua, Harrison', 'Grace, Yoo']
>>> list1.sort(key=len)
>>> list1
['Grace, Yoo', 'Jacob, Spanjer', 'Joshua, Harrison', 'Matthew, Marrison']
>>> list1.sort(reverse=True)
>>> list1
['Matthew, Marrison', 'Joshua, Harrison', 'Jacob, Spanjer', 'Grace, Yoo']
>>> list1.sort()
>>> list1
['Grace, Yoo', 'Jacob, Spanjer', 'Joshua, Harrison', 'Matthew, Marrison']
>>> list1.sort(key=lambda x: x.split()[1])
>>> list1
['Joshua, Harrison', 'Matthew, Marrison', 'Jacob, Spanjer', 'Grace, Yoo']
>>> list1.sort()
>>> list1
['Grace, Yoo', 'Jacob, Spanjer', 'Joshua, Harrison', 'Matthew, Marrison']
>>> list1 = ["grace yoo", "joshua harrison", "matthew marrison", "jacob spanjer"]
>>> list1
['grace yoo', 'joshua harrison', 'matthew marrison', 'jacob spanjer']
>>> import string
>>> string.capwords("list1")
'List1'
>>> import string
>>> string.capwords["grace yoo"]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    string.capwords["grace yoo"]
TypeError: 'function' object is not subscriptable
>>> list1
['grace yoo', 'joshua harrison', 'matthew marrison', 'jacob spanjer']
>>> list1.title()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    list1.title()
AttributeError: 'list' object has no attribute 'title'
>>> "grace yoo".title()
'Grace Yoo'
>>> print(list1.capitalize())
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(list1.capitalize())
AttributeError: 'list' object has no attribute 'capitalize'
>>> list1
['grace yoo', 'joshua harrison', 'matthew marrison', 'jacob spanjer']
>>> list1.sort(key=len)
>>> list1
['grace yoo', 'jacob spanjer', 'joshua harrison', 'matthew marrison']
>>> list1.sort(reverse=True)
>>> list1
['matthew marrison', 'joshua harrison', 'jacob spanjer', 'grace yoo']
>>> def SortBySec(element)
SyntaxError: invalid syntax
>>> def SortBySec(element)
SyntaxError: invalid syntax
>>> def SortBySec(element):
	return element[1]

>>> list1
['matthew marrison', 'joshua harrison', 'jacob spanjer', 'grace yoo']
>>> list1.sort(key=SortBySec)
>>> list1
['matthew marrison', 'jacob spanjer', 'joshua harrison', 'grace yoo']
>>> list1
['matthew marrison', 'jacob spanjer', 'joshua harrison', 'grace yoo']
>>> list1.sort()
>>> list1
['grace yoo', 'jacob spanjer', 'joshua harrison', 'matthew marrison']
>>> [element upper() for element in list]
SyntaxError: invalid syntax
>>> [element.upper() for element in list]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    [element.upper() for element in list]
TypeError: 'type' object is not iterable
>>> [element.upper() for element in list1]
['GRACE YOO', 'JACOB SPANJER', 'JOSHUA HARRISON', 'MATTHEW MARRISON']
>>> [element.lower() for element in list1]
['grace yoo', 'jacob spanjer', 'joshua harrison', 'matthew marrison']
>>> list1.upper()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list1.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> [element.upper() for element in list1]
['GRACE YOO', 'JACOB SPANJER', 'JOSHUA HARRISON', 'MATTHEW MARRISON']
>>> list1
['grace yoo', 'jacob spanjer', 'joshua harrison', 'matthew marrison']
>>> [element.upper() for element in list1]							element=element.title()
SyntaxError: invalid syntax
>>> element=element.title
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    element=element.title
NameError: name 'element' is not defined
>>> list1=list1.title()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list1=list1.title()
AttributeError: 'list' object has no attribute 'title'
>>> element =input()
	element=element.title()
>>> list1
['grace yoo', 'jacob spanjer', 'joshua harrison', 'matthew marrison']
>>> list1 = [element.upper() for element in list1]
>>> list1
['GRACE YOO', 'JACOB SPANJER', 'JOSHUA HARRISON', 'MATTHEW MARRISON']
>>> element=element.title()
>>> list1
['GRACE YOO', 'JACOB SPANJER', 'JOSHUA HARRISON', 'MATTHEW MARRISON']
>>> list1 =list1.title()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list1 =list1.title()
AttributeError: 'list' object has no attribute 'title'
>>> a = "james morris"
>>> a.title()
'James Morris'
>>> list1.title()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list1.title()
AttributeError: 'list' object has no attribute 'title'
>>> b = ["james morris", "bob plankton", "steven queen"]
>>> b=b.title()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    b=b.title()
AttributeError: 'list' object has no attribute 'title'
>>> b.title()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    b.title()
AttributeError: 'list' object has no attribute 'title'
>>> b.capitalize()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b.capitalize()
AttributeError: 'list' object has no attribute 'capitalize'
>>> string_name.capitalize()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    string_name.capitalize()
NameError: name 'string_name' is not defined
>>> print(b.capitalize)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(b.capitalize)
AttributeError: 'list' object has no attribute 'capitalize'
>>> 
