#### Gist
	- **Typing a number with an operator repeats it that many times.**
		- operator [number] motion
		- operator: what to do, such as d for delete.
		- [number]: is an optional count to repeat the motion. 
		- motion: moves over the text to operate on, such as w (word), $ (to the end of line).


#### General
    - undo: u	//undo the last command; U	//undo opeartions on a whole line.
    - redo: <CTRL-R>

#### File Operation

    - open/create file
        -  # vim file
    - close file
        -  # :q
        -  # ZZ
    - open a file in vim
        -  # :open file
    - switch to next file
        -  # :bn
    - switch to previouse file
        -  # :bp 

#### Parenthesis pairing
    - # %

#### Copy & paste
    3.1 copy 
        # yy
    3.2 paste
        # p //paste in current cursor.
        # P //paste in current line.
    3.3 cut & paste
        1.# V(whole line), v(character)     //visual mode
        2.d                                 //cut
        3.p                                 //paste

#### Insertion
    4.1 # I //Insert from the begining of the line.
    4.2 # A //Insert from the end of the line.
    4.3 # i //Insert at the cursor
    4.4 # a //Insert (1) character after the cursor
    4.5 # o //Insert a line after current line.
    4.6 # O //Insert a line before current line.

#### Search
    5.1 # /text
        5.1.1 n -> find next
        5.1.2 N -> find previous

        5.1.3 config
            5.1.3.1 :set ignorecase //ignore case.
            5.1.3.2 :set noignorecase //doesn't ignore cse
            5.1.3.3 :set incsearch //search when start input characters, rather than hitting <enter>

#### Replace
    6.1 # r* //replace current character(after cursor) to any character (only one); 
    6.2 # :s/old/new/       //replace the first meet (old) in current line to (new);
    6.3 # :s/old/new/g      //replace all (old) in current line to (new);
    6.4 # :%s/old/new/      //replace the first meet (old) in any line of a file to (new);
    6.5 # :%s/old/new/g     //replace all (old) in the file to (new);

       
#### Move cursor
    7.1 # [[        //move to the begining of the file;
    7.2 # ]]        //move to the end of the file.
    7.3 shift + direction.
    7.4 # 0         //move to the begining of the line.
    7.4.1 # $       //move to the end of the line.
    7.5 # :w        //move to the begining of next word.
    7.6 # :b        //move to the begining of previous word.
    7.7 # :e        //move to the end of current word.
    7.8 # :n*       //repeat operation n times.

#### Delete
    8.1 # x         //similar to delete
    8.2 # dd        //remove current line
    8.3 # D         //remove from current character to the end of the line.
    8.3.1 or use # d$
    8.4 # :A, *d    //remove line A-*
    8.5 # :1, $d    //remove all lines
    8.6 # :d + direction key. 

    8.7 Remove words
        8.7.0 #d + n + w   //delete next n words.
        8.7.1 #dw   //remove till the begining of next word.
        8.7.2 #de   //remove till the end of current word.
        8.7.3 #db   //(Delete).
        8.7.4 #cw   //de + i.
    8.8 delete to the end of the line: d$.

#### visual mode
    9.1 v + use direction key: copy characters/words.
    9.2 <Shift + v> + use direction key: copy lines.

#### Window
    10.1 split window
        # :split, vertical split.
	# :vsplit, horizontal split.

    10.2 close split
        # :close

    10.3 open another file in the same window
        # :split ./filename

    10.4 choose between different window:
        # <Ctrl + W> + h,j,k,l

# Appendix
* https://www.jianshu.com/p/117253829581
