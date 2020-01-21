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
        - ```c```       : change
        - ```d```       : delete
        - ```gu```      : make lowercase
        - ```gU```      : make uppercase
        - ```~```       : reverse the case.
        - ```g~```      : reverse the case.
        - ```\>```      : shift right
        - ```<```       : shift left
        - ```:h```      : operator to see more operators.
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
        - could also use ```r``` to replace selected character.
 
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
            - Use ```{start},{end}bd``` to delect buffer in range.
    - ```:bs{#buffer}```        :split {buffer} into a new window.


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
    - Alter Windows:
        - ```<C-w>{HL}  : move current window left/right(switch to vertical split).
        - ```<C-w>{JK}  : move current window down/up(switch to horizontal split).

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
    - ```edit %:h```            : % will be the path of file in activated buffer.
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
    - Use ```o``` to open file in a new window; Use ```<CR>``` to open file in current window (default).

- T44: Save file into not-existed dir
    - when we try to save file into a not existed dir, an error will occur.
    - We could use ```:!mkdir -p %h``` to create the target dir first, then save the file into it.
        - ```%``` is the path of file in activated buffer. 

- T45: Save file as super-user, [skip]

## Chapter8
- T46: place your finger in the right place.

- T47: distinguish "actual line" and "screen line"
    - ```g + {move_keys}``` to move between "screen line"
        - e.g. ```g0```, ```g + hjkl```, ```g$```, ```g^```.

- T48: move based on word/WORD (!)
    - distinguish "word" and "WORD"
        - word: {character, number, _, non-empty character}, seperated using empty-character.
        - WORD: {character}, seperated using empty-character.
        - use ```w, b, e, ge``` to jump between word; use ```W, B, E, gE``` to jump between WORD.
    - ```ge```      :move to the end of last previous word.
    - ```ea```      :add to the end of the word.
    - ```w, e, b``` :...

- T49: search/move based on character
    - ```f{char}```
    - use ```;``` and ```,``` to choose forward and backward.
    - ```t{char}```     :move cursor 1 char before the next {char} (!).
        - ```dt{char}```   :delete till the specified character.
    - when moving, better use ```f{char}```; when modifying(d, c), better use ```dt{char}/ct{char}``` (!).

- T50: moving with search
    - visual mode with search;
    - delete with search;
    - move with search;

