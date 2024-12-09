def linear(num , search):
    for i in range(len(num)):
        if(num[i] == search):
            print("Element found at index :",i)
            return
    print("Element not found")

def sentinel(num , search):
    last = num[len(num) - 1]
    num[len(num)-1] = search
    for i in range(len(num)):
        if(num[i] == search):
            break
    if(i != (len(num)-1) or last == search):
        print("Element found")
    else:
        print("Element not found")

nums = []
n = int(input("Enter the total number of students:-"))
print("Enter roll numbers:-")
for i in range(n):
    element = int(input("Roll no:"))
    nums.append(element)
print(nums)
search = int(input("Enter roll number to be search in students list :"))
linear(nums,search)
sentinel(nums,search)