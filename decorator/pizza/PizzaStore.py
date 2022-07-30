from Cheese import Cheese
from Olives import Olives
from Pizza import Pizza
from ThincrustPizza import ThincrustPizza


class PizzaStore:
    @staticmethod
    def main(*args) -> None:
        pizza: Pizza = ThincrustPizza()
        cheesePizza: Pizza = Cheese(pizza)
        greekPizza: Pizza = Olives(cheesePizza)
            
        print(f'{greekPizza.getDescription()} ${greekPizza.cost()}')
        
if __name__ == '__main__':
    PizzaStore.main()