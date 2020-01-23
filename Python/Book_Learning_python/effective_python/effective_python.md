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
            - No spaces around (list_index, kw_assignments).
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
