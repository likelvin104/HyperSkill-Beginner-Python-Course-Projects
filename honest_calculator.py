msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0
result = 0

# Get yes/no answer from user
def ask_yes_no_question(question):
    input_ = ""
    while True:
        print(question)
        input_ = input()
        if input_ in ["y", "n"]:
            return input_ == "y"

# Check if the given number is an integer
def is_one_digit(num):
    return num.is_integer() and -10 < num < 10

# Check the difficulty of the given equation
def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and oper != "/":
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

# Check if the equation is valid
while True:
    # Ask for user input
    print(msg_0)
    x, oper, y = input().split()

    # Check if the user uses number from memory
    if x == "M":
        x = memory
    
    if y == "M":
        y = memory

    # Check if the user input valid numbers
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    
    # Check if the user input a valid operator
    if oper not in ["+", "-", "*", "/"]:
        print(msg_2)
        continue
    
    check(x, y, oper)
    
    # Evaluate the answer of the equation
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y == 0:
        print(msg_3)
        continue
    else:
        result = x / y
    
    # Print the result
    print(result)
     
    # Store the result into memory
    if ask_yes_no_question(msg_4):
        if is_one_digit(result):
            msg_index = 10
            while msg_index <= 12:
                if ask_yes_no_question(eval("msg_"+str(msg_index))):
                    msg_index += 1
                else:
                    break
            if msg_index == 13:
                memory = result
        else:
            memory = result

    
    # Stop the Program or continue calculations
    if ask_yes_no_question(msg_5):
        continue
    else:
        break
