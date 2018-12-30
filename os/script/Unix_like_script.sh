if [ $# -ne 3 ];then
    echo 'Usage: script Arg1 Arg2 Arg3.'
    exit 1
fi

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

echo "Is it morning? Please answer yes or no:"
read timeOfDay

if [ "$timeOfDay" = "yes" ];then
    echo "  Good morning."
elif [ "$timeOfDay" = "no" ];then
    echo "  Good sleep."
else
    echo "  nice try."
fi

echo 'print /:'
for stuff in $(ls /); do
    echo '  ' $stuff
done

exit 0

