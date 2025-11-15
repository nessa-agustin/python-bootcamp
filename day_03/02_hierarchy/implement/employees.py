class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)
    


class Recruiter(Employee):
    def recruit(self):
        self.add_work('Some Recruiter tasks')


class Developer(Employee):
    def code(self):
        self.add_work('Some Development tasks')


class Manager(Employee):
    def manage(self):
        self.add_work('Some Managerial tasks')



emp_manager = Manager('Jack Black', '1234')
emp_manager.add_work('Attend Meetings')
emp_manager.manage()

print(emp_manager.tasks)

