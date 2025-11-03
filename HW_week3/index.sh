echo "Hello world!"
x="my name is a boy Sammy"
y="his name is Tommy"

echo '$x'
echo "$x"

echo "${y}"
echo "${x:0:7}"
echo "${y:2:8}"
echo "${#x}"
echo "${y#*a }"
