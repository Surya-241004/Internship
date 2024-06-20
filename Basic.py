Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=["abc,1,2,4,True,2.5]
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["abc"]
...    
>>> a.append("bike")
...    
>>> 
>>> print(a)
...    
['abc', 'bike']
>>> a.insert(-2,"bikw")
...    
>>> a.remove("car")
...    
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.remove("car")
ValueError: list.remove(x): x not in list
>>> print(a)
...    
['bikw', 'abc', 'bike']
>>> a.remove("car")
...    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.remove("car")
ValueError: list.remove(x): x not in list
>>> a.remove("a")
...    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.remove("a")
ValueError: list.remove(x): x not in list
>>> 
>>> del a[-1]
...    
>>> print[a]
...    
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d=festival
...    
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d=festival
NameError: name 'festival' is not defined
t=abcde
   
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t=abcde
NameError: name 'abcde' is not defined
t=("a","b",,1,2,3,True)
   
SyntaxError: invalid syntax
t=("a","b",1,2,3,True)
   
x=("absa","bads","cadsa")
   
z=("bafs","adsd")
   
a=x+z
   
y=list(x)
   
y[1]="kiwi"
   
x=tuple(y)
   
print(a)
   
('absa', 'bads', 'cadsa', 'bafs', 'adsd')
s={"a","adc","adc",1,45}
   
print(s)
   
{'a', 1, 45, 'adc'}
s.add("car")
   
print(s)
   
{1, 'a', 45, 'adc', 'car'}
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
    }
   
x=thisdict.updtae({"year":2020})
   
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x=thisdict.updtae({"year":2020})
AttributeError: 'dict' object has no attribute 'updtae'. Did you mean: 'update'?
x=thisdict.update({"year":2020})
   
x=thisdict["model"]
   
print(x)
   
mustang
y=thisdict.keys()
   
print(y)
   
dict_keys(['brand', 'model', 'year'])
thisdict.updtae({"model":Endeavour})
   
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    thisdict.updtae({"model":Endeavour})
AttributeError: 'dict' object has no attribute 'updtae'. Did you mean: 'update'?
thisdict.update({"model":Endeavour})
   
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    thisdict.update({"model":Endeavour})
NameError: name 'Endeavour' is not defined
x=thisdict["year"]
   
print(x)
   
2020
thisd={
    "a":BMW,
    "b":Benz
    }
   
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    "a":BMW,
NameError: name 'BMW' is not defined
thisdict["engine"]="V8"
   
print(thisdict)
   
{'brand': 'ford', 'model': 'mustang', 'year': 2020, 'engine': 'V8'}
del thisdict["year"]
   
print(thisdict)
   
{'brand': 'ford', 'model': 'mustang', 'engine': 'V8'}