- T51: select text inside tags
    - vim can select text inside some tags (<, {, (, ', ", [).
        - cursor must be placed inside the tags.

    - operator {a;i}
        - a: text and(with) the tag.
        - i: text within the tag.

    - e.g.:
        - ```vi{tag}```      :select text inside the tag. (e.g. <Text>, press ```vi<``` will select Text).
        - ```va{tag}```      :select text inside the tag with tag. (e.g. <Text>, press ```va<``` will select <Text>).
        - ```ci{tag}``` 
        - ```di{tag}``` 

    - lookup table:
        - ```a)``` or ```a(```       :select text with parentheses.
        - ```i)``` or ```i(```       :select text inside parentheses.
        - ```a}``` or ```a{```       :select text with braces.
        - ```i}``` or ```i{```       :select text inside braces.
        - ```a] or a[; i] or i[```   :select ... brackets.
        - ```a> or a<; i> or i<```   :select ... angle brackets.
        - ```a' or a'; i' or i'```   :select ... single quotes.
        - ```a" or a"; i" or i"```   :select ... double quotes.
        - ```a` or a`; i` or i` ```  :select ... backticks.
        - ```at or at; it or it ```  :select ... tags.

- T52: more deletion
    - lookup table
        - ```iw```      :current word.
        - ```aw```      :current word + "space". 
            - ```dw``` == ```daw```
            - ```cw``` == ```ciw```
        - ```iW```      :current WORD.
        - ```aW```      :current WORD + "space".
        - ```is```      :current sentence.
        - ```as```      :current sentence + "space". 
        - ```ip```      :current paragraph.
        - ```ap```      :current paragraph. + "space". 

    - In general, better use ```as, aw, ap``` with ```d{motion}```; and use ```iw, is, ip``` with ```c{motion}```.

- T53: set mark to jump back quickly (!)
    - ```m{a-zA-Z}```   will set a mark at current position of cursor with {a-zA-Z}.
    - ``` '{mark}```    will jump to the line marked with {mark}.
        - Could also use ```<C-o>```.
        - use ```mm``` and ``` `m``` to mark a mark and jump back.

- T54: jump between parentheses
    - ```%```       :jump between pair of parentheses (e.g. (),{,[])

- Usage of vim-surround (!)
    - ```cs{old}{new}```                 :change a surrounding.
    - ```ds{target}```                   :delete a surrounding.
    - ```ys{motion}{target}```           :add a surrounding.
        - ```v``` + ```S{target}```      :add a surrounding.
    - ```yS{motion}{target}```           :add a surrounding of {motion} to a new line with indent.

## Chapter9
- T55: walk through jump-through list
    - Use ```:jumps``` to view the jump-through list.
        - jump      :index.
        - line/col  :cursor position.
        - file/text :which file.

    - Move around:
        - ```<C-o>```        :go backward.
        - ```<C-i>```        :go forward.

- T56: walk through change list
    - Use ```:changes``` to view the change list.
    
    - Move around:
        - ```g;```          :move cursor to the position of "previous" change;
        - ```g,```          :move cursor to the position of "next" change;

- T57: Jump to files under cursor (!)
    - Use ```gf``` cmd to go to file "play.txt" if it exist under path.
        - we can jump forward/backward using ```<C-i>``` and ```<C-o>```.

    - Add expanded-name
        - ```:set suffixesadd+={.name}```
        - Now, we can go to file "play", even we doesn't wirte its expanded name.

- T58: Jump through global mark (!)
    - As mentioned before, we could use ```m{a-z}``` to create a mark inside a file.
        - Use ``` `{mark}``` to jump to {mark}.

    - We could also create a global mark using ```m{A-Z}```.
        - This is useful when we want to find definition in other files; Yes, we can use ```<C-o>``` to jump back; However, when the number of files increase, it takes more effort to get back to the original file; Thus, mark sure to set a "global mark" before using commands that could lead us to other places.

## Chapter10
- T59: delete/copy/paste using "nameless register".
    - ```y{motion}```       : yank {motion} into nameless register. 

- T60: deep into vim register
    - Yank/put into/from system (!)
        - yank into system clipboard       :Use ```"+``` prefix.
        - put from system clipboard        :Use ```"+``` prefix under insert mode.
            - or just use ```<C-p>``` under insert mode.
    - Delete/yank/put in vim will use one of the registers; we could add ```"{register}``` prefix to indicate which register to use; If not indicate, vim will use the "nameless register" by default.
    - The blackhole register :operations after ```"_``` prefix will not be stored to nameless register (!).
        - i.e. we could use ```"_dd``` to delete a line while not mess up the nameless register.
    - Named register
        - vim provide 26 named register: {a-z}; we could use ```_{a-z}``` prefix to indicate which named register to use.

- T61: replace register content with selected area
    - when we replace content of selected area with content inside the register, content of selected area will be written into the register.
        - This design makes it easy to switch 2 selected areas (!).

- T62: put out content inside a register
    - ```p```       :paste content after the cursor.
    - ```P```       :paste content before the cursor.
    - Could also use ```<C-r>{register}``` to put in insert mode (!).
        - use "" to reference nameless register in normal mode, " in insert mode.
        - use ```y{motion}``` to yank, and ```ciw``` to clear; finally, use ```<C-R>0``` to put.

- T63: interact with system clipboard
    - "autoindent" arg could mess up the indentation.
    - To prevent this issue, always use ```"+p``` or ```<C-r>+``` to put content in system clipboard into vim (!).

## Chapter11
- T64: Macro (!)
    - macro is a series of commands.
    - record a macro:
        - start recording: ```q{register}```
        - input cmds.
        - end recording: ```q```, the macro will be stored in {register}.
    - play a macro:
        - ```[count]@{register}```; After the first use, we could use ```@@``` to repeat.
    - Better define a macro in parallel.

- T65: cursor movement when using a macro.
    - Principle: make sure every cmd could be executed repeatedly when defining a macro.
        - ```w, b, e, ge``` is better than ```hjkl```; make sure cursor will be in the right position every time you use a macro when define it;
    - when one of the motions failed, the macro will stop executing.
        - for macros contain "move to next matched obj", we could set [count] to a very large number and the macro will automatically stops when the motions fail (!).

- T66: ```[count]@{register}``` (!)
    - Use simple recorded macro and use ```[count] @{register}``` to repeat it(like the use of ```.```).

- T67: Repeat modification on continuous lines (!)
    - ```[count]@{register}```                  :execute a macro in series.
        - if one of the macro failed, the rest will stop executing.
    - ```:{selected area}normal @{register}```  :execute a macro in parallel
        - all of the macros will be executed even if some failed.

    - parallel execution is more robust; serial execution is more convenient and can help us locate problems during execution.

- T68: append new cmds to recorded macro
    - use ```q{A-Z}``` to append contents onto previous macro, so we don't need to record the whole macro again.

- T69: execute macro in multiple files, [skip]

- T70: iterate index 
    - define and increase a var:
        - ```:let i=0```                           :define a variable i.
        - ```<C-r>=i```                            :insert the value of i(under insert mode).
        - ```:let i+=1```                          :increase i by 1.
    - macro:
        - ```qa0<C-r>=i<CR> )<Esc>:let i+=1<CR>q```: this macro will increase the number of i as iteration.
        - finally, use parallel execution to execute the macro.

- T71: modify a record macro (!)
    - Use ```:reg {a-z}``` to view the content of a macro.
    - Since macros are stored in register, we can put the content of register to current window and modify it. Finally, we could yank the content back to update the macro.

    - modify a macro (!):
        - ```"{register}p```
        - modify
    - save a macro (!):
        - ```"{register}y{motion}```

## Chapter12
- T72: search mode and case sensitiveness
    - Turn on both ignorecase and smartcase.
    - After turning on smartcase, if one of the letter in searching pattern is uppercase, the ignorecase will automatically be ignored.

- T73: ```\v``` switch when using regex, [skip]
- T74: searching using ```\V```
    - If want to search using regex, use ```/\v{pattern}``` (magic mode).
    - If want to search string without ESC, use ```/\V{pattern}``` (nomagic mode).

- T75: ues () to pair sub-matches, [skip]
- T76: search a pattern accurately
    - If we want to search the word "the", when we input '/the', there may be lots of other matches excepts the word "the"; 
    - we could use '''/\v<pattern>``` to specifically search the pattern "<pattern>" (!).

- T77: define the search boarder, [skip]
- T78: Escape character
    - Use ```\V``` to turn off escape mode during searching.
    - The rest are [skiped].

## Chapter13
- T79: search cmd
    - ```/{pattern}```      :forward searching.
    - ```?{pattern}```      :backward searching.
    - Use ```n/N```         :go next/previous match item depends on searching direction.

- T80: highlight matched items, [skip]

- T81: "incsearch":
    - Use ```<C-r><C-w>``` to auto-complete the rest of a matched pattern.

- T82: count the number of total matched item.
    - ```%s///gn```         :count the number of total matches.
        - ```n``` will stop the substitude operation and count the number of matches.

- T83: move cursor to the end of matched pattern
    - ```/{pattern}/e```    :automatically place cursor at the end of each matched pattern.

- T84: operate on complete matches, [skip]

- T85: utilize search history (!)
    - use ```q/``` to open search history buffer. We could modify the content in it and press ```<CR>``` on a modified pattern to perform search.

- T86: use ```*``` to search word under cursor
    - ```*``` will search word under cursor.

## Chapter14
- T87: ```substitute``` command.
    - 
