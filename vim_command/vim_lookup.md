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
- ```[[```        :move to the begining of the file;
- ```]]```        :move to the end of the file.
- ```0```         :move to the begining of the line.
- ```$```       :move to the end of the line.
- ```w```        :move to the begining of next word.
- ```b```        :move to the begining of previous word.
- ```e```        :move to the end of current word.

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

- close split
    - ```:close```

- open another file in the same window
    - ```:split ./filename```

- choose between different window:
    - ```<Ctrl + w> + h,j,k,l```
    - ```<C-w> + w```, cycle between the open windows

- move window
    - ```<c-w> + H,J,K,L```; move current window to ...
    - ```<c-w> + r```; rotate all windows.
    - ```<c-w> + x```; exchange the current window with its neighbor.

# Appendix
- https::www.jianshu.com/p/117253829581
