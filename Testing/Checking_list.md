## This is a checking list for possible bugs in programs.
#### Note: 
    1. Checking list should focus on possible bugs, not coding style.
    2. During checking process, everyone involved should be impartial and make judgement on program instead of programmer.
        2.1 Focus on program, not programmer.
        2.2 When bugs come out, don't blame on programmer, 
            but treat bugs as commmon mistakes so that 
            they could be considered to be added to the checking list later.
    3. All programs contain bugs, if your program passes all checking cases, it doesn't imply your program is perfect, instead, it means this checking list didn't provide you any help(This test is unsuccessful). 
    4. Based on your progress and ddl, make decisions on whether put more efforts into testing or not.

#### 1.Data reference error
    1.1 Uninitialized variable?
        1.1.1 For each reference(variable, array element, instance variable in an object),
        attempt to 'prove' informally that the item has a value at that point.

    1.2 Does index out of array boundary?
    
    1.3 Does each array index have an integer value? 

    1.4 For all references through pointer or reference variables,
    is the referenced memory currently allocated?
        1.4.1 attempt to 'prove' informally that in each reference using a pointer variable, the reference
        memory exists.
    
    1.5 If a data structure is referenced in multiple procedures, is the structure
    defined identically(exactly same) in each procedure?

    1.6 When indexing an array, is off-by-one error exists?
        1.6.1 Exceed the boundary by 1 (Also take care whether the index never reaches the last elements of array).

    1.7 For OO language, are all inheritance requirements met in the implementing class?

#### 2.Data declaration error
    2.1 Have all variables been explicitly and properly declared?
        2.1.1 Variable declaration: int x; float y[];
    
    2.2 Is each variable assigned the correct length and datatype?
        2.2.1 e.g. overflow?
    
    2.3 Are there any variables with similar names? This is not 
    necessarily an error, but it should be seen as a warning that 
    the names may have been confused somwhere within the program.

#### 3.Computation error
    3.1 Are there any mixed-mode computations? 
        3.1.1 e.g. (float)a + (int)b; Such occurrences are not necessarily errors, but they should be explored carefully to ensure that the language's conversion rules are understood.
    
    3.2 Are there any computations using variables having the same datatype but different
    lengths?
        3.2.1 (e.g.): short a = (int)c + (int)b;
    
    3.3 Is the datatype of the target variable of an assignment smaller than the datatype or 
    result of the right-hand expression? 
        3.3.1 reference 3.2.
    
    3.4 Is an overflow or underflow expression possible during the computation of an expression?
    
    3.5 Is it possible for the denominator in a division operation to be 0?

    3.6 Can the value of a variable go outside the meaningful range?
        3.6.1 (e.g.) probability > 1;
    
    3.7 For expressions containing more than one operator, checking the priority of arithmetical operators.

    3.8 Are there any invalid use of integer arithmetic, particularly divisions?
        3.8.1 (e.g.) the result of 2 * i / 2 == i depends on whether
        1. i has an odd or an even value
        2. whether the multiplication or division is performed first.
        
### Inspection Error Checklist Summary

* Data Reference
  * Uninitialized variable used?
  * Subscripts within bounds?
  * Non integer subscripts?
  * Off-by-one errors in subscripts?
  * Are inheritance requirements met?

* Computation
  * Computations on nonarithmetic variables?
  * Mixed-mode computations(May generate unexpected result)?
  * Are the types consistant between LHS and RHS of the computation?
  * Overflow/underflow?
  * Division by 0?
  * Base-2 inaccuracies?
  * Variable's value outside of meaningful range(e.g. prob should lies in [0,1])?
  * Operator precedence.

* Comparison
  * Comparisons between inconsistant variables?
  * Operator precedence.
  * Compiler evaluation of Boolean Expressions understood?
  
* I/O
  * OPEN statement correct?
  * Buffer size matches record size?
  * Files opened before use?
  * Files closed after use?
  * I/O Errors handled?