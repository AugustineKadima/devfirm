import unittest
from Employee import Employee

class EmployeeTest(unittest.TestCase):
    def test_employee_instance_creates_successfully(self):
        employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
        self.assertTrue(isinstance(employee_x, Employee) )

    def test_full_name_set_correctly(self):
        employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
        self.assertEqual(employee_x.fullname, "John Doe")

    def test_employee_is_saved_successfully(self):
        employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
        employee_x.save()
        employee_x = Employee("Kelvin", "Hart", "kelvinhart@gmail.com", "07854546", 70)
        employee_x.save()
        self.assertEqual(len(Employee.employee_list), 2)




if __name__ == "__main__":
    unittest.main()