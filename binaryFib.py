def binarysearch(arr,x,low,high):
  while (low<=high):
    mid=low+(high-low)//2
    if (x==arr[mid]):
      return mid
    elif (x>arr[mid]):
      low=mid+1
    else:
      high=mid-1
  return -1
def rbinarysearch(arr,x,low,high):
  if (high>=low):
    mid=low+(high-low)//2
    if (x==arr[mid]):
      return mid
    elif (x<arr[mid]):
      return rbinarysearch(arr,x,low,mid-1)
    else:
      return rbinarysearch(arr,x,mid+1,high)
  else:
    return -1
def fibsearch(arr,x,n):
  f2=0
  f1=1
  fib=f1+f2
  while(fib<n):
    f2=f1
    f1=fib
    fib=f1+f2
  off=-1
  while(fib>1):
    i=min(off+f2,n-1)
    if (arr[i]<x):
      fib=f1
      f1=f2
      f2=fib-f1
      off=i
    elif(arr[i]>x):
      fib=f2
      f1-=f2
      f2=fib-f1
    else:
      return i
  if(f1 and arr[n-1]==x):
    return n-1
  return -1
def insert(dict,name):
  name=find
  number=int(input('Enter Number '))
  dict[name]=number
def create():
  name=input('Enter Name ')
  number=int(input('Enter Number '))
  dict1[name]=number
  ch2=input('Do you want to create another contact?\n(Enter Y for Yes & N for No) ')
  if ch2.upper()=='Y':
    create()
def absent():
  print(find,'is not present in phonebook')
  insert(dict1,find)
  print(find,'has been inserted in phonebook')

#Main
flag=0
dict1={}
while (flag==0):
  ch=int(input('Welcome To Phonebook\nPlease Enter Your Choice:\n1.Create\t2.Search\n3.Display\t4.Update\n5.Delete\t6.Exit '))
  if ch==1:
    create()
  elif ch==2:
    find=input('Enter Name to search ')
    ch1=int(input('Enter the operation you want to perform:\n1.Iterative Binary Search\n2.Recursive Binary Search\n3.Fibonacci Search '))
    if ch1==1:
      result=binarysearch(list(sorted(dict1)),find,0,len(list(dict1))-1)
      print('Binary using iterative')
      if result!=-1:
        print(find,'is present at index %d in phonebook'%(result))
        print('%s\'s number is %d'%(find,dict1[find]))
      else:
        absent()
    elif ch1==2:
      result1=rbinarysearch(list(sorted(dict1)),find,0,len(list(dict1))-1)
      print('Binary using recursive')
      if result1!=-1:
        print(find,'is present at index %d in phonebook'%(result1))
        print('%s\'s number is %d'%(find,dict1[find]))
      else:
        absent()
    elif ch1==3:
      result2=fibsearch(list(sorted(dict1)),find,len(list(dict1)))
      print('Fibonacci')
      if result2!=-1:
        print(find,'is present at index %d in phonebook'%(result2))
        print('%s\'s number is %d'%(find,dict1[find]))
      else:
        absent()
  elif ch==3:
     print('Phonebook:\n',dict1)
     count=0
     print('\t Name\t\t Number')
     for i in dict1:
       print('%d.\t'%(count),str(i),'\t',dict1[i])
       count+=1
  elif ch==4:
    upd=input('Enter Name of contact you wish to update ')
    if upd in dict1:
      new=int(input('Enter %s\'s new number: '%(upd)))
      dict1[upd]=new
      print('%s\'s number has been successfully updated'%(upd))
    else:
      print('%s does not exist'%(upd))
  elif ch==5:
    del1=input('Enter the name of the contact you want to delete ')
    if del1 in dict1:
      del dict1[del1]
      print('%s has been successfully deleted'%(del1))
    else:
      print('%s does not exist'%(del1))
  elif ch==6:
    flag=1
  else:
    print('Invalid choice')