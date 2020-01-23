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
    - Ph

## Chapter2: Functions

## Chapter3: Classes and Inheritance

## Chapter4: Metaclasses and Attributes

## Chapter5: Concurrency and Parallenlism

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
