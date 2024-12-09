def dedup(d):
    list1=[]
    for i in d:
        if i not in list1:
            list1.append(i)
    return list1
    
def intersection(list1,list2):
    list3=[]
    for a in list1:
        if a in list2:
            list3.append(a)
    return list3

def union(list1,list2):
    list3=list1.copy()
    for a in list2:
        if a not in list3:
            list3.append(a)
    return list3

def difference(list1,list2):
    list3=[]
    for a in list1:
        if a not in list2:
            list3.append(a)
    return list3
def symmetric_difference(list1,list2):
    list3=[]
    d1=difference(list1,list2)
    d2=difference(list2,list1)
    list3=union(d1,d2)
    return list3

def func1(list1,list2):
    list3=intersection(list1,list2)
    print('The number of students who play both cricket & badminton are ', len(list3))
   
def func2(list1,list2):
    list3=symmetric_difference(list1,list2)
    print('The number of students who play either cricket or badminton are: ', len(list3))

def func3(list1,list2):
    list3=intersection(list1,list2)
    list4=[]
    result=len(SE_Comp)-len(list1)-len(list2)+len(list3)
    print('The number of students who play neither cricket nor badminton are: ', result)

def func4(list1,list2,list3):
    list4=difference(intersection(list1,list2),list3)
    print('The number of students who play cricket & football but not badminton are: ', len(list4))

#Main
SE_Comp=[]
n=int(input('Enter Number of Students '))
for i in range(0,n):
    name=input('Enter Name ')
    SE_Comp.append(name)
print('List of Students in SE Computer:', str(SE_Comp))


Cricket=[]
n=int(input('Enter Number of Students playing Cricket '))
for i in range(0,n):
    name=input('Enter Name ')
    Cricket.append(name)
dCricket=dedup(Cricket)
print('List of Students who play Cricket:', str(dCricket))

Football=[]
n=int(input('Enter Number of Students playing Football '))
for i in range(0,n):
    name=input('Enter Name ')
    Football.append(name)
dFootball=dedup(Football)
print('List of Students who play Football:', str(dFootball))

Badminton=[]
n=int(input('Enter Number of Students playing Badminton '))
for i in range(0,n):
    name=input('Enter Name ')
    Badminton.append(name)
dBadminton=dedup(Badminton)
print('List of Students who play Badminton:', str(dBadminton))


while(True):
    print("Choose an option")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))
    if(ch==1,ch==2,ch==3,ch==4,ch==5):
        if (ch==1):
            func1(Cricket,Badminton)
        if (ch==2):
            func2(Cricket,Badminton)
        if (ch==3):
            func3(Cricket,Badminton)
        if (ch==4):
            func4(Cricket,Football,Badminton)
        if (ch==5):
            exit()
        next=input('Do you want to do another operation?(Yes=Y, No=N) ')
        Y=1
        N=2
        if(next=='N'):
            break
        if(next=="Y"):
            continue
    else:
      print('Invalid choice')