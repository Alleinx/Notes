# Practical Vim

## Structure:
- Chapter
    - Techniques

## Chapter1
- T1: The ```.``` command:
	- ```.``` command can repeat the last operation.
		- Includes commands in normal mode; Inserted character; etc.

	- ```.``` is actually a macro, which could execute pre-defined operation in sequence.

- T2: Use ```.``` to reduce duplicated operation (!)
    - Composed keys:
        - ```C == c$```
            - ```c$``` : delete the rest of the line and enter insert mode.
            - ```c``` [motion]: delete + enter insert mode. (!)
        - ```s == cl```
            - delete the next character and enter insert mode.
        - ```S == ^C``` (!)
            - **delete the whole line and enter insert mode.**
            - ```^``` : move cursor to the first non-empty character of the line.
            - ```0``` : move cursor to the first character of the line.
            - ```$``` : move cursor to the last character of the line.
        - ```I == ^i```
            - Enter insert mode at the begining of the statement.
        - ```A == $a```
            - Append at the end of the sentence.
        - ```o```
            - Insert a line below.
        - ```O```
            - Insert a line Above.

- T3: Find: ```f{char}```
    - ```f{char}```: find the next {char} and place cursor on it.
        - use ```;``` to move to the next matched {char}.
        - use ```,``` to move to the previous matched {char}.

- T4: Undo 
    - different motion has different undo keywords.
    - ```u``` is the mostly used undo operand.

- T5: search/replace
    - ```/keywords```
        - Search keywords globally.
        - Use ```n/N``` to select next/previous matched word.
    - ```:noh```
        - Turn off highlight after search.
    - ```:%s/target/to/g```
        - Replace all {target} within the text with {to}.
    - ```cw.```
        - ```cw``` : change a word and enter insertion mode; Recognized as 1 operation/macro.
        - ```.``` : use ```.``` to repeat.

- T6 : pattern of ```.```
    - Ideal situation: move-key + ```.```
        - use move-key to move and use ```.``` to repeat operation.
    - Think how to convert duplicated operations into the ideal pattern. 

## Chapter 2
- T7 : Switch to normal mode when not typing.

- T8 : Control the size of undo operation
    - ```i {insert some text}``` <Esc> : is a modification.
        - we can control the size of each undo operation by inserting <Esc> at the place we need.
        - Since undo operation will undo the "last operation".

- T9 : ```.``` the duplicated modification.
    - ```dl```:
        - delete a letter.
    - ```daw```:
        - delete a word.
    - ```das``` or ```S```:
        - delete a sentence.
    - ```dap```:
        - delete a paragraph.
    - Since ```l, aw, as, ap``` is a [motion], d[motion] is considered as a single operation; So ```daw/s/p``` is ideal when using ```.``` operation.

- T10 : Modify Numbers:
    - ```[count]<ctrl-a>```
        - Add the number under cursor by [count].
    - ```[count]<ctrl-x>```
        - Subtract the number under cursor by [count].
    - If the cursor is not on a number, execute these commands will modify the first number in current line.

- T11 : Repeat > [count]
    - Use [count] if necessary:
        - if use ```[operator][count][motion]```, then undo will undo the whole modification.
        - In contrast, use ```.``` could provide better flexibility.
        - ```c3w``` or ```dw..i```: depends.

- T12 : Operator + [count] + [motion] = Operation
    - Operator defines which operation to take; 
        - ```c```: change
        - ```d```: delete
        - ```gu```: make lowercase
        - ```gU```: make uppercase
        - ```g~```: reverse the case.
        - ```\>```: shift right
        - ```<```: shift left
        - ```:h``` operator to see more operators.
        - ```[count]J```: join the following [count] lines.

    - [count] defines how many time the operation will be executed.

    - The scope of operation is determined by motion; (e.g. ```dw, daw, dl, dap```).

    - Combine operator and motion. (!)
    - **When a operator is called twice, then it will perform on current line.**
        - e.g.``` cc = S = ddi```   //delete the whole line and enter insert mode.
        - ```gUU = gUgU```    //make the line uppercase.
        - ```gugu = guu``` make the line lowercase.

## Chapter3

- T13 : Insertion mode
    - deletion under insert mode:
        - ```<C-h>``` = backspace.
        - ```<C-w>``` = delete previous word. (!)
        - ```<C-u>``` = delete until the begining of the line. (!)

- T14 : Back to general mode
    - ```<Esc>```
    - ```<C-[>```
    - ```<C-c>```

- T15/16 Register, [skip]

- T17 Insert not commonly used character
    - ```<C-v>u{code}```
        - If we know the unicode of a character, we can insert the character by ```<C-v>u{unicode}```.

- T18 Insert not commonly used character with digraphs, [skip]

- T19 Replace mode
    - use ```R``` to enter replace mode.
    - use ```r``` to replace a single character.

## Chapter4
- T20 Visual Mode
    - ```<C-g>```
        - Switch between "visual mode" and "select mode"
        - In select mode, input will replace selected area; In visual mode, input will not change selected area by default, we can press ```c``` to achieve the same effect as select mode.

- T21 Selection under visual mode
    - ```v```: select a character at a time.
    - ```V```: select a line at a time.
    - ```<C-v>```: select a block at a time (!).
        - When want to select a character vertically.
    - ```gv```: select previous selected area. 

    - Change the selective side (!):
        - ```o``` will change the moving direction of visual mode. In this way, we can easily change the selected area.

- T22 Repeat Visual cmd using ```.```
- T23 Use operator rather than visual mode if possible.
    - By doing so, we could better utilize the power of ```.``` operator.

    - For one-time operations; and text areas that are hard to be described using cmd, it's convenient to use visual mode.

    - ```U``` could convert selected text into upper case under visual mode.

    - ```vit```: select text between a Tag; Then press ```U``` to convert them into upper case. However, using ```.``` to repeat this operation will modify the same # of characters as the first selected item.

    - ```gUit```: This could solve the problem that ```vit-U``` has.

- T24 Select text blocks vertically:
    - ```<C-v>```
        - Enter blockwise visual mode.

- T25 modify vertical texts:
    - ```<C-v>``` -> select vertical text areas that want to modify at the same time -> ```c``` -> input modified contents -> ```<Esc>``` -> done.
    - ```<C-v>``` -> select text -> operator -> modify -> back to normal mode and done.

- T26 Append Text after text-areas with different length:
    - could use ```A{text}``` and key + ```.``` operation.
    - could also ```<C-v>$A``` and key + ```{text}``` to add text (!).

    - ```i/I``` and ```a/A```:
        - When using ```<C-v>```, ```i/a``` are treated as a component of a text object, instead of entering the insert mode; ```I/A``` will enter insert mode at the begining/end of the "selected area", instead of the "whole line".

## Chapter5
- T27 Command-line mode in Vim
    - press ```:```, and vim will enter command-line mode; cmds within command-line mode is called "ex-cmd".
    - ```[range] delete [x]```
        - delete lines within range to register [x].
    - ```[range] yank [x]```
        - copy lines within range to register [x].
    - ```[line] put [x]```
        - paste contents in [x] after [line]
    - ```[range] copy {address}```
        - copy lines within range after address line.
    - ```[range] move {address}```
        - move lines within range after address line.
    - ```[range] join```
        - join lines within range. 
    - ```[range] substitute/{pattern}/{string}/[flags]```
        - replace {pattern} within range to {string}.
    - ```%s/{pattern}/{string}```
        - replace {pattern} globally to {string}.
