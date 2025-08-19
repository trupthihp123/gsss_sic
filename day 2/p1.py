Name=input("enter the employee name:")
EmpID=int(input("enter the employee ID:"))
Basic_monthly_salary=float(input("enter the basic monthly salary:"))
Special_allowance=float(input("enter the special allowance:"))
Bonus_Percentage=float(input("enter the bonus percentage:"))
Annual_gross_salary=Basic_monthly_salary*0.15
print("The annual gross salary of the employee is:", Annual_gross_salary)
Gross_Monthly_Salary=Basic_monthly_salary+Special_allowance +(Annual_gross_salary)
