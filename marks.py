marks = []
total = int(input("Total number of students are:\t"))

def marksInput():
    print("\n----------\nNOTE: PLEASE ENTER MARKS OUT OF 50. ENTER '-1' FOR ABSENT STUDENTS.\n----------\n")
    for i in range(total):
        enterMarks = int(input(f"Enter marks for student {i+1}:\t"))
        marks.append(enterMarks)
    print(f"\n-----\nMarks of {total} students are:\t{marks}\n-----")

def average_marks():
    marks_withoutAbsent = []
    for i in marks:
        if (i >= 0):
            marks_withoutAbsent.append(i)
        else:
            continue
    average_calc = sum(marks_withoutAbsent) / total
    print(f"\n------\nAverage score of {total} students is:\t{average_calc}\n-----")

def high_low():
    maxi = marks[0]
    mini = marks[0]
    for i in range(len(marks)):
        if (maxi < marks[i] and marks[i] > -1):
            maxi = marks[i]
    for j in range(len(marks)):
        if (mini > marks[j] and marks[j] > -1):
            mini = marks[j]
    print(f"\n-----\nHighest score is:\t{maxi}\nLowest score is:\t{mini}\n-----")

def absent():
    absent_count = 0;
    for i in marks:
        if (i < 0):
            absent_count+=1
        else:
            continue
    print(f"\n-----\nTotal absent students are:\t{absent_count}\n-----")

def high_freq():
    freq_count = 0 
    for i in range(len(marks)): 
        if (marks[i] >= 0):
            temp_count = 0 
            for j in range(len(marks)): 
                if (marks[i] == marks[j]):
                    temp_count+=1
            if (freq_count < temp_count):
                freq_count = temp_count
    print(f"\n-----\nHighest frequency is:\t{freq_count}\n-----")

def main():
    marksInput()
    
    while (1):
        print("\n----- MAIN MENU -----")
        print("1 -> Average score of class")
        print("2 -> Highest and lowest score of class")
        print("3 -> Total absent students")
        print("4 -> Marks with highest frequency")
        print("5 -> Exit")
        
        optn = int(input("Choose an option (1-5):\t"))
        
        if (optn == 1):
            average_marks()
        elif (optn == 2):
            high_low()
        elif (optn == 3):
            absent()
        elif (optn == 4):
            high_freq()
        elif (optn == 5):
            print("\n\nExiting\n\n")
            quit()
        else:
            print("\n\nPlease choose a valid option (1-5)\n\n")
main()