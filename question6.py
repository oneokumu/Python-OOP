# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for a generic employee.")

# Subclass
class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for a manager, including bonuses and allowances.")

# Demonstration of overridden behavior
employee = Employee()
manager = Manager()

# Call calculate_salary on both instances
employee.calculate_salary()
manager.calculate_salary()
