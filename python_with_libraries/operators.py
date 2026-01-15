## Arithmethic Operation

a=49
b = 30

add_result=a+b  #addiiton
sub_result=a-b  #substraction 
mult_result=a*b #multiplication
div_result=a/b  #division
floor_div_result=a//b ## floor division
modulus_result=a%b #modulus operation

exponent_result=a**b ## Exponentiation


print(add_result)
print(sub_result)
print(mult_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponent_result)

## Comparison Operators
## == Equal to
a=10
b=10

a==b

str1="Kriti"
str2="Kriti"

str1==str2

## Not Equal to !=
str1!=str2

str3="Kriti"
str4="kriti"

str3!=str4

# greater than >

num1=45
num2=55

num1>num2

## less than <

print(num1<num2)

#greater than or equal to
number1=45
number2=45

print(number1>=number2)

#less than or equal to
number1=44
number2=45

print(number1<=number2)

## Logical Operators
## and , or , not
x = 5   
y = 10
z = 15
# and operator
result_and = (x < y) and (y < z)  # True and True -> True
print("Result of AND operator:", result_and)
# or operator
result_or = (x > y) or (y < z)    # False or True -> True
print("Result of OR operator:", result_or)
# not operator
result_not = not(x < y)            # not True -> False
print("Result of NOT operator:", result_not)
## Bitwise Operators
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
# AND operator
c = a & b  # 12 = 0000 1100
print("Result of AND operation:", c)

# OR operator
c = a | b  # 61 = 0011 1101
print("Result of OR operation:", c)
# XOR operator
c = a ^ b  # 49 = 0011 0001
print("Result of XOR operation:", c)

# NOT operator
c = ~a     # -61 = 1100 0011
print("Result of NOT operation:", c)
# Left Shift operator
c = a << 2 # 240 = 1111 0000
print("Result of Left Shift operation:", c)
# Right Shift operator

c = a >> 2 # 15 = 0000 1111
print("Result of Right Shift operation:", c)



