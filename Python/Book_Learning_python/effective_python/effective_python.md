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
    - When need to write a function that process a sequence of data and return a sequence of result, always use Generator instead of returning List.
    - Syntax: ```... yield value```.
    - Beware: generator results can only be iterated once; If need to store the result, store result in list/array first, or use defensive iterating rules.

## Chapter3: Classes and Inheritance

## Chapter4: Metaclasses and Attributes

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
