# $#(number of args) here 
if [ $# -ne 3 ];then
    echo 'Usage: script Arg1 Arg2 Arg3.'
    exit 1
fi

# control flow here
echo 'Print parameters here:'
for para in $1 $2 $3;do
    echo $para
done

echo
if [ $1 -gt $2 ];then
    echo  $1 'is greater than' $2.
elif [ $1 -eq $2 ];then
    echo $1 'is equal to' $2.
else
    echo $1 'is smaller than' $2.
fi

if [ !true ];then
    echo 'Apparently, you are wrong.'
else
    echo 'Not bad'
fi

if [ 'Hello' = 'Hello' ];then
    echo 'Not case sensitive.'
else 
    echo 'hello != Hello.'
fi

if [ -f $3 ];then
    cat $3
else
    echo $3 'is not a file.'
fi

# $command here
echo 'print /:'
for stuff in $(ls /); do
    echo '  ' $stuff
done

# Case here
echo "Is it morning? Please answer yes or no:"
read timeOfDay

case "$timeOfDay" in
    [yY] | [yY][Ee]Ss] )    echo "Good Morning";;
    [nN] | [nN][oO] )     echo "Good Afternoon";;
    *)      echo "Nice Try";;
esac

# AND operator here:
touch file_one
rm file_two
if [ -f file_one ] && {
        echo "hello"
    } && [ -f file_two ] && echo " there";then
    echo "in if"
else
    echo "in else"
fi

# OR operator here:

# if [ -f file_one ] || ...
# Notes: AND, OR are in short circuit evaluation mode.
# And if want multi-statements in one condition -> use {} to cover them.

# function here:
func_test() {
    echo "Function test"
    local local_var=100
    # function must be defined before use.
}

echo "Function begin below..."
func_test
echo "Function ended above..."

# (($x)) used for arithmetic replacement, ($x) used for executing command and get output (or set)

x=0
while [ "$x" -ne 10 ];do
    echo $x
    x=$(($x+1))
done

exit 0

