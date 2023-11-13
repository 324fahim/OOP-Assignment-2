 class Employee:
  def __init__(self, name, employee_id, salary):
      self.name = name
      self.employee_id = employee_id
      self.salary = salary

  def display_details(self):
      print(f"Employee Name: {self.name}")
      print(f"Employee ID: {self.employee_id}")
      print(f"Salary: ${self.salary:.2f}\n")

# Creating instances for different employees
employee1 = Employee("John Doe", 1001, 50000)
employee2 = Employee("Jane Smith", 1002, 60000)
employee3 = Employee("David Johnson", 1003, 55000)

# Displaying employee details
employee1.display_details()
employee2.display_details()
employee3.display_details()
 
