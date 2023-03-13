# Python_Core_Practice

We have every thing From start to end with complete path
string :- learn slicing, row string(r''), skip special meaning("meaning\"s") and many more string method, immutable datatype

list : list slicing, list is mutable data type, list = [it can be anything] it allow duplicate value

set : set ={} does not allow duplicate value, set can be in unorderd way, set is also a mutable data type

dictionary : dictionary = {key : value} dictioanry have key and value pair you can get the value with the help of
dictionary[key], it also is mutable data type, dictionary can contain dictionary and list in dictionary
like example : dictionary = {'abc' : [1,2], 'bca' : {'aa' : 'bb'}}
you can fetch the data with
dictionary['abc']
dictionary['bca']['aa']
key has to be unique value can be repetad
  
tuple : tuple is immutable data type once you asign a value in that you cannot change it tuple = ()

variable : there is not constant variable in python insted of that we just saw the current variable is constant or not
with the help of capital letter variable assign like for example : PI = 3.14
And all the value store in variable it depend what we choose name of that variable like a or b or like pro
programmer you can asign close to what value you store like name = 'your name' with this method the
reader who read your code it get help to understand what mean of this variable
after using variable is that value does not used right now that at that point garbage collection is being used

Data types : None : That variable we dont asign any value we can call none like example : a = None after this we can change the value of it
Numeric : int : a = 1,float : b= 2.5,complex : a = 6+9j ,bool : a = True or False
List : lst = []
Tuple : tup = ()
Set : set = {}
String : str = '' or ""
Range : range(start, excluded end, step) example list(range(1,3)) output = [1,2], step means how many steps
need to skip from start to end
Dictionary : dict = {key : value}, key has to be unique value can be repetad

    	You can use type conversion to convert a type of a specific variable like a = data_type(value)
    	example :
    		  a = 10.5
    		  b = int(a)
    			you can also check with the help of type to check type of specific variable
    			print(type(b))
    			It will return : <class 'int'>

Understand about operator like airethmatic operator, logical etc.
Understand about hexadicimal, dicimal, binary, and octal.

Learn swapping :
with third variable
a = 5,b = 6
temp = a
a = b
b = temp
second method without third variable
a = a+b in this a+b = 11
b = a-b in this a-b = 11-6 = 5
a = a-b in this a-b = 11-5 = 6
But in this we use one extra bit(11)
third method without third variable
a = a xor(^) b
b = a xor(^) b
a = a xor(^) b
fourth method only for python
a,b = b,a
This work like our system initialy run right side first sor first b,a is solved b = 6 and a = 5
this goes to stack and it reverse in stack (ROT_TWO() swap the two top-most stack items.)
so beacuse of this the value of b comes into a and a comes into b it just a rotating a
value and after that it initialized to a and b thats how this swap work \* From stackoverflow : Python separates the right-hand side expression from the left-hand side assignment.
First the right-hand side is evaluated, and the result is stored on the stack,
and then the left-hand side names are assigned using opcodes that take values from the stack again. >>> import dis >>> def foo(a, b):
... a, b = b, a
... >>> dis.dis(foo)
2 0 LOAD_FAST 1 (b)
3 LOAD_FAST 0 (a)
6 ROT_TWO  
 7 STORE_FAST 0 (a)
10 STORE_FAST 1 (b)
13 LOAD_CONST 0 (None)
16 RETURN_VALUE
After the two LOAD_FAST opcodes (which push a value from a variable onto the stack),
the top of stack holds [a, b]. The ROT_TWO opcode swaps the top two positions on the stack so
the stack now has [b, a] at the top. The two STORE_FAST opcodes then takes those two values and
store them in the names on the left-hand side of the assignment. The first STORE_FAST pops a
value of the top of the stack and puts it into a, the next pops again, storing the value in b.
The rotation is needed because Python guarantees that assignments in a target list on the
left-hand side are done from left to right.

    	For longer left-hand-side assignments, an explicit tuple is built:

    	>>> def bar(a, b, c, d):
    	...     d, c, b, a = a, b, c, d
    	...
    	>>> dis.dis(bar)
    	  2           0 LOAD_FAST                0 (a)
    	              3 LOAD_FAST                1 (b)
    	              6 LOAD_FAST                2 (c)
    	              9 LOAD_FAST                3 (d)
    	             12 BUILD_TUPLE              4
    	             15 UNPACK_SEQUENCE          4
    	             18 STORE_FAST               3 (d)
    	             21 STORE_FAST               2 (c)
    	             24 STORE_FAST               1 (b)
    	             27 STORE_FAST               0 (a)
    	             30 LOAD_CONST               0 (None)
    	             33 RETURN_VALUE

    		Here the stack with [d, c, b, a] is used to build a tuple (in reverse order, BUILD_TUPLE pops
    		from the stack again, pushing the resulting tuple onto the stack), and then UNPACK_SEQUENCE pops
    		the tuple from the stack again, pushes all elements back from the tuple back onto the stack again
    		for the STORE_FAST operations.

    		The latter may seem like a wasteful operation, but the right-hand side of an assignment may be
    		something entirely different, a function call that produces a tuple perhaps, so the Python
    		interpreter makes no assumptions and uses the UNPACK_SEQUENCE opcode always. It does so even for
    		the two and three-name assignment operations, but a later (peephole) optimization step replaces a
    		BUILD_TUPLE / UNPACK_SEQUENCE combination with 2 or 3 arguments with the above ROT_TWO and
    		ROT_THREE opcodes for efficiency.

