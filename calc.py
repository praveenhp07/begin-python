try:
 print"1. Addition"
 print"2. Subtraction"
 print"3. Multiplication"
 print"4. Division"
 try:
   op=abs(input("Enter your choice: "))
 except:
   print "Please enter the correct choice" 
 if (op==1 or op==2 or op==3 or op==4):
    print"Enter two numbers: "
    try:
     num1=int(input())
     num2=int(input())
    except:
      print"Please enter integer value" 
    if op == 1:
    	res=num1+num2
    	print"Result = ",res
    elif op == 2:
    	res=num1-num2
    	print"Result = ",res
    elif op == 3:
    	res=num1*num2
    	print"Result = ",res
    elif op == 4:
    	res=num1/num2
    	print"Result = ",res 
 else:
     print"Wrong input..!!"
except:
  print"error.. exception!"