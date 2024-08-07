#Day-3
#Reverse of number
n=int(input("Enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)
  
#using String
n=543
print(str(n)[::-1])  