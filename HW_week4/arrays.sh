array=(you will be the best programmer)

# echo ${array[5]}  # Output: best
# echo ${array[@]}  # Output: you will be the best programmer
# echo ${#array[@]} # Output: 6

function foo()
{
    echo "Arguments passed to script: $@"
    echo "And: $1 $2..."
    echo "This is a function"
    returnValue=0
    return $returnValue
}
foo arg1 arg2
returnValue=$?

bar ()
{
    echo "This is another function"
    return 0
}
bar

foo "My name is Sanjar"