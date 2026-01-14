## Declaring And Assigning Variables

age=21
height=5.1
name="Kriti"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)
print("Is Student:", is_student)

## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="Kriti"
last_name="Puri"

# Invalid variable names
#9age=21
#first-name="Kriti"
#@name="Kriti"

## case sensitivity
name="Kriti"
Name="Puri"

age=25
print(type(age))

#Type conversion
age_str = str(age)
print(age_str)
print(type(age_str))

age = '25'
print(type(int(age)))

height = 5.1
type(height)
print(type(int(height)))

## Dynamic Typing
## Python allows the type of a variable to change as the program executes
var=10 
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))

#input
age = int(input("enter your age:"))
print(age,type(age))


# SIMPLE CALCULATOR
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

sum = num1 + num2
diff = num1 - num2
prod = num1*num2
quot = num1/num2

print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Quotient:", quot)