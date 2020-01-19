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

## Chapter2
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

- T28 Execute cmds on multiple lines
    - ```:{start}, {end}[ex-cmds]```
        - {start}, {end} are addresses; line number is one of the addresses.
        - ```{/some_pattern}, {/end_pattern}``` could also be address, i.e. could use search pattern as the address.
        - address could also be selected regions; use visual mode to select some text and then enter the cmd command-line mode to conduct operations using cmds.

    - [ex-cmds] could also be cmds in normal mode.
        - e.g. ```:3d``` means delete the 3rd line.

    - ```:{line}```
        - Jump to line.    

    - Address lookup table (!):
        - ```.``` represent the address for current line.
        - ```$``` represent the address for the last line in the doc.
        - ```%``` represent all the lines in the doc.
            - ```:%s``` == ```:%substitute```
        - ```0``` represent the 0th line of the file; useful when want the last address to be the begining of the file. e.g. ```x copy 0```: copy xth line to the begining of the file.

- T29: use ':t' and ':m' to copy and move lines
    - ```t``` is the short version of ex-cmd ```copy```.
        - E.g.: 
            - ```:6 t .``` copy 6th line after the current line.
            - ```:. t 6``` copy current line after the 6th line.
            - ```. t .``` == ```yyp```
            - ```. t $``` copy current line after the last line.
            - ```'<, '> t0``` copy select lines to the begining of the file.

    - ```m``` is the short version of ex-cmd ```move```.

- T30: execute normal mode cmds on selected area (!)
    - ```'<,'> normal [cmd]```
        - e.g. If we want to do "repeat" operation on selected lines, we could use ```'<,'> normal .```, instead of ```j + .``` for many times. 
        - ```%normal A;``` to add ; for all the lines in the doc.
            - Or use ```<C-v>[count]j$A;```

- T31: repeat the last ex-cmd
    - Use ```.``` to repeat last normal cmd.
    - Use ```@:``` to repeat last ex-cmd.
        - If want to repeat a ex-cmd multiple times, use ```@@``` after the first ```@:```.

- T32: auto-completion for ex-cmd
    - Use ```<Tab>, <S-Tab>``` to iterate/reverse iterate the completion list. 
    - Use ```<C-d>``` to list all items in the completion list (!).
        - e.g ```cop<C-d>``` will list all item in completion list for "cop".

- T33: Insert copied word into cmd-line mode: [skip]
- T34: Trace history
    - Press ```<Up>, <Down>``` in cmd-line mode to trace historical ex-cmds.
    - vim will also preserve history for "Search mode".

- T35: Shell cmd (!)
    - Use ```:![shell-cmd]``` to execute a shell cmd.
        - ```:ls``` invokes the built-in cmd of vim.
        - ```:!ls``` invokes the shell cmd.

    - If want to execute multiple shell cmds:
        - 1st way:
            - Use ```:shell``` to create a shell;
            - After using, input exit to back into vim;
        - 2nd way:
            - Use ```Ctrl-z``` to hang up vim process.
            - Use ```fg``` to get back into vim.

    - Lookup table (!)
        - ```:shell```                  : launch a shell (type exit to return to vim).
        - ```!{cmd}```                  : execute {cmd} in shell.
        - ```read !{cmd}```             : execute {cmd} in shell and insert result after cursor in vim.
        - ```[range]write !{cmd}```     : execute {cmd} in shell with input in [range].
        - ```[range]!{filter}```        : execute {filter} with input in [range].

## Chapter6
- T36: manage files
    - Changes will be temporarily stored in vim buffer, and write to file when save those changes. 
    - Use ```:ls``` to list items in buffer.
    - Open multiple docs using ```vim files```, files will be stored in buffer; Use ```:bnext``` and ```:bprevious``` to switch between files; Could also use ```<C-^>``` to switch files in buffer.
        - ```:bp``` == ```:bprevious```, ```:bn``` == ```:bnext``` (!).
        - Use ```:bd {buffer_index}``` to delete/close specific buffer (!).
            - Use ```:.bd``` to delete/close activated buffer (!).


- T37: Group buffer using args
    - Use ```args {files}``` to add files into buffer inside vim. Then, we can use ```:bn``` and ```:bp``` to switch files.
    - Use ```:w``` to write changes to file; Use ```:e!``` to discard all changes that haven't been saved to file.
    - Use ```:wa!``` to write all changes to files.

- T38: manage hidden buffer
    - Vim will not allow user to switch to another buffer if there are changes haven't been saved in current buffer, unless we use ```!```; After adding ```!``` to the end of ex-cmd, current buffer will become a "hidden buffer", and we can make changes in other buffer as normal; When we want to close all windows, vim will remind us to "save/discard" changes in all hidden buffer if existed. 

- T39: divide workspace into several windows
    - Split window:
        - Use ```<C-w>s``` to split horizontally.
        - Use ```<C-w>v``` to split vertically
            - Then, we could use ```edit {file}``` to override buffer.
            - Or, we could switch buffers using ```:bn, :bp``` if any.
        - ```:split```, vertical split.
        - ```:vsplit```, horizontal split.
    - Switch between windows:
        - ```<C-w> + hjkl```
        - ```<C-w> + w``` or ```<C-w><C-w>```
    - Close windows:
        - ```close```   : close the activated window.
        - ```only```    : close all other windows rather than the activated window.

- T40: Using tabpage in vim
    - In vim, tabpage is a container contains several windows.
        - I.e. Each tabpage contains several windows; different tabs could have different windows.
        - Tabpage is useful when we need to work on sth else but don't want mess up current windows alignment.

    - Open/close tabpage
        - ```tabe {filename}``` : create a new tabpage.
            - if {filename} is not provided, will create a new tabpage with empty buffer.
        - Use ```<C-w>T``` to move current window into a new tabpage.
        - ```tabclose```        : close current tab.
        - ```close```           : close the tabpage if there's only 1 window in it.
        - ```tabonly```         : close other tabs.

    - Switch between tabpages:
        - ```{N}gt```           : go to {N}th tabpage; {N} start from 1.
        - ```gt```              : go to next tabpage.
        - ```gT```              : go to previous tabpage.
    - Re-arrange tabpages:
        - ```:tabmove [N]```    : move current tabpage into [N]th place.

## Chapter7
- T41: using ```:edit``` to open files
    - ```edit {file}``` or ```e {file}``` (!).
    - ```edit %:h```            : % will be the path of file in activated buffer
    - Add a config to .vimrc file; now, we can use ```%%``` to show the path of the file in activated buffer.

- T42: use ```:find``` to open files
    - ```:find``` allow us to open a file using filename without input the complete filepath.
        - Need to set path first: use ```:set path+={path/**}``` to add a new path.

- T43: use "netrw" to manage file system.
    - Use ```e{dir}``` to open the file system management window of {dir}.
        - ```:e.``` opens the Fs of current dir(dir of activated buffer).
        - Or use ```:E``` to achieve the same effect.
    - Use ```Vexplore``` to open the file system in a vertical window (!).
        - Or use ```:Vex``` for short cut.
    - Use ```Sexplore``` to open the file system in a horizontal window (!).
        - Or use ```:Sex``` for short cut.
    - Use ```<C-^>``` to switch between file system management window and workplace.