Bitwise operator : one's complement(~), bitwise And(&), bitwise or(|), xor(^), left shift(<<), right shift(>>)

: Learn User input in python

: Learn about CPU(we are working on memory unit till now to store data now we user ALU(airethmatic/logical unit))

: Before leraning if learn about flowcharts it it good to know basics

: learn IF, IF else, if else if, for loop, while loop, break, continue, pass

: now do some basic pattern practice for quick refreshment of all learning

: learn for else

: learn about array in python and its type code, c type,python type, and min size in bytes to take to store

: learn algorithm

: Learn about the user input in array , deletion of array and reverse a array with the help of algorithm

: Learn on numpy array how it work different way to create it

: learn about copy array in numpy
arr = array([1,2,3])
you can copy array with this
arr1 = arr
but array don't going to be created again but both the variable will point at same array
if you check both element id you can see both have same id

    there are two types of copying
     1: shallow copying
     2: deep copying
    	1 :
    	 in shallow copying both are dependent to each other
    	 if you change one of the array value than it will change to other as well as
    	 	we can copy with the help of view function in this function id will be different

    		arr1 = arr.view()

    	2 :
    	  in deep copy if you change the value of one array after initialized the copy than the
    	  second array don't going to be change
    	  and also in this both the variable id will be different

    	  we will use copy function to deep copy a array

    	  arr1 = arr.copy()

: learn about function

: different types of arguments
1: actual arguments
2: formal arguments
1 : actual arguments :::
i : position
ii : keyword
iii : default
iv : variable length
i : while giving value to function you have to make sure about position of passing a value
because it depend which function variable will hold the value when calling the function
ii : in position we simply do
function_name(age = 2, name = 'xyz')
iii : def person(name,age=18):
print(name,age)
person('xyz')
so in this if you don't pass value than it will take default value that you assign to a
function in this case its age=18
iv : def sum (a,\*b):
c = a
for i in b:
c += i
print(c)
sum(1,2,3,4)
this method comes to an help when we don't know how many argument we will pass in function
in this example a is confirm 1 and other value will be assign to a b in tuple format
so we iterate through each of them and print sum of all value
:: kwargs :

    		def person(name, **data):
    			print(name)
    			print(data)

    		person('xyz',city = 'abc',age = 20, mob = 1234 )

    		output :
    		   xyz
    		   {'city':'abc','age':20,'mob':1234}

    		   when you want to pass multiple value with key we will use kwargs(**)

: learn about keyword like global and local variable learn about global and globals

: practice all thing in function

: learn recursion in function

: learn about lambda function

: learn about module and how to use it for big projects , simply mean break down big file into small file

: learn about special variable **name**

:----- now start learning oop(object oriented programming)
: get some information about classes and objects : object is an instance of a class
you can say class is a blueprint of a particular thing

: learn about methods and special methods do some practice of it

: learn about constructor and self

: learn about types of variable in oop like class variable(It's also called static variable) and instance variable

: learn about types of method :
class method
instance method
static method

: learn about inner class

: learn inheritance

: learn polymorphism

: learn method overloading(but in python we don't have this we can not create two method with the same name)
and method overriding

: learn about abstract classes and abstract methods

: learn iterator

: learn try, except and finally

: learn about multi threading

: learn file handling

: learn about comments

: learn what language python is like compiled or interpreted

: learn about searching algorithm and sorting algorithm

: learn to connect database
