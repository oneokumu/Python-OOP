
"""
 To calculate the total payroll for a company using the Employee class
 defined in the oop3.py file of the repository, you can create a Payroll class
 that keeps track of employee instances and computes their total salaries.

 First; Define the Employee Class: Ensuring that the Employee class has an attribute
  for salary and a method to retrieve it.

  Then; Create the Payroll Class: This class will maintain a list of Employee objects
  and provide a method to calculate the total payroll.

  Then Add Employees: When creating employee objects, you can add them to the payroll class.
  Lastly; Calculating Total Payroll: When you need to find the total payroll, the payroll class
  will loop through its list of employees, retrieving each employee's salary and calculating the total.

"""

#Below is the code

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        total = sum(employee.get_salary() for employee in self.employees)
        return total


# Example in usage
if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    emp3 = Employee("Charlie", 70000)

    payroll = Payroll()
    payroll.add_employee(emp1)
    payroll.add_employee(emp2)
    payroll.add_employee(emp3)

    print("Total Payroll: $", payroll.total_payroll())
