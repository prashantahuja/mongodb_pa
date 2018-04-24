def insert():
    try:
        employeeid = raw_input("Enter Employee Id:")
        employeename = raw_input("Enter employee Name")
        db.employees.insert_one(
            {
                "id": employeeid,
                "name": employeename
            }
        )
    except Exception as ex:
        print("exception")


def read():
    try:
        empCol = db.Employees.find()
        print("All data from EmployeeData Database")
        for emp in empCol:
            print(emp)

    except exception as exr:
        print("exception")


