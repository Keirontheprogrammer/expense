# fruits =["pineapple","peach","avocado"]

# def list_fruits(fruit):
#     for i, fruit in enumerate (fruits):
#         print(f"Fruits{i}:{fruit}!")

# list_fruits(fruits)

# a, b = 0, 1 
# while a<10:
#     print(a, end=',')
#     a, b = b, a+b;


# a calculator #

def calculator():
    number1 =int(input("First number :"))
    number2 =int(input("Second number :"))
    symbol =input("pick the operator (+,-,/,*):")
    
    match symbol:
            case '+':
                return number1 + number2
            case '-':
                return number1 - number2
            case '/':
                if  number2 ==0:
                     return "ERROR: Nigga is you dumb ?"
                return number1 / number2
            case '*':
                return number1 * number2
            case _:
              return "ERROR: Pick a valid operator"
         

result =calculator();
print(result)



 