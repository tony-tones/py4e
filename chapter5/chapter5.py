largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        num = int(num)
    except ValueError:
        print("Invalid Input")
        continue
    if largest is None or num > largest :
        largest = num
        continue
    elif smallest is None or num < smallest :
        smallest = num
        continue
    
print("Maximum is", largest)
print("Minimum is", smallest)
