#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
#numbers = []

#while True:
#    num = input("Enter number: ")
#    try:
#        if num == 'done':
#            break
#        else:
#            fnum = float(num)
#            numbers.append(fnum)
#    except:
#        print("Invalid input")
#        continue

#min_num = min(numbers)
#max_num = max(numbers)
#print("Minimum number: ", min_num, "Maximum number: ", max_num)

i = 0
m = 0
while True:
    num = input("Enter number: ")
    if num == 'done':
        break
    else:
        try:
            fnum = float(num)
        except:
            print("Invalid input")
            continue
        if i == 0:
            smallest_num = fnum
            i=i+1
        elif fnum < smallest_num:
            smallest_num = fnum
        else:
            if m == 0:
                largest_num = fnum
                m=m+1
            elif fnum > largest_num:
                largest_num = fnum

print("Minimum number:", smallest_num, "Maximum number:", largest_num)
