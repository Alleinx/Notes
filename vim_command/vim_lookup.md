#### Gist

- Typing a number with an operator repeats it that many times.
    - ```operator [number] motion```
    
    - Operator: what to do, such as d for delete.

    - [number]: is an optional count to repeat the motion. 

    - Motion: moves over the text to operate on, such as w (word), $ (to the end of line).

    - Typing ```:h [cmd]``` to get the doc for [cmd].


#### General
- undo: ```u```	to undo the last command, ```U``` to undo opeartions on a whole line.

- Redo: ```<CTRL-R>```

- Execute a shell command:
    - ```:[cmd]```	: execute cmd within vim

- blockwise visual mode: ```<C-v>```
    - Select characters blockwise.

- Repeat the last ex-cmd
    ```@:```

- ```<C-o>```       :move cursor back to the previous position.

- ```:e!```         : Discard all buffed changes that haven't been written to file.

- ```<C-g>```       : check file status.

- ```t{char}```     :move cursor 1 char before the next {char}.
    - ```dt{char}```   :delete till the specified character.

- Jump to files under cursor (!)
    - Use ```gf``` cmd to go to file "play.txt" if it exist under path.
        - we can jump forward/backward using ```<C-i>``` and ```<C-o>```.
    - Add expanded-name
        - ```:set suffixesadd+={.name}```
        - Now, we can go to file "play", even we doesn't wirte its expanded name.

- Jump through global mark (!)
    - As mentioned before, we could use ```m{a-z}``` to create a mark inside a file.
        - Use ``` `{mark}``` to jump to {mark}.
    - We could also create a global mark using ```m{A-Z}```.
        - This is useful when we want to find definition in other files; Yes, we can use ```<C-o>``` to jump back; However, when the number of files increase, it takes more effort to get back to the original file; Thus, mark sure to set a "global mark" before using commands that could lead us to other places.

- yank/put into/from system (!)
    - yank into system clickboard       :Use ```"+``` prefix.
    - put from system clickboard        :Use ```"+``` prefix under insert mode.
        - or just use ```<C-p>``` under insert mode.
#### Plugin
- Usage of vim-surround (!)
    - ```cs{old}{new}```                 :change a surrounding.
    - ```ds{target}```                   :delete a surrounding.
    - ```ys{motion}{target}```           :add a surrounding.
        - ```v``` + ```S{target}```      :add a surrounding.
    - ```yS{motion}{target}```           :add a surrounding of {motion} to a new line with indent.


#### File Operation

- Open/create file
    - ```:vim file```
- Close file
    - ```:q```
    - ```:ZZ```
- Open a file in vim
    - ```:open file```
- Switch to next file
    - ```:bn```
- Switch to previouse file
    - ```:bp```

#### Parenthesis pairing
- ```:%```

#### Copy & paste
- copy 
    ```:yy```
- paste
    ```:p``` : paste in current cursor.
    ```:P``` : paste in current line.
- cut & paste
    - ```V``` (whole line),```v```. 
    - ```d```                                 : cut
    - ```p```                                 : paste

#### Insertion
- ```I``` : Insert from the begining of the line.
- ```A``` : Insert from the end of the line.
- ```i``` : Insert at the cursor
- ```a``` : Insert (1) character after the cursor
- ```o``` : Insert a line after current line.
- ```O``` : Insert a line before current line.
- ```<C-o>```: Execute 1 normal mode command, then switch back to insert mode.

#### Search
- ```/text```
    - ```n``` -> find next
    - ```N``` -> find previous

    - Config
        - ```:set ignorecase``` : ignore case.
        - ```:set noignorecase``` : doesn't ignore cse
        - ```:set incsearch``` : search when start input characters, rather than hitting ```<enter>```

#### Replace
- ```r*``` : replace current character(after cursor) to any character (only one); 
- ```:s/old/new/```       : replace the first meet (old) in current line to (new);
- ```:s/old/new/g```      : replace all (old) in current line to (new);
- ```:%s/old/new/```      : replace the first meet (old) in any line of a file to (new);
- ```:%s/old/new/g```     : replace all (old) in the file to (new); 
       
#### Move cursor
- ```[[```            :move to the begining of the file;
- ```]]```            :move to the end of the file.
- ```0```             :move to the begining of the line.
- ```$```             :move to the end of the line.
- ```w```             :move to the begining of next word.
- ```b```             :move to the begining of previous word.
- ```e```             :move to the end of current word.
- ```ge```            :move to the end of previous word.
- ```G```             :move to the end of file.
- ```gg```            :move to the begining of the file.
- ```[i]G```          :move to the ith line of the file.
- ```<C-o>```         :move back to the previous position.
- ```<C-d>```         :...
- ```<C-u>```         :...
- ```<C-e>```         :move downwards.
- ```<C-y>```         :move upwards.

#### Delete
- ```x```         :similar to delete
- ```dd```        :remove current line
- ```D```         :remove from current character to the end of the line.
- ```d + hjkl```. 

-   Remove words
    - ```d + n + w```   :delete next n words.
    - ```dw```   :remove till the begining of next word. 
    - ```de```   :remove till the end of current word.
    - ```db```   :(Delete).
    - ```cw```   :de + i.
    - ```daw```  :delete the word under cursor.

- Delete to the end of the line: ```d$```.

#### Window
- split window
    - ```:split```, vertical split.
    - ```:vsplit```, horizontal split.

    - Use ```<C-w>s``` to split horizontally.
    - Use ```<C-w>v``` to split vertically
        - Then, we could use ```edit {file}``` to override buffer.
        - Or, we could switch buffers using ```:bn, :bp``` if any.

- close split
    - ```close```   : close the activated window.
    - ```only```    : close all other windows rather than the activated window.

- open another file in the same window
    - ```:split ./filename```

- choose between different window:
    - ```<Ctrl + w> + h,j,k,l```
    - ```<C-w> + w```, cycle between the open windows

- move window
    - ```<c-w> + H,J,K,L```; move current window to ...
    - ```<c-w> + r```; rotate all windows.
    - ```<c-w> + x```; exchange the current window with its neighbor.

- Resize window
    - ```<C-w><, <C-w>>```: resize the window horizontally.
    - ```<C-w>+, <C-w>-```: resize the window vertically.
    - ```: res[ize] [+,-] [number]``` : use command to resize.
    - ```: vertical res[ize] [+,-] [number]``` : use command to resize.
    - ```<C-w>=```        : resize the window to be equal.

#### Plugins:
- netrw
    - ```d```       : Make a directory
    - ```D```       : Delete a directory/file.
    - Just do ```:h netrw-quickmap```

# Appendix
- https::www.jianshu.com/p/117253829581
