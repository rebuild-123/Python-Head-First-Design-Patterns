from Pizza import Pizza
from PizzaStore import PizzaStore
from SimplePizzaFactory import SimplePizzaFactory


class PizzaTestDrive:
    @staticmethod
    def main(*args) -> None:
        factory: SimplePizzaFactory = SimplePizzaFactory()
        store: PizzaStore = PizzaStore(factory)
        
        pizza: Pizza = store.orderPizza("cheese")
        print(f"We ordered a {pizza.getName()}\n")
        print(pizza.toString())
        
        pizza = store.orderPizza('veggie')
        print(f"We ordered a {pizza.getName()}\n")
        print(pizza.toString())
        
if __name__ == "__main__":
    PizzaTestDrive.main()