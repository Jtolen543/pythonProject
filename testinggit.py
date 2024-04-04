# class Employee:
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#         pass
#
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Salary: ${self.salary}")
#         pass
#
#     def update_salary(self, new_salary):
#         self.salary = new_salary
#         return self.salary
#
#
# class Manager(Employee):
#     def __init__(self, name, employee_id, salary, department):
#         super().__init__(name, employee_id, salary)
#         self.department = department
#
#     def display_info(self):
#         super().display_info()
#         print(f"Department: {self.department}")
#
#
# employee1 = Employee("John Doe", "E001", 50000)
# manager1 = Manager("Jane Smith", "M001", 80000, "Sales")
#
#
# employee1.display_info()
# print("----")
# manager1.display_info()
# print("----")
#
#
# employee1.update_salary(55000)
# employee1.display_info()


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         pass
#
#     def display_info(self):
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#         pass
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors):
#         super().__init__(make, model, year)
#         self.num_doors = num_doors
#
#     def display_info(self):
#         super().display_info()
#         print(f"Number of Doors: {self.num_doors}")
#
#
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, has_sidecar):
#         super().__init__(make, model, year)
#         self.has_sidecar = has_sidecar
#
#     def display_info(self):
#         super().display_info()
#         print(f"Has Sidecar: {self.has_sidecar}")
#
#
# car1 = Car("Toyota", "Camry", 2022, 4)
# motorcycle1 = Motorcycle("Honda", "CBR", 2021, False)
#
#
# car1.display_info()
# print("----")
# motorcycle1.display_info()

a = [1, 5, 3, 1, 1, 3]
a = set(1, 5, 3)
