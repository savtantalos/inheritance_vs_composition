class ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }
    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError("invalid role_id")
        return role_type()
    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")


class ManagerRole:
    def perform_duties(self, hours):
        return f"Manager {hours} hours per week"


class SecretaryRole:
    def perform_duties(self, hours):
        return f"Secretary {hours} hours per week"


class SalesRole:
    def perform_duties(self, hours):
        return f"Sales {hours} hours per week"


class FactoryRole:
    def perform_duties(self, hours):
        return f"Factory {hours} hours per week"
