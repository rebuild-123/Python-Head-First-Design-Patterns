from typing import List


class Pizza:
    name: str
    toppings: List[str]
        
    def addToppings(self, toppings: List[str]) -> None:
        self.toppings = toppings
        
    def prepare(self) -> None:
        print(f"Prepare {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f"   {topping}")
            
    def bake(self) -> None:
        print("Bake for 25 minutes at 350")
        
    def cut(self) -> None:
        print("Cut the pizza into diagonal slices")
        
    def box(self) -> None:
        print("Place pizza in official PizzaStore box")
        
    def setName(self, name: str) -> None:
        self.name = name
        
    # toString # Not in the authors' code.
    def __str__(self) -> str:
        ls = []
        ls.append(f'{self.name} with [')
        for idx,topping in enumerate(self.toppings):
            if idx < len(self.toppings) - 1: 
                ls.append(f'{topping}, ')
            else:
                ls.append(f'{topping}]')
        return ''.join(ls)
    # Not in the authors' code.
    def __repr__(self) -> str:
        return str(self)