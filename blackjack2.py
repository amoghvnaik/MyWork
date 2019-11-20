import sys
loop = 0
def play_again():
                while loop == 0:
                    play_again = input("Play again(Y/N)?")
                    if play_again == "Y":
                        break
                    elif play_again == "N":
                        sys.exit()
                    print("Please enter a valid response")
while 1:
    try:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        if first_number >= second_number and first_number < 22 or second_number > 21 and first_number < 22:
            print(first_number)            
            play_again()
        elif second_number > first_number and second_number < 22 or first_number > 21 and second_number < 22:
            print(second_number)
            play_again()
        else:
            print("0")
            play_again()
    except ValueError:
        print ("Please enter a valid number")

