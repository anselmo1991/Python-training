class Person:
    def __init__(self, name, age, address=None, gender=None):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender


class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.company = None  # начинаем безработными
        self.balance = 0

    def hire(self, company):
        if not self.company:
            self.company = company
            company.add_employee(self)

    def fire(self):
        if self.company:
            self.company.remove_employee(self)
            self.company = None

    def work(self):
        pass

    def receive_salary(self, salary):
        self.balance += salary

    def celebrate_holiday(self):
        self.receive_salary(5)


class Engineer(Employee):
    def work(self):
        if self.company and self.company.money >= 10:
            self.company.pay_employee(self, 10)


class Manager(Employee):
    def work(self):
        if self.company and self.company.money >= 12:
            self.company.pay_employee(self, 12)


class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []
        self.money = 1000

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def pay_employee(self, employee, salary):
        if employee in self.employees and self.money >= salary:
            self.money -= salary
            employee.receive_salary(salary)
        else:
            self.bankrupt()

    def celebrate_holiday(self):
        for employee in self.employees:
            employee.celebrate_holiday()

    def bankrupt(self):
        print(f"{self.name} has gone bankrupt. All employees are now unemployed.")
        for employee in self.employees:
            employee.fire()
        self.employees = []


if __name__ == "__main__":
    company = Company("Tenzor", "123 Street")

    engineer1 = Engineer("Alice", 30)
    engineer2 = Engineer("Bob", 35)

    manager1 = Manager("Charlie", 40)

    engineer1.hire(company)
    engineer2.hire(company)
    manager1.hire(company)

    print("Company money before work:", company.money)

    engineer1.work()
    engineer2.work()
    manager1.work()

    print("Company money after work:", company.money)
    print("Engineer 1 balance:", engineer1.balance)
    print("Engineer 2 balance:", engineer2.balance)
    print("Manager 1 balance:", manager1.balance)

    company.celebrate_holiday()

    print("Engineer 1 balance after holiday:", engineer1.balance)
    print("Engineer 2 balance after holiday:", engineer2.balance)
    print("Manager 1 balance after holiday:", manager1.balance)

    company.bankrupt()
