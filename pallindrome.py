#To check whether given number is pallindrome or not
r=None
sum=0
temp=None
number=input("Enter the number: ") #Taking input from user
number = int(number)
temp=number

while(number>0):
    r=int(number%10) #getting remainder
    sum=(sum*10)+r
    number=int(number/10)

if(temp==sum):
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")
