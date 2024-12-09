def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [] 
    middle = [] 
    right = []
    for i in arr:
        if (i < pivot):
            left.append(i)
        elif (i == pivot):
            middle.append(i)
        else:
            right.append(i)

    return quickSort(left) + middle + quickSort(right)

def top5(arr):
    top_scores = quickSort(arr)
    return top_scores[-1:-6:-1]

def main():
    percent = [] 
    
    total = int(input("Total number of students are:\t"))
    for i in range(total):
        percent_in = float(input(f"Enter percentage for student {i+1}:\t"))
        percent.append(percent_in)
    
    print(f"-----\nPercentages of students are:\t {percent}\n-----")
    print(f"\n-----\nSorted marks (using quick sort algorithm):\t{quickSort(percent)}\n-----")
    print(f"\n-----\nTop five scores are:\t{top5(percent)}\n-----")

main()