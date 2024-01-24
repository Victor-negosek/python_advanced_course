from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """

    @abstractstaticmethod
    def print_departament():
        """ implement in child class """
    
class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees
    
    def print_departament(self):
        print("Accounting Dempartment: {self.employees}")

class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees
    
    def print_departament(self):
        print(f"Development Dempartment: {self.employees}")
    
class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []
    
    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees
    
    def print_departament(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_departament()
        print(f"Total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(300)

parent_dept = ParentDepartment(50)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_departament()
