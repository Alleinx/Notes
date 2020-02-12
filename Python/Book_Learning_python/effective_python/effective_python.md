## Structure:
- Chapter
    - Item

## Chapter1: Pythonic Thinking
- Item1: Python Version, [skip]

- Item2: Follow the PEP8 Style Guide
    - Ref: https://www.python.org/dev/peps/pep-0008/
    - Few Rules:
        - Whitespace:
            - Use spaces instead of tabs for indentation and 4 spaces for indentation.
            - Continuations of long expressions onto additional lines should be indented by 4 extra spaces from their indentation level.
            - No spaces around (list_index, slice, kw_assignments).
        - Naming:
            - Class and Exception           :CamelNaming.
            - func, var, attr               :lowercase_underscore.
            - Module-level constant         :ALL_CAPS
            - Class methods should use ```cls``` as the name of the first parameter.
        - Expressions & statements:
            - ```if not sth```              :to check whether sth is empty (```[], ''```);
                - ```if a is not b```
            - ```if sth is not None```      :to check whether sth is None;
                - Be careful when checking sth is "empty" or "None".
- Item3: Differences between str, bytes, unicode, [skip]

- Item4: Write Helper Functions instead of Complex Expressions
    - As soon as expressions get complicated, it's time to wrap them into functions.
        - One statement/function does 1 thing; Don't mix too many functionalities into 1 statement/function.
    - Make good use of ternary statement        : ```value_1 if condition else value_b```.
        - Instead of boolean operators.

- Item5: Know How to Slice Sequence
    - Slicing can be extended to classes that implements the ```__getitem__()``` and ```__setitem__()``` method.
    - Beware the negative and 0 index can get surprising results from slicing.
        - ```list[-0:]```       :return a copy of original list.
    - Slicing is forgiving of out-of-bound indexes.

- Item 6|7, [skip]

- Item8: Avoid More than 2 Expressions in List Comprehensions.

- Item9: Consider Generator for huge amount of data.
    - Save memory (Lazy unpacking).

- Item10: consider ```enumerate()``` rather than ```range()```
    - Useful when want to know the index of current item during iteration.

- Item11: use ```zip``` to process iterators in parallel
    - In python3.x, ```zip()``` returns a lazy "generator".
    - Use ```itertools.zip_longest()``` to avoid truncating behavior.

- Item12: Avoid ```else``` blocks after ```{for/while}``` loops "entirely".
    - The ```else``` block after a loop "only runs" if the loop body "didn't" encounter a ```break``` statement.

- Item13: Take Advantage of Each Block in ```try/except/else/finally```
    - Use ```try/finally``` when you want exceptions to propagate up.
        - Usually as the cleanup code.
        - ```finally``` will always be executed even if there's return in the ```try/except/else``` blocks.
    - Use ```Else``` blocks to minimize the amount of code in ```try``` block and improves readability.
        - Could also be used to decide which exception is approprate to be threw out.
        - It's intuitive to put additional operations or a return value in ```else``` block if no exceptions were threw out.
            - And ```finally``` block will always be executed.

## Chapter2: Functions
- Item14: Prefer Exceptions to Returning None (!)
    - In most cases, raise exceptions instead of returning "None" value when handling errors in a helper function. (!)
    - And it's more intuitive to let the caller handle the exceptions by themselves, instead of returning a "None" value.

- Item15: Know how closures interact with Variable Scope
    - Python support "closures": methods that refer to variables from the the scope in which they were defined.
        - That's why methods defined in a file could refer to all "global variables" in that file.
    - When sort tuples, Python will first compares items in index 0, then 1, and so on.

    - Reference Scope traverse order:
        1. The current function's scope.
        2. Any Enclosing scopes(other containing functions if any).
        3. The scope of module contains the code (so-called the *global scope*).
        4. The built-in scope.
        5. Raise a **NameError** exception if not found the reference name.

    - Assigning value scope traverse order is different:
        - If the variable is defined in the current scope, then the value is assigned to it.
        - If the variable doesn't exist in the current scope, then Python treats the assignment as "a variable definition", and the scope of this variable stays inside the definied function (local scope).
            - To expand the local scope variable, use ```nonlocal``` keyword.
            - And the scope becomes "[1-2]" of reference scope; Module and built-in scope is not included.
            - Try to avoid using ```nonlocal``` keyword; And if needed, create a class to include and track variables need ```nonlocal``` keyword.


