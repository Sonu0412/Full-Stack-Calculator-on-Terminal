title = "Welcome to db calculator......"
print(title)

while True:
    firstNumber = int(input("Enter 1st number : "))
    secondNumber = int(input("Enter 2nd number : "))
    print('''
**NOTE**
1) For Sum enter : +
2) For Sub enter  : -
3) For Mul enter : *
4) For Div enter : /                  
''')

    def sums(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        if b != 0:
            return a / b
        else :
            return "The demominator cant be zero...."

    option = input("Enter your Input : ").strip()

    match option:
        case "+":
            result = sums(firstNumber, secondNumber)
            result_str = f"{firstNumber} + {secondNumber} = {result}"
            print(result_str)

        case "-":
            result = sub(firstNumber, secondNumber)
            result_str = f"{firstNumber} - {secondNumber} = {result}"
            print(result_str)

        case "*":
            result = mul(firstNumber, secondNumber)
            result_str = f"{firstNumber} * {secondNumber} = {result}"
            print(result_str)

        case "/":
            result = div(firstNumber, secondNumber)
            result_str = f"{firstNumber} / {secondNumber} = {result}"
            print(result_str)

        case _:
            print("Wrong Input....")
            continue


    usr = input("Do you want to continue? (yes/no): ").lower().strip()
    if usr == "no":
        save = input("Do you want to save the output? (yes/no): ").lower().strip()
        if save == "yes":
            fileName = input("Enter the file name to store with extension (ex.: Name.txt): ").strip()
            with open(fileName, "w") as file:
                file.write(f"{title}\n")
                file.write(f"Entered option: {option}\n")
                file.write(f"Result: {result_str}\n")
            print(f"Result saved in {fileName}")
        break

    elif usr == "yes" :
        continue
    else:
        print("The option not right....")