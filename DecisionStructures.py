# Definitions/Declarations
def ifStatement():
    answer = input("Type y or n ")
    if answer == "y":
        print("Your answer is YES")
    elif answer == "n":
        print("Your answer is NO")
    else:
        print("Answer is not valid")
    return

def whileStatement():
    answer = int(input("Type a number greater an 0 "))
    while answer != 0:
        print(answer)
        answer = answer - 1
    return

def forStatement():
    listA = ["apple", "orange", "banana", "avacado"]
    for items in listA:
        print(items)
    return

def main():
    # ifStatement()
    # whileStatement()
    # forStatement()
    return

######################

main()