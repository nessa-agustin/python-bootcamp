class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.var = name + id
        self.tasks = []
        print(f'Employee {name} created with id {id}')

    def work(self, task):
        print(f'{self.name} Working {task}....')
        self.tasks.append(task)


employee = Employee('Richard', '1234')
# employee.name = 'Richard'
# employee.id = '1234'
# print(employee.id, employee.name)
employee.work('Create slides')

employee1 = Employee('Lucy', '4567')
# employee1.name = 'Lucy'
# employee1.id = '4567'
# print(employee1.id, employee1.name)
employee1.work('Do Research')