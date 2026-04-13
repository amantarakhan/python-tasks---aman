total = float(input('what is the first number : ')) # Changed to float for safety
while True :
    print (f"current total : {total}")
    operation = input("Enter operator (+, -, *, /) or '=' to finish: ") 
    if (operation == '=') : 
        break  
    
    number = float(input("what is your sec number : ")) # Changed to float

    if (operation == '+') : 
        total += number
    elif (operation == '-') : 
        total -= number
    elif (operation == '*') : 
        total *= number 
    elif (operation == "/" ) :
        if (number == 0 ) : 
            print ("you can't devide smth on zero ")
        else:  
            total /= number
    else:
        print("Invalid operator!")

print (f'final result : {total}')