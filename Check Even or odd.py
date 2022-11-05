#Check Even or odd

value = None

while value != 0:
    value = int(input("enter your number(type 0 to exit): "))
    
    if value == 0:
        break
    elif value%2 == 0:
        print(value,"is even")
    else:
        print(value,"is odd")

   