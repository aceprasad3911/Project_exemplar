# option 2
import csv
from datahandler import data
import math


# process ui
def process():
    choice = int(input("""How would you like to process the data?
    Number of records loaded    [1]
    Department Names            [2]
    Employee Record             [3] (Employee ID Required)
    Employees in department     [4]
    Employees Department + Role [5]
    Employees of Job Role       [6]
    Summary                     [7]
    Choice:  """))
    if choice == 1:
        print(f"There are {len(data) - 1} profiles.")
    elif choice == 2:
        print("Departments:")
        uniquedept(data)
    elif choice == 3:
        employeeid = int(input("Enter Employee ID:  "))
        filter_by_employee_id(data, employeeid)
    elif choice == 4:
        departmentid = input("Enter Department:  ")
        filter_by_department(data, departmentid)
    elif choice == 5:
        department = input("Enter Department:   ")
        role = input("Enter Role:   ")
        filter_by_department_role(data, department, role)
    elif choice == 6:
        role = input("Enter Job Role:   ")
        filter_by_role(data, role)
    elif choice == 7:
        dept = input("Please Choose a Department: ")
        summary(data, dept)
    else:
        print("Invalid option...")


# unique departments
def uniquedept(dat):
    reader = csv.reader(dat)
    next(reader)
    unique = set(row[5] for row in reader)
    for value in unique:
        print(value)


# data summary
def summary(dat, department):

    print(f"Summary for {department}:")
    reader = csv.DictReader(dat)
    records = list(reader)
    # Age
    ages = [int(record['Age']) for record in records if record['Department'].lower() == department.lower()]

    minage = min(ages)
    maxage = max(ages)
    numemploy = len(ages)
    meanage = sum(ages) / numemploy
    print(f"""Age Stats:
    Youngest: {minage}, Oldest: {maxage}, Average: {meanage}""")

    # Distance from home
    dist = [int(record['DistanceFromHome']) for record in records if record['Department'].lower() == department.lower()]

    mindist = min(dist)
    maxdist = max(dist)
    numdist = len(dist)
    meandist = sum(dist) / numdist
    print(f"""Distances From Home:
    Closest: {mindist}, Furthest: {maxdist}, Average: {meandist}""")

    # Hourly Pay
    pay = [float(record['HourlyRate']) for record in records if record['Department'].lower() == department.lower()]
    minpay = min(pay)
    maxpay = max(pay)
    numpay = len(pay)
    meanpay = sum(pay) / numpay
    print(f"""Hourly Wages:
    Least: {minpay}, Most: {maxpay}, Average: {meanpay}""")

    # Martial Stat
    single = 0
    marry = 0
    divorce = 0
    total = 0
    for record in records:
        if record['Department'].lower() == department.lower():
            total += 1
            if record['MaritalStatus'] == 'Single':
                single += 1
            elif record['MaritalStatus'] == 'Married':
                marry += 1
            elif record['MaritalStatus'] == 'Divorced':
                divorce += 1
    percentagemarry = (marry / total) * 100
    percentagediv = (divorce / total) * 100
    percentagesing = (single / total) * 100
    print(f"""Marital Stats:
    Single: {percentagesing}%, Married: {percentagemarry}%, Divorced: {percentagediv}%""")

    # Business Travel
    freq = 0
    rare = 0
    never = 0
    for record in records:
        if record['Department'].lower() == department.lower():
            if record['BusinessTravel'] == 'Frequently':
                freq += 1
            elif record['BusinessTravel'] == 'Rarely':
                rare += 1
            elif record['BusinessTravel'] == 'Never':
                never += 1
    percentagefreq = (freq / total) * 100
    percentagerare = (rare / total) * 100
    percentagenever = (never / total) * 100
    print(f"""Business Travel Stats:
    Frequently: {percentagefreq}%, Rarely: {percentagerare}%, Never: {percentagenever}%""")
    #
    # Stats for pay
    payvar = sum((value - meanpay) ** 2 for value in pay) / (numpay - 1)
    paysd = sum((value - meanpay) ** 2 for value in pay) / numpay
    paysq = math.sqrt(paysd)
    print(f"""Hourly Wage Stats:
    Mean: {meanpay}, Standard Deviation: {paysq}, Variance: {payvar}""")
    #
    # W:L Balance
    wlbal = [int(record['WorkLifeBalance']) for record in records if record['Department'].lower() == department.lower()]
    numwl = len(wlbal)
    worklife = sum(wlbal) / numwl
    print(f"""Work:Life Balance Average:
    {worklife}""")

    # Attrition
    attrition = 0
    for record in records:
        if record['Department'].lower() == department.lower():
            if record['Attrition'] == 'Yes':
                attrition += 1
    attritionyes = (attrition / total) * 100
    print(f"""Attrition Percentage:
    {attritionyes}%""")


# employee id filter
def filter_by_employee_id(dat, employeei):
    reader = csv.DictReader(dat)
    employee_data = [row for row in reader if int(row['EmployeeID']) == employeei]

    print(employee_data)


# role filter
def filter_by_role(dat, role):
    reader = csv.DictReader(dat)
    employee_data = [row for row in reader if row['JobRole'].lower() == role.lower()]

    for val in employee_data:
        print(val)
    print(f"There are {len(employee_data)} Employees")


# department filter
def filter_by_department(dat, dept):
    reader = csv.DictReader(dat)
    employee_data = [row for row in reader if row['Department'].lower() == dept.lower()]

    for val in employee_data:
        print(val)
    print(f"There are {len(employee_data)} Employees")


# dept and role filter
def filter_by_department_role(dat, dept, role):
    reader = csv.DictReader(dat)
    employee_data = [row for row in reader if row['Department'].lower() == dept.lower() and row['JobRole'].lower() == role.lower()]

    for val in employee_data:
        print(val)
    print(f"There are {len(employee_data)} Employees")
