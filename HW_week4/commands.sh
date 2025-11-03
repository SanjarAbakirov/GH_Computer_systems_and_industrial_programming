name="Sanjar"
echo "Hello, $name!"
echo 'Hello, $name!' # single quotes do not expand variables

echo "I'm in $(pwd) this directory."
echo "I'm here `pwd` too."  # older syntax using backticks

while read -r line; do
    echo "Line: $line"
done < HW_week4/commands.sh

printf "Hello %s, I'm %s " Sven Olga 
printf "%.2f\n" 3.14159