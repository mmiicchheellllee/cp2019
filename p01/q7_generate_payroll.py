 '''
7 (Payroll)
Write a program q7_generate_payroll.py that reads the following information and prints a payroll statement. A sample input and output session is as follows:

Sample input:

Enter name: Lim Ah Seng
Enter number of hours worked weekly: 10
Enter hourly pay rate: 6.75
Enter CPF contribution rate(%): 20

Sample output:

Payroll statement for Lim Ah Seng
Number of hours worked in week: 10
Hourly pay rate: $6.75
Gross pay = $67.50
CPF contribution at 20% = $13.50
Net pay = $54.00 '''

name = str(input("Enter name: "))
hours = int(input("Enter number of hours worked weekly: "))
pay_rate = float(input("Enter hourly pay rate: "))
CPF = int(input("Enter CPF contribution rate(%): "))

print("Payroll statement for ", name)
print("Number of hours worked in week: ", hours)
print("Hourly pay rate: $", pay_rate)
print("Gross pay = $""{0:.2f}".format(hours * pay_rate))
print("CPF contribution at", CPF, "% = $""{0:.2f}".format((20/100) * (hours * pay_rate)))
print("Net pay = $""{0:.2f}".format(((hours * pay_rate) - ((20/100) * (hours * pay_rate)))))
