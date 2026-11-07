# Q1 Find the largest of three numbers------------------->
a=int(input("Enter a number :"))
b=int(input("Enter b number :"))
c=int(input("Enter c number :"))

if a>b :
    if a>c :
        print("a is greater than b and c")
    else :
        print("c is greater than b and a")

else :
    if b>c :
        print("b is greater than c and a")
    else :
       print ("c is greater than b and a")

#Q2 Assign grades:------------------------------------------>
# ● A → marks ≥ 90
# ● B → marks ≥ 75
# ● C → marks ≥ 60
# ● Fail → below 60

marks=int(input("Enter marks : "))
if marks>=90 :
    print("A Grade ")
else :
   if marks>=75 :
    print("Grade B")
   else :
    if marks>=60 :
     print("C Grade ")
    else :
     print("Fail ")

#Q3 Check whether a triangle is equilateral, isosceles, or scalene------------------------>
a=input("Enter a number :")
b=input("Enter b number :")
c=input("Enter c number :")

if a==b and b==c and c==a :
    print("The triangle is equilateral")
else:
    if a==b or b==c or c==a :
     print("The triangle is isosceles")
    else :
        print("The triangle is scalene")

#Q4 Check whether a character is uppercase, lowercase, digit, or special character-------------->
ch=input("Enter  character :")

if "A" <=ch<="Z" :
    print("The character is upper case")
else :
    if "a"<=ch<="z" :
        print("The character is lower case")
    else :
        if "0"<=ch<="9" :
            print("The character is digit")
        else :
                print("The character is special character")

#Q5 Calculate electricity bill using slab-wise rates.--------------------------------->
bill=int(input("Enter electricity bill: "))

if bill>50:
    print("Then slab-rate is 8 rupees :",bill*8)
else :
    print("Bills less than 50 then slabs rate is decrease :",bill*6)
#Q6 Validate login using username and password------------------------------------->
username=(input("Enter your username: "))
password=(input("Enter your password: "))

if username == "admin" :
    if password == "admin123" :
        print("login is Successful")
    else :
        print("login is not successful")
else :
    print("login is Failed")
#Q7 Check student result using marks of 3 subjects----------------------------------------->
maths=int(input("enter Math Marks :"))
science=int(input("enter Math Marks :"))
computer=int(input("enter Math Marks :"))
if maths>33 :
    if science>33 :
        if computer>33 :
            print("Pass ")
        else :
            print("fail")
    else :
        print("fail")
else :
    print("fail")