name="Kriti"
Name="Puri"

print(name)
print(Name)

age=21
if age>18:
    print(age)
else:
    print("Age is 18 or below")
    
print(age)

## Line Continuation
##Use a backslash (\) to continue a statement to the next line

total=1+6+3+4+5+6+7+\
10+5+6

print(total)

## Multiple Statements on a single line
x=50;y=70;z=x+y
print(z)

##Understand  Semnatics In Python
# variable assignment
age=21 ##age is an integer
name="Kriti" ##name is a string

## Type Inference
variable=40
print(type(variable))
variable="Kriti"
print(type(variable))

age=21
if age>20:
    print(age)

    
    
## Name Error
#a=b

## Code exmaples of indentation
if True:
    print("Correct Indentation")
    if False:
        print("This ont print")
    print("This will print")
print("Outside the if block")