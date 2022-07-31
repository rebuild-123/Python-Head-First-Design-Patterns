from Cook import Cook
from Customer import Customer
from Waitress import Waitress


class Diner:
    @staticmethod
    def main(*args) -> None:
        cook: Cook = Cook()
        waitress: Waitress = Waitress()
        customer: Customer = Customer(waitress, cook)
        customer.createOrder()
        customer.hungry()
        
if __name__ == "__main__":
    Diner.main()