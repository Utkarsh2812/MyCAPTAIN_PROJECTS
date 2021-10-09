terms = int(input("How many terms do you want? "))

n1 = 0
n2 = 1
count = 0

if terms < 0:
   print("Please enter a positive integer")


elif terms == 1:
   print(f"Fibonacci sequence upto {terms} :")
   print(n1)


else:
   print("Fibonacci sequence: " , end='')
   while count < terms:
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       count = count+1