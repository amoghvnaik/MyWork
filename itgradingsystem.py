name = input("Enter name: ")

while(1):        
    try:
        homework = int(input("Enter homework mark: "))
        if homework > 25 or homework < 0:
            print("Please enter a mark out of 25")
            continue
        else:
            print("Thank you")
            break
    except ValueError:
        print("Please enter a number")
        
while(1):
    try:
        assessment = int(input("Enter assessment mark: "))
        if assessment > 50 or assessment < 0:
            print("Please enter a mark out of 50")
            continue
        else:
            print("Thank you")
            break
    except ValueError:
        print("Please enter a number")

while(1):
    try:
        exam = int(input("Enter exam mark: "))
        if exam > 100 or exam < 0:
            print("Please enter a mark out of 100")
            continue
        else:
            print("Thank you")
            break
    except ValueError:
        print("Please enter a number")

total_mark = homework*0.25 + assessment*0.35 + exam*0.4
total_percentage = float(total_mark/63.75*100)

print("Name: ", name)

if total_percentage >= 90:
    print("Grade : A*")
elif total_percentage >= 80:
    print("Grade : A")
elif total_percentage >= 70:
    print("Grade : B")
elif total_percentage >= 60:
    print("Grade : C")
elif total_percentage >= 50:
    print("Grade : D")
elif total_percentage >= 40:
    print("Grade : E")
elif total_percentage >= 30:
    print("Grade : F")
else:
    print("Grade: U")
