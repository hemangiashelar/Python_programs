Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1="hello"
>>> str2="PYTHON"
>>> str3="gooD Morning"
>>> print(str1)
hello
>>> print(str2)
PYTHON
>>> print(str3)
gooD Morning
>>> 
>>> str4=str1.upper()
>>> print(str4)
HELLO
>>> str5=str2.lower()
>>> print(str5)
python
>>> str6=str3.()
SyntaxError: invalid syntax
>>> str6=str3.capitalize()
>>> print(str6)
Good morning
>>> str7=str3.swapcase()
>>> print(str7)
GOOd mORNING
>>> 
>>> l=length(str1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l=length(str1)
NameError: name 'length' is not defined
>>> l=len(str1)
>>> print(l)
5
>>> print(str1.islower())
True
>>> print(str2.islower())
False
>>> str8="PYTHON8"
>>> 