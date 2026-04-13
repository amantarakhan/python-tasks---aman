total = int(input ('what is the first number : '))
while True :
    print (f"current total :  {total}")
    operation = input("Enter operator (+, -, *, /) or '=' to finish: ") 
    if (operation == '=') : 
        break  
    
    number = int (input ("what is your sec number : "))

    if (operation == '+') : 
        total += number
    elif (operation == '-') : 
        total -= number
    elif (operation == '*') : 
        total *= number 
    elif (operation == "/" ) :
        total /= number
    else:
        print("Invalid operator!")

print (f'final result :  {total}')