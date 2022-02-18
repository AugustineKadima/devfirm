
class Employee:

    employee_list = []

    def __init__(self, first_name, last_name, email, phone_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.age = age

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    
    def save(self):
        self.employee_list.append(self)

    def all_employees(self):
        return self.employee_list


# employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
# employee_x.save()
# employee_y = Employee("Kevin", "Hart", "kevinhart@gmail.com", "07968464", 60)
# employee_y.save()

# print(Employee.employee_list[1].__dict__)