def employee_id(employeeid):
    csvfile = "nurse_attrition.csv"
    df = pd.read_csv(csvfile)
    employee_record = df[df['EmployeeID'] == employeeid]
    pd.set_option('display.max.rows', None)
    pd.set_option('display.max.columns', None)
    print(employee_record)


def deptid(departmentid):
    csvfile = "nurse_attrition.csv"
    df = pd.read_csv(csvfile)
    department_rec = df[df['Department'].str.lower() == departmentid.lower()]
    pd.set_option('display.max.rows', None)
    pd.set_option('display.max.columns', None)
    print(department_rec)
    print(f"there are {len(department_rec)}")


def jobrole(role):
    csvfile = "nurse_attrition.csv"
    df = pd.read_csv(csvfile)
    job_role = df[df['JobRole'].str.lower() == role.lower()]
    pd.set_option('display.max.rows', None)
    pd.set_option('display.max.columns', None)
    print(job_role)


def combined(department, role):
    csvfile = "nurse_attrition.csv"
    df = pd.read_csv(csvfile)
    conditions = (df['Department'].str.lower() == department.lower()) & \
                 (df['JobRole'].str.lower() == role.lower())
    combine = df[conditions]
    pd.set_option('display.max.rows', None)
    pd.set_option('display.max.columns', None)
    print(combine)

    csvfile = "nurse_attrition.csv"
    df = pd.read_csv(csvfile)
    unique_depts = df['Department'].unique()
    return unique_depts


def uniqued(unique_depts):
    print("Department Names:")
    for dept in unique_depts:
        print(dept)