#Get a input for score percentage. Only If the percentage is greater than 70, get input for his name, department and location. Then print you are elgibile. If not print you are not eligible.

salary=int(input("Enter the Salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25):
    amt=int(input("Enter the required loan amt:"))
    if(amt>=50000):
       print("THE MAX LOAN AMOUNT IS 50000 ")
    else:
          print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")

