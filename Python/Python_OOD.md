## Class Related Knowledge
#### 1. Basic concepts in OOP: Abstraction, Polymorphism, Encapsulation, Inheritance 
    * The abstraction is simplifying complex reality by modeling classes appropriate to the problem. The polymorphism is the process of using an operator or function in different ways for different data input. The encapsulation hides the implementation details of a class from other objects. The inheritance is a way to form new classes using classes that have already been defined.

#### 2. Class Attributes
* Basic configuration

```python
#!/usr/bin/python

# initialize.py


class Cat:
   def __init__(self, name):
      self.name = name


missy = Cat('Missy')
lucky = Cat('Lucky')

print missy.name
print lucky.name
```
* In this code example, we have a Cat class. The special method __init__() is called automatically right after the object has been created. Each method in a class definition begins with a reference to the instance object. It is by convention named self. There is nothing special about the self name. We could name it this, for example. The name is the argument. The value is passed during the class instantiation.

* The atributes can be assigned dynamically, not just during initialization. This shows the next example.

```python
#!/usr/bin/python

# dynamic.py

class Dynamic:
   pass

d = Dynamic()
d.name = "Dynamic"
print d.name

# Output:
$ ./dynamic.py 
Dynamic
```
* So far, we have been talking about the instance attributes. In Python there are also so called class object attributes. Class object attributes are same for all instances of a class.

```python
# cat.py

class Cat:
   species = 'mammal'

   def __init__(self, name, age):
      self.name = name
      self.age = age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print missy.name, missy.age
print lucky.name, lucky.age

print Cat.species
print missy.__class__.species   # Two ways to access the class object attributes
print lucky.__class__.species
```

#### 3. Class Methods
* In Python, we can call methods in two ways. There are bounded and unbounded method calls.
* [bound, unbound, static](http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static)

```python

class Methods:
   def __init__(self):
      self.name = 'Methods'

   def getName(self):
      return self.name


m = Methods()

print m.getName()   # Bounded method call
print Methods.getName(m) # Unbounded method call 
```

* [Special Methods](http://zetcode.com/lang/python/oop/)


```python

#!/usr/bin/python

# book.py

class Book:
   def __init__(self, title, author, pages):
      print "A book is created"
      self.title = title
      self.author = author
      self.pages = pages

   def __str__(self):
      return "Title:%s , author:%s, pages:%s " % \
              (self.title, self.author, self.pages)

   def __len__(self):
      return self.pages

   def __del__(self):
      print "A book is destroyed"


book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print book  
# The print keyword calls the __str__() method. This method should return an informal string representation of an object.

print len(book)
# The len() function invokes the __len__() method. In our case, we print the number of pages of our book.

del book
# The del keyword deletes an object. It calls the __del__() method.
```

#### 4. Object and Type
##### 1. Everything is an object 
* Any classes that we define are objects, and of course, instances of those classes are objects as well.

``` python
>>> two = 2  # 1
>>> type(two)  # 3
<type 'int'>
>>> two.__class__  # 3 
<type 'int'>
>>> 
>>> type(type(two))
<type 'type'>
>>> type(two).__class__ 
<type 'type'>
>>> int
<type 'int'>
>>> type(int)
<type 'type'>
>>>  
>>> i = int(3)  # 2
>>> type(i)
<type 'int'>
>>> type(3)
<type 'int'>
>>> i.__class__
<type 'int'>
```
* Note 1), 2), we create the python in_build int instance, the type of these instance is 'int' 
* Note 3), In Python, the type of an object is represented by the class used to build the object: that is, in Python the word type has the same meaning of the word class.

``` python
>>> object  # 1) 
<type 'object'>
>>> type    # 2) 
<type 'type'>

>>> type(object)  # 3) 
<type 'type'>
>>> object.__class__  # 4) 
<type 'type'>
>>> object.__bases__
()

>>> type.__class__
<type 'type'>
>>> type.__bases__
(<type 'object'>,)

>>> isinstance(object, object)
True
>>> isinstance(type, object)
True

```

* 1), 2) The names of the two primitive objects within Python. Earlier type() was introduced as a way to find the type of an object (specifically, the __class__ attribute). In reality, it is both an object itself, and a way to get the type of another object.
* 3), 4) Exploring <type 'object'>: the type of <type 'object'> is <type 'type'>. We also use the __class__ attribute and verify it is the same as calling type()
* 个人理解：每一个class, 包括class 的instance都是object，例如我们定义 ```i = 2; i = int(2) ```,实际上是定义了int class 的一个instance i, 所以type(i) 相当于 ```i.__class__() ```返回的是 ```type 'int'```. 对于object来说, type(object)是一个type，所以object.__class__是type，而对于type来说，它的type就是它本身，所以它本身的class就是type. 但是它的bases是建立在object上面的，所以在python里面，type和object是相辅相成的。
* These two objects are primitive objects in Python. We might as well have introduced them one at a time but that would lead to the chicken and egg problem - which to introduce first? These two objects are interdependent - they cannot stand on their own since they are defined in terms of each other.

#### 5. Type Object 
* Type and classes are readlly the SAME in Python !!
* Class is Type, Type is Class ! 
* Type objects share the following traits:
      * They are used to represent abstract data types in programs. For instance, one (user defined) object called User might represent all users in a system, another once called int might represent all integers.
      * They can be subclassed. This means you can create a new object that is somewhat similar to exsiting type objects. The existing type objects become bases for the new one.
      * They can be instantiated. This means you can create a new object that is an instance of the existing type object. The existing type object becomes the __class__ for the new object.
      * The type of any type object is <type 'type'>.
      * They are lovingly called types by some and classes by others.

#### 6. Type Or Non-type Test Rule 
##### If an object is an instance of <type 'type'>, then it is a type. Otherwise, it is not a type !! 
* Summarize: 
      1. <type 'object'> is an instance of <type 'type'>.
      2. <type 'object'> is a subclass of no object.
      3. <type 'type'> is an instance of itself.
      4. <type 'type'> is a subclass of <type 'object'>.
      5. There are only two kinds of objects in Python: to be unambiguous let's call these types and non-types. Non-types could be called instances, but that term could also refer to a type, since a type is always an instance of another type. Types could also be called classes, and I do call them classes from time to time.

* For example:

```python
>>> list
<type 'list'>  # the build-in <type 'list'> object
>>> list.__class__  # it's type is <type 'type'>
<type 'type'>
>>> list.__bases__
(<type 'object'>,)
>>> tuple.__class__, tuple.__bases__ 
(<type 'type'>, (<type 'object'>,))
>>> dict.__class__, dict.__bases__
(<type 'type'>, (<type 'object'>,))
>>>
>>> mylist = [1,2,3]
>>> mylist.__class__  # the type of the mylist here is the 'list'
<type 'list'>
```

* 个人理解，对于build-in type比如list，tuple来说，我们create了一个mylist, 实际上是create了list class 的instance，所以type(mylist) or mylist.__class__是<type 'list'>, 对于class C, 来说，我们相当于create了一个class类的instance，所以type(C)为classobj, 在我们create一个class D的继承C时候，create 一个classobj

```
>>> class C:
...     pass
>>> type(C)
<type 'classobj'>
>>> class D(C):
...     pass
>>> type(D)
<type 'classobj'>
```

* New Objects by subclass
* The built-in objects are, well, built into Python, like list, typle, classobj. They're there when we start Python, usually there when we finish. So how can we create new objects? New objects cannot pop out of thin air. They have to be built using existing objects.
* For example:

```python
# In python 2.7
>>> class C(object):
...     pass
... 
>>> class D(C):
...     pass
... 
>>> type(D)     # Create a new object !
<type 'type'>
>>> D.__class__
<type 'type'>
>>>
>>> class C:   
...     pass
... 
>>> class D(C):   
...     pass
... 
>>> type(D)      # C and D are still the class obj
<type 'classobj'>
>>> type(C)
<type 'classobj'>
>>> 

# In Python 3.x, the explicit base class is not required, classes are
# automatically subclasses of object:
Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> class C:
...    pass
... 
>>> type(C)
<class 'type'>
>>> 
>>> class D(C):
...   pass
... 
>>> type(D)
<class 'type'>
```
```python
# In Python 2.x:
class C(object):  # 1) 
 pass
# In Python 3.x, the explicit base class is not required, classes are
# automatically subclasses of object:
class C:  # 2) 
 pass
class D(object):
 pass
class E(C, D):  # 3) 
 pass
class MyList(list):  # 4) 
 pass 
````
      * 1) The class statement tells Python to create a new type by subclassing an existing type.
      * 2) Don't do this in Python 2.x or you will end up with an object that is an old-style class, everything you read here will be useless and all will be lost.
      * 3) Multiple bases are fine too.
      * 4) Most built-in types can be subclassed (but not all). After the above example, C.__bases__ contains <type 'object'>, and MyList.__bases__ contains <type 'list'>.
      * 5) The types.ClassType object is in some ways an alternative <type 'type'>. Instances of this object (classic classes) are types themselves. The rules of attribute access are different for classic classes and new-style classes. The types.ClassType object exists for backward compatibility and may not exist in future versions of Python. Other sections of this book should not be applied to classic classes.

#### 7. New Objects by Instantiating

```python
obj = object()    # 1) 
cobj = C()        # 2)
mylist = [1,2,3]  # 3) 
```

* 1), 2) The call operator (()) creates a new object by instantiating an existing object. The existing object must be a type. Depending on the type, the call operator might accept arguments.
* 3) Python syntax creates new objects for some built-in types. The square brackets create an instance of <type 'list'>; a numeric literal creates an instance of <type 'int'>

#### 8. Wrap Up

* The Python Objects Map
![pic](https://cloud.githubusercontent.com/assets/9062406/7671625/322ae91c-fc8d-11e4-91fc-81fce875b93e.png)

* To summarize all that has been said:
      * There are two kinds of objects in Python:
         * 1. Type objects - can create instances, can be subclassed.
         * 2. Non-type objects - cannot create instances, cannot be subclassed.

* <type 'type'> and <type 'object'> are two primitive objects of the system.
* objectname.__class__ exists for every object and points the type of the object.
* bjectname.__bases__ exists for every type object and points the superclasses of the object. It is empty only for <type 'object'>.
* To create a new object using subclassing, we use the class statement and specify the bases (and, optionally, the type) of the new object. This always creates a type object.
* To create a new object using instantiation, we use the call operator (()) on the type object we want to use. This may create a type or a non-type object, depending on which type object was used.
* Some non-type objects can be created using special Python syntax. For example, [1, 2, 3] creates an instance of <type 'list'>.
* Internally, Python always uses a type object to create a new object. The new object created is an instance of the type object used. Python determines the type object from a class statement by looking at the bases specified, and finding their types.
* issubclass(A,B) (testing for superclass-subclass relationship) returns True iff:
      * 1. B is in A.__bases__, or
      * 2. issubclass(Z,B) is true for any Z in A.__bases__.
* isinstance(A,B) (testing for type-instance relationship) returns True iff:
      * 1. B is A.__class__, or
      * 2. issubclass(A.__class__,B) is true.
* Squasher is really a python. (Okay, that wasn't mentioned before, but now you know.) 

#### More Data points

```python
>>> import types
>>> types.ListType is list
True
>>> def f():
... pass
...
>>> f.__class__ is types.FunctionType
True
>>>
>>> class MyList(list):  # Some built-in types can be subclassed.
... pass
...
Python Types and Objects 13
>>> class MyFunction(types.FunctionType):  # Some built-in types can not be subclassed.
... pass
...
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
TypeError: type 'function' is not an acceptable base type
>>> dir(types)
['BooleanType', 'DictProxyType', 'DictType', ..]
```

* If X is an instance of A, and A is a subclass of B, then X is an instance of B as well.
* If B is an instance of M, and A is a subclass of B, then A is an instance of M as well.


#### Descripter

```python
class Descripter(object):
    def __get__(self, obj, cls = None):
        print "get_func !, obj: ", obj

    def __set__(self, obj, val):
        print "set func: val: ", val

    def __delete__(self, obj):
        print "delete: obj:", obj

class C(object):
    d = Descripter()


cobj = C()
x = cobj.d
cobj.d = 'set a value'
cobj.__dict__['d'] = 'try to force a value'
x = cobj.d
print "xcobj.d ", x
del cobj.d

print "\n after reset d"
x = cobj.d
print "x: ",x
cobj.d = 'set a value'
print "cobj.d: ", x
print "cobj.__dict__", cobj.__dict__['d']
print "x: ", x

print "\n after reset x"
x = C.d
C.d = 'set a value on class'
print "x: ", x
print "C.__dict__", C.__dict__
print "x.__dict__", x.__dict__

>>> ================================ RESTART ================================
>>> 
get_func !, obj:  <__main__.C object at 0x1063fee50>
set func: val:  set a value
get_func !, obj:  <__main__.C object at 0x1063fee50>
xcobj.d  None
delete: obj: <__main__.C object at 0x1063fee50>

 after reset d
get_func !, obj:  <__main__.C object at 0x1063fee50>
x:  None
set func: val:  set a value
cobj.d:  None
cobj.__dict__ try to force a value
x:  None

 after reset x
get_func !, obj:  None
x:  None
C.__dict__ {'__dict__': <attribute '__dict__' of 'C' objects>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'C' objects>, 'd': 'set a value on class', '__doc__': None}
x.__dict__

Traceback (most recent call last):
  File "/Users/jinzh2/Desktop/Python_training/Leetcode/descripter.py", line 36, in <module>
    print "x.__dict__", x.__dict__
AttributeError: 'NoneType' object has no attribute '__dict__'
```

#### Descripter Reference
* [装饰器，descripter中文教程] (http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000)
* [Descripter tutorial](https://docs.python.org/2/howto/descriptor.html)

####  [Class Inheritance](https://docs.python.org/2/tutorial/classes.html#multiple-inheritance)
####  [What's metaclass ?](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)

