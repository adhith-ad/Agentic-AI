from backend.services.database_service import get_employees_by_experience

employees = get_employees_by_experience(5)

for emp in employees:
    print(emp)