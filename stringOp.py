def longest_word(word_list):
    word_len = []
    for n in word_list:
        word_len.append((len(n), n))
    word_len.sort()
    result=word_len[-1][0], word_len[-1][1]
    print('\nLongest word',result[1])
    print('Length of the longest word',result[0])
def occurrences():
  count=0
  ch=input('Enter character ')
  for i in str1:
    if i==ch:
      count+=1
  print('%c occurs %i times'%(ch,count))
def palindrome(a):
  if a==a[::-1]:
    print('%s is a palindrome'%a)
  else:
    print('%s is not a palindrome'%a)
def index():
  c=input('Enter character ')
  position=0
  for i in range(0, len(str1)):
    if str1[i] == c:
        position = i + 1
        break
  if position==0:
    print('No character found')
  else:
    print('%c is present at index %i'%(c,position-1))
def word_count(str1):
  count=dict()
  words=str1.split()
  for word in words:
    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  print(count)
#main
str1=input('Enter a string ')
flag=0
while(flag==0):
  option=int(input('Enter your choice\n1.Longest Word\t2.Occurrences of a character\n3.Palindrome\t4.Index of a character\n5.Word Count\t6.Exit '))
  if (option==1):
    longest_word(str1.split())
  elif (option==2):
    occurrences()
  elif (option==3):
    palindrome(str1)
  elif (option==4):
    index()
  elif (option==5):
    word_count(str1)
  elif (option==6):
    flag=1
  else:
    print('Invalid Choice')