import unittest
from Employee import Employee

class EmployeeTest(unittest.TestCase):
    def test_employee_instance_creates_successfully(self):
        employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
        self.assertTrue(isinstance(employee_x, Employee) )

    def test_full_name_set_correctly(self):
        employee_x = Employee("John", "Doe", "johndoe@gmail.com", "07846563", 30)
        self.assertEqual(employee_x.fullname, "John Doe")



if __name__ == "__main__":
    unittest.main()