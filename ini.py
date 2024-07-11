print("ini is a calculator program")

choice = str(input("Please choose what service you need (Division,Addition,Multiplication and Subtraction) : "))
#USERS CHOICE
if choice == "Division":
        div1 = int(input("First number : "))
        div2 = int(input("Second number : "))
        print("Result: ",div1/div2)
    #Division Finish
elif choice == "Addition":
        add1 = int(input("First number : "))
        add2 = int(input("Second number : "))
        print("Result :",add1 + add2)
    #Addition Finish
elif choice == "Multiplication":
        mul1 = int(input("First number : "))
        mul2 = int(input("Second number : "))
        print("Result: ",mul1 * mul2)
     #Multiplacation Finish
elif choice == "Subtraction":
        sub1 = int(input("First number : "))
        sub2 = int(input("Second number : "))
        print("Result : ",sub1 - sub2)
    #Substraction Finish
else:
        print("invalid")

print("Thank you for using ini.")
