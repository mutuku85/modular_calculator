import operators
import others
import trig

operator=input("enter the operator")
if operator=="cube":
    num=eval(input("enter number"))
    x=others.cube(num)
    print(x)
elif operator=="sin":
    angle=eval(input("enter angle in degrees"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)
elif operator== "tan":
    angle=eval(input("enter angle in degrees"))
    tan_of_angle=trig.get_tan(angle)
    print(tan_of_angle)
else:
    num1=eval(input("enter number 1:"))
    num2=eval(input("enter number 2:"))
if operator== "+":
    x=operators.add(num1,num2)
    print(x)
elif operator==  "-":
    x=operators.subtract(num1,num2)
    print(x)
elif operator=="*":
    x=operators.multiply(num1,num2)
    print(x)
elif operator=="/":
    x=operators.divide(num1,num2)
    print(x)
    

