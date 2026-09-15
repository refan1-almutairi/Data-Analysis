
num1=int(input("Enter Frist number: ")) 
num2=int(input("Enter second number:"))
chossen=input("Enter operation (+,-,*,/):  ")

if  chossen=="+":
      print(num1+num2)
elif chossen=="-":
      print(num1-num2)
elif chossen=="*":
      print(num1*num2)

elif chossen=="/":
     if num2 ==0:
        print("error:division by zero is not allowed.")
     else:
          print(num1/num2) 
print("invalid operation.pleae choose from (+.-,*,/)")


