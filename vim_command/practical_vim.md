# Practical Vim

## Structure:
- Chapter
    - Techniques

## Chapter1
- T1: The . command:
	- . command can repeat the last operation.
		- Includes commands in normal mode; Inserted character; etc.

	- . is actually a macro, which could execute pre-defined operation in sequence.

- T2: Use . to reduce duplicated operation (!)
    - Composed keys:
        - C == c$
            - c$ : delete the rest of the line and enter insert mode.
            - c [motion]: delete + enter insert mode. (!)
        - s == cl
            - delete the next character and enter insert mode.
        - S == ^C (!)
            - **delete the whole line and enter insert mode.**
            - ^ : move cursor to the first non-empty character of the line.
            - 0 : move cursor to the first character of the line.
            - $ : move cursor to the last character of the line.
        - I == ^i
            - Enter insert mode at the begining of the statement.
        - A == $a
            - Append at the end of the sentence.
        - o
            - Insert a line below.
        - O
            - Insert a line Above.

- T3: Find: f{char}
    - f{char}: find the next {char} and place cursor on it.
        - use ; to move to the next matched {char}.
        - use , to move to the previous matched {char}.

- T4: Undo 
    - different motion has different undo keywords.
    - u is the mostly used undo operand.

- T5: search/replace
    - /keywords 
        - Search keywords globally.
        - Use n/N to select next/previous matched word.
    - :noh
        - Turn off highlight after search.
    - :%s/target/to/g
        - Replace all {target} within the text with {to}.
    - cw.
        - cw : clear a word and enter insertion mode; Recognized as 1 operation/macro.
        - . : use . to repeat.

- T6 : pattern of .
    - Ideal situation: move-key + .
        - use move-key to move and use . to repeat operation.
    - Think how to convert duplicated operations into the ideal pattern. 

## Chapter 2
- T7 : switch to normal mode.

- T8 : control the size of undo operation
    - i {insert some text} <Esc> : is a modification.
        - we can control the size of each undo operation by inserting <Esc> at the place we need.
        - Since undo operation will undo the "last operation".

- T9 : . the duplicated modification.
    - dl:
        - delete a letter.
    - daw:
        - delete a word.
    - das or S:
        - delete a sentence.
    - dap:
        - delete a paragraph.
    - Since l, aw, as, ap is a [motion], d[motion] is considered as a single operation; So daw/s/p is ideal when using . operation.

- T10 : Modify Numbers:
    - [count]<ctrl-a>
        - Add the number under cursor by [count].
    - [count]<ctrl-x>
        - Subtract the number under cursor by [count].
    - If the cursor is not on a number, execute these commands will modify the first number in current line.

- T11 : Repeat > [count]
    - Use [count] if necessary:
        - if use [operator][count][motion], then undo will undo the whole modification.
        - In contrast, use . could provide better flexibility.
        - c3w or dw..i: depends.

- T12 : Operator + [count] + [motion] = Operation
    - Operator defines which operation to take; 
        - c: change
        - d: delete
        - gu: make lowercase
        - gU: make uppercase
        - g~: reverse the case.
        - \>: shift right
        - <: shift left
        - :h operator to see more operators.

    - [count] defines how many time the operation will be executed.

    - The scope of operation is determined by motion; (e.g. dw, daw, dl, dap).

    - Combine operator and motion. (!)
    - **When a operator is called twice, then it will perform on current line.**
        - e.g. cc = S = ddi   //delete the whole line and enter insert mode.
        - gUU = gUgU    //make the line uppercase.
        - gugu = guu make the line lowercase.
