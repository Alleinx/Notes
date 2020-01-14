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
            - delete the next character.
        - S == ^C (!)
            - **delete the whole line.**
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
- T7: PH
