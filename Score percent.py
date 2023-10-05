# Get input for salary and age.
# If salary greater than or equal to 20000 or age less than or equal to 25, get input for required loan amount. If not print you are not eligible for loan. 
# If required loan amount is less than or equal to 50,000 print You are eligible for loan. If it is greater than 50,000 print maximum loan amount is 50000.

score=int(input("Enter the Score Percent:"))
if(score>=70):
    name=input("enter the name:")
    dep=input("enter the dep:")
    loc=input("enter the loc:")
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
