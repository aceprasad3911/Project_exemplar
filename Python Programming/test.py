import csv
data = []


def load_data():
    with open("nurse_attrition.csv") as csv_file:
        for record in csv_file:
            data.append(record)


def filter_by_employee_id(dat, employeei):
    reader = csv.DictReader(dat)
    employee_data = [row for row in reader if int(row['EmployeeID']) == employeei]

    print(employee_data)

load_data()

employee_id_input = int(input("Enter the employee ID: "))
if employee_id_input == 1:
    empid = int(input("hello"))

    filter_by_employee_id(data, empid)




# def gendercounts(dat, department):
#     userdept = department.lower()
#     gender = {'Male': 0, 'Female': 0}
#     for record in dat:
#         if record['Department'] == userdept:
#             gender[record['Gender']] += 1
#     print(gender)
#     return gender
#    print(f"Department: {department}")

# Below are samples of code that are not 100% suitable for my work:
#
#  elif choice == 8:
#       departmeme()
#    elif choice == 9:
#        employee_id_input = int(input("Enter the employee ID: "))
#        filter_by_employee_id(data, employee_id_input)
#    elif choice == 10:
#       filter_by_role(data, role)

# def departmeme():
#     with open('nurse_attrition.csv') as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader)
#         for row in reader:
#             print(row[5])
