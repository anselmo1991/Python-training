import pytest

@pytest.fixture
def company_instance(request):
    company = Company("Test Company", "456 Avenue")
    engineer1 = Engineer("Alice", 30)
    engineer2 = Engineer("Bob", 35)
    manager1 = Manager("Charlie", 40)
    engineer1.hire(company)
    engineer2.hire(company)
    manager1.hire(company)

    def cleanup():
        company.bankrupt()

    request.addfinalizer(cleanup)

    return company

@pytest.mark.parametrize("employee_class", [Engineer, Manager])
def test_work(company_instance, employee_class):
    company_instance.work()
    if employee_class == Engineer:
        assert company_instance.employees[0].balance == 10
        assert company_instance.employees[1].balance == 10
    elif employee_class == Manager:
        assert company_instance.employees[2].balance == 12

def test_celebrate_holiday(company_instance):
    company_instance.celebrate_holiday()
    for employee in company_instance.employees:
        assert employee.balance == 5

def test_bankrupt(company_instance):
    company_instance.bankrupt()
    assert len(company_instance.employees) == 0
    for employee in company_instance.employees:
        assert employee.company is None
