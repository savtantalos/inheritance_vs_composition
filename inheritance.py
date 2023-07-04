from abc import   ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass

class Employee(ABC):

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        "Compute how much employee should be paid"
        ...


@dataclass
class HourlyEmployee(Employee):

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate *self.hours_worked + self.employer_cost

@dataclass
class SalariedEmployee(Employee):

    monthly_salary: float
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked

@dataclass
class SalariedCommissionEmployee(SalariedEmployee):
    """Salaried employee that's paid based on a fixed monthly salary and commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return (
            super().compute_pay()
            + self.commission * self.contracts_landed
        )
@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee that's paid based on number of worked hours and that gets a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that's paid based on number of worked hours and that gets a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


def main() -> None:
    savvas = HourlyEmployee("Savvas", id = 1, pay_rate=30, hours_worked=160)
    print(f"{savvas.name} should be paid {savvas.compute_pay()}")

    georgia = HourlyEmployeeWithCommission("Georgia", id=2, pay_rate = 20, hours_worked = 41\
                                           , contracts_landed = 2)
    print(f"{georgia.name} should be paid {georgia.compute_pay()}")

if __name__ == "__main__":
    main()
