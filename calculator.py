COUNT = 0
SUM = 0
AVERAGE = 0

# infinite loop to get constanly inputs unless "Done" is entered.
while True:
    NUM = input("Enter a number:").lower()
    if NUM == "done":
        break
    else:
        try:
            SUM = int(NUM) + SUM
            COUNT += 1  # COUNT = COUNT + 1
        except:
            print("Invalid Input")

print("Count=", COUNT, "Sum =", SUM, "Average =", SUM/COUNT)
