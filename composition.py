from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Type

@dataclass
class Commission:
    commission: float = 100
    contracts_landed: float = 0
    @abstractmethod
    def get_payment(self) -> float:
        """computes the commission to be paid out"""
        return self.commission * self.contracts_landed


class Contract(ABC):
    """Represents a contract and a payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""
@dataclass
class Contract_sample(ABC):
    """Represents a contract and a payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""


class Employee(ABC):
    # name: str
    # id: int
    # contract: Type[Contract]
    # commission: Optional[Commission] = None

    def __init__(self,name: str, id: int, contract: Contract, commission: Optional[Commission] = None):
        self.name = name
        self.id = id
        self.contract = contract
        self.commission = commission
    def compute_pay(self) -> float:
        contract_instance = self.contract
        payout = contract_instance.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()

        return payout

@dataclass
class HourlyContract(Contract_sample):
    """Contract type for an employee being paid on an hourly basis."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost

@dataclass
class SalariedContract(Contract):
    """ Contract type for an emplooyee that is paid a fixed monthly salary."""

    monthly_salary: float
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage

@dataclass
class FreelancerContract(Contract):
    """Contract type for an employee being paid on an hourly basis."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self):
        return self.pay_rate * self.hours_worked

def main():

    savvas_contract = HourlyContract(pay_rate=50, hours_worked=100)
    savvas = Employee(name = "Savvas", id = 1, contract = savvas_contract)

    print(f"{savvas.name} with id {savvas.id} and contract {savvas.contract} should be paid {savvas.compute_pay()}")

    georgia_contract = SalariedContract(monthly_salary=10000)
    georgia_commission = Commission(contracts_landed=10, commission=300)
    georgia = Employee(name = "Georgia", id = 2, contract = georgia_contract, commission = georgia_commission)

    print(f"{georgia.name} with id {georgia.id} should be paid {georgia.id} has a commission of {georgia.commission.get_payment()}")


main()