- Item16: Consider Generators instead of Returning Lists. (!)
    - When need to write a function that process a sequence of data and return a sequence of result, conxider Generator instead of returning List.
        - Commonly used in user iterable object.
    - Syntax: ```... yield value ...```.
    - **Beware**: generator results can only be iterated once; If need to store the result, store result in list/array first, or use defensive iterating rules.


- Item17: **Be Defensive when iterating over arguments** (!)
    - Beware of functions that iterate over *input arguments multiple times*. If these arguments are iterators, you may missing values after the first traverse.
        - You can convert the argument into a container, but will consume lots of memory if the obj is large.
        - Or be defensive: You can detect an obj is an iterator instead of a container by using ```iter(obj) is iter(obj)```, and only manipulate container obj. Outside iterator will be exhausted if used inside a method.

    - You can define your own iterable obj by implementing the ```__iter__()``` method as a generator.
        - when use ```for``` blocks or other built-in like ```sum()```, python will call ```iter(obj)```, which will call ```obj.__iter__()```. The ```__iter__()``` method need to return a iterator obj(which implements the ```__next__()``` method(the ```__next__() method need to raise a StopIteration Exception)). The ```for``` loop repeatedly calls the ```next()``` function until it's exhausted (and raises a StopIteration exception).

    - A generator function/exp is always a "generator"; A geneartor is always a "Iterator". "Iterator" contains the ```__next__()``` method. Container is usually "Iterable", calling ```iter()``` on a iterable obj will return an iterator (in general). An Iterable obj is not always an iterator, but could become an iterator.
    - An iterable object must implement ```__iter__()``` method, which returns a iterator in general.
    - To make an iterable obj an Iterator:
        - implement ```__iter__()```            :1. return self; 2. maintain a flag/count.
        - implement ```__next__()```            :1. return value based on flag/count; 2. reset flag & raise StopIteration.


- Item18: Reduce Visual Noise with Variable Positional Arguments
    - Replace the last arguments with ```*args``` to improve readability on caller side.
        - e.g. : ```def func(var_a, *values)```;        caller: ```func(var_a, 1,2,3,4,5)```.

    - Cons:
        1. Have to change all caller function when need to add a new argument.
        2. Buggy: if caller want to pass a iterable obj, need to unpack the variable first with ```*var```.
        3. Since positional argument is always a tuple, could consume lots of memory.


- Item19: Provide Optional Behavior with Keyword Arguments
    - Usage: Positional arguments must be specified before keyword arguments.

    - Benefit:
        1. Keyword arguments make the function call clearer to reader of the code.
            - e.g. ```func(first_arg=arg1, ...)```
        2. Provide default and additional operations based on different type/value of the keyword argument.

    - Always pass optional arguments using the keyword names and never pass them as positional arguments.

- Item20: Use "None" and Docstrings to Specify Dynamic default arguments
    - Default arguments are evaluated **Only Once** per module load(or when the function is defined).
        - Could cause odd behaviors for dynamic values.
        - Explains why ```def func(some_arg=[])``` may cause unexpected results.
        - So avoid placing mutable obj in the function arguments.

    - Use ```None``` as a placeholder to the keyword arguments and use ```default_behavior if arg is None else behavior``` to choose between default/indicated behavior.

    - Use "None" as the default value for arguments that have **dynamic value(changes through time/event)**, and document the actual behavior in the docstring.


- **Item21: Enforce Clarity with Keyword-Only Arguments(!)**
    - When functions are complex, it's better to require that callers are clear about their intentions by making functions accept **keyword-only arguments**, which can only be supplied by keyword, never by positional argument.
        - Syntax: ```def func(arg1, arg2, *, kw1, kw2)```
        - By doing so, user can only call this function using ```func(arg1, arg2, kw1=v1, kw2=v2)```, never by ```func(arg1, arg2, kw1, kw2)```.

    - Use keyword-only arguments to force callers to supply keyword arguments for potentially confusing functions, especially those that accept multiple Boolean flags.

## Chapter3: Classes and Inheritance
- Item22: Prefer Helper classes over bookkeeping with dictionaries and tuples
    - Dictionaries are so easy to use that there's a danger of overextending them.
    - As soon as the bookkeeping is getting complicated, break it into classes.

    - ```collections.namedtuple(type_name, attrs, ...) -> cls```
        - return a subclass of tuple with attrs.
        - Limitations:
            - You can't specify default argument values for namedtuple cls.
            - The attribute values of namedtuple instances are accessible using indexes/iterations, leading to unintentional usage.

    - Summary:
        - Avoid making dicts with values that are other dicts or long tuples.
        - Use namedtuple for lightweight, immutable data container before you need the flexibility of a full cls.
        - Move your book keeping code to helper clses, when your internal state dicts get complicated.


- Item23: Accept Functions for simple interface instead of cls
    - **You may want to add dynamic behavior to a function(!)**
        - In other language, you may need to define 2 clses and their dependencies.
        - In python, you can directly pass function to the receiver function to achieve polymorphism.
            - ```def func1(hook, ...): if condition {hook()}, ...```
    - Instead of using cls, functions are often all you need for simple interfaces between components.
    - When you need a function to maintain state, consider defining a cls that provides the ```__call__()``` method instead of defining a stateful closure.


- Item24: Use ```@classmethod``` to provide constructor polymorphism
    - Interface in python       : ```def func(): raise NotImplementedError```.

    - Python only supports single constructor per class, the ```__init__()``` method.
    - To provide constructor polymophism (or override the constructor), we need to use ```@classmethod``` keyword.
        - ```@classmethod``` convert a function into class method, which can be called on the class.
            - A decorator function on ```__init__()```.
        - Syntax:   ```@classmethod def func(cls, arg1, arg2, arg3, ...): ... cls(args) ...```
        - Usage :   ```Class.func(args)```


- Item25: Initialize Parent Classes with ```super()```.
    - Python's Method Resolution Order(MRO) solves the problems of superclass initialization order and diamond inheritance problem.
    - **Always use ```super().__init__(args)``` to initialize parent classes.(!)**


- Item26: Use multiple inheritance only for mix-in utility classes
    - Avoid using multiple inheritance if **mix-in** (util) class can achieve the same func.


- Item27: Prefer Public Attributes over Private ones
    - Private fields are specified by prefixing attr's name with 2 underscore.
        - Directly accessing private fields from outside the class will cause an exception.
        - *Subclass can't access its parent class's private fields.*

    - Essentially, what private attr does is translate ```ClassObject.__private_attr``` to ```_ClassObject.private_attr```; Knowing this, we can access any private fields with ```obj._ClassObject__private_field```.
        - Private fields are actually stored in ```obj.__dict__```.
        - Could use *protected field*, by means ```ClassObj._protect_field```

    - Anyway, your potential subclasses will still access the private fields when the absolutely need to, and using private field is easily breakable.

    - In general, it's better to use public & protected attributes; 
    - Only consider using private field to **avoid naming conflict** with subclasses that're out of your control.
        - The only time to seriously consider using private attribute is *when you're worried about naming conflicts with subclasses.* This is a concern with classes that are part of a public API; the subclasses are out of your control, so naming conflict is especially possible. To reduce the risk of this happening, you can use a private attribute in the parent class to ensure that there are no attribute names that overlap with cild classes.


- Item28: Inherit from ```collections.abc``` for custom container types.
    - For classes that inherited from classes in ```collections.abc```, if the custom class doesn't implement some essential method, an error will be raised until all necessary method are implemented.

    - After defining required method by an abstract base class, it will provide all of the additional methods for free, (consider extend from ```collections.abc``` if want to act like a builtin).

    - Inherit directly from Python's container types for simple usage.

    - Beward the number of methods required to implement a custom container type correctly.

    - Have your custom type inherit from the ```collections.abc``` to ensure your classes match required interface and behavior.

## Chapter4: Metaclasses and Attributes
- Item 29: Use Plain Attributes Instead of Get&Set Methods
    - If want to add extra behavior when read/set/del an attribute, you can use ```@property, @attr.setter, @attr.deleter``` to add a decorator onto a function.

    - Can even assign ```@property``` to ```arg``` of ```__init__(self, arg)```: when executing ```self.arg = arg```, ```@arg.setter``` method will be called, immediately running the validation code before **object construction** has completed.
        - Same for init super class.
        - Can also provide read-only attr.

    - Be sure to avoid any other side effects except the specified attribute.


- Item 30: Consider ```@property``` instead of Refactoring Attributes
    - Use ```@property``` to give attributes new functionality.
    - Make incremental progress toward data models by using ```@property```
    - Consider refactoring a class when you find yourself using ```@property``` too heavily.


- Item 31: Use Descriptors for Reusable ```@property``` methods
    - If we have multiple attributes, defining getter, setter for each one of them is dump. Instead, could use ```__get__(*args, **kws), __set__(*args, **kws)``` to define bunch of (get,set) behavior.

    - More specifically, we need to put common code into ```__get__(), __set__()```.
        - e.g.: ```self.attr = ClassWithGetSet()```. If this class attribute is an object that has ```__get__(), __set__()``` method, python will assume you want to follow the descriptor protocol.

    ```py
    exam.math_grade = 50
    # Will be interpreted as Exam.__dict__['writting_grade'].__set__(exam, 40)
    print(exam.writing_grade)
    # Will be interpreted as print(Exam.__dict__['writting_grade'].__get__(exam, Exam))
    ```

    - Syntax:
        - ```def __get__(self, instance, instance_type)```
        - ```def __set__(self, instance, value)```

- Item 32: Use ```__getattr__(), __getattribute__(), __setattr__()``` for Lazy Attributes
    - Plain instance attribute, ```@property``` method, descriptors can't handle dynamic attributes, like database scheme, since they need to be defined in advance.
    - Python relies on the ```hasattr(object, name, value)```, to determine whether attributes exist.
    - And the ```getattr(object, name)``` to access property values.

    - ```__getattr__(object, name)```: Python makes dynamic behavior possible with the ```__getattr__()``` special method. If your class defines ```__getattr__()```, **it will only be called everytime an attribute can't be found** in an ```instance.__dict__```. **(!)**

    - ```__getattribute__(object, name)```: This method is called **everytime an attribute is accessed** on an object, no matter whether it exists in the ```instance.__dict__``` or not. This enables us to do extra operations everytime we access some attributes.
        - In the event that a dynamically accessed property **shouldn't exist**, you can raise an ```AttributeError```.
        - Has **2** ways to avoid infinite recursion

    - ```__setattr__(object, name, value)```    : This method is **always** called everytime an attribute is assigned on an instance, no matter whether the attribute exist or not.
        - Has 3 ways to avoid infinite recursion.
    - ```__delattr__(object, name)```           : Has 3 ways to avoid infinite recursion.

    - When you define ```__getattribute__(), __setattr__()``` method in your class, it may cause infinite loop, since accessing & modifing attributes need to call them. 
        - **To avoid this problem, use ```super().__getattribute__(), super().__setattr__(), super().__delattr__()``` to avoid infinite recursion. (!) **


- Item 33: Validate Subclasses with Metaclasses
    - TODO

## Chapter5: Concurrency and Parallelism

## Chapter6: Bulit-in Modules

## Chapter7: Collaboration

## Chapter8: Production

## MISC
- ```is```, ```not```, ```!=```, ```==```
    - ```is```              :compare ```id(x)```.
    - ```== : obj.__eq__()```
        - for checking whether sth is None, ```is``` will always work; ```==``` could change the result if user override the ```__eq__()``` method.
    - ```!=``` vs ```is not```
        - ```not```         :return ```bool(x)```.
        - ```!=```          :refers to ```__eq__()```, ```__ne__()```, ```__cmp__()``` method.
    - ```is not```          :same as ```is```.

- ```@classmethod``` and ```@staticmethod```
    - ```@classmethod func(cls, args) -> cls object```
        - Could be used to provide constructor polimorphism, and can be inherited by subclasses.
    - ```@staticmethod func(args) -> Any```
        - Basically just a function; Its task is usually logically bound to the class, but doesn't require instantiation.

- **The use of keyword-only arguments:**
    - If the function contains ```*arg```, don't need to use keyword-only argument.
        -  e.g. ```print(*object, sep=' ', ...)```.
    - If the args contains an iterable obj, use keyword-only argument.
        - Try to avoid putting normal positional arg with an iterable arg into the same function.

    - If the function has multiple form, like ```max(iterable), max(arg1, arg2,...)```, then use the keyword-only argument to prevent mis-using.
        - That's why ```max(iterable, *[, key, default])```.

- **The doc-form of optional keyword**
    - If the keyword has a default value, use ```func(arg, kw1=de_value, ...)```.
    - If the keyword doesn't have a default value, use ```func(arg[, kw1, kw2])```

- The best way to join strings:
    - Use ```''.join(sequence)```
