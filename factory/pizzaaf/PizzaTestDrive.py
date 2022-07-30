from ChicagoPizzaStore import ChicagoPizzaStore
from NYPizzaStore import NYPizzaStore
from Pizza import Pizza
from PizzaStore import PizzaStore


class PizzaTestDrive:
    @staticmethod
    def main(*args):
        nyStore: PizzaStore = NYPizzaStore()
        chicagoStore: PizzaStore = ChicagoPizzaStore()
 
        pizza: Pizza = nyStore.orderPizza("cheese")
        print(f"Ethan ordered a {pizza.toString()}\n")
        
        pizza = chicagoStore.orderPizza("cheese")
        print(f"Joel ordered a {pizza.toString()}\n")

        pizza = nyStore.orderPizza("clam")
        print(f"Ethan ordered a {pizza.toString()}\n")
 
        pizza = chicagoStore.orderPizza("clam")
        print(f"Joel ordered a {pizza.toString()}\n")

        pizza = nyStore.orderPizza("pepperoni")
        print(f"Ethan ordered a {pizza.toString()}\n")
 
        pizza = chicagoStore.orderPizza("pepperoni")
        print(f"Joel ordered a {pizza.toString()}\n")

        pizza = nyStore.orderPizza("veggie")
        print(f"Ethan ordered a {pizza.toString()}\n")
 
        pizza = chicagoStore.orderPizza("veggie")
        print(f"Joel ordered a {pizza.toString()}\n")
        
if __name__ == "__main__":
    PizzaTestDrive.main()