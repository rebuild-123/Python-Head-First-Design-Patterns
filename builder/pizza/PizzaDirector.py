from MeatLoversPizzaBuilder import MeatLoversPizzaBuilder
from Pizza import Pizza
from PizzaBuilder import PizzaBuilder
from VeggieLoversPizzaBuilder import VeggieLoversPizzaBuilder


class StringBuilder:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)
    
    def __len__(self) -> int:
        return sum(map(len, self.ls))
    
    def __setitem__(self, idx, value) -> None:
        self.ls[idx] = value

class PizzaDirector:
    # Fluent Interface pattern (return the builder each time so we can string the calls together)
    # Builder pattern (we have two different builders so the "same construction process can create
    #   different representations").
    # Builder is a solution to the telescoping constructor anti-pattern, where we have multiple,
    #   complex constructor methods with various args for all various combinations of options
    #   in construction options. 
    # 
    # in this example main() is the construct() method
    @staticmethod
    def main(*args) -> None:
        # Could hand builders to PizzaStore which would take the customer's order,
        #   and call appropriate methods for each topping, then call the
        #   pizza methods to prep and return to the customer. 
        veggieBuilder: PizzaBuilder = VeggieLoversPizzaBuilder()
        # The PizzaDirector calls the methods in the correct order to
        # build a veggiePizza. 
        veggie: Pizza = veggieBuilder.addSauce().addCheese().addOlives().addTomatoes().addSausage().build()
        veggie.prepare()
        veggie.bake()
        veggie.cut()
        veggie.box()
        print(veggie)
        
        meatBuilder: PizzaBuilder = MeatLoversPizzaBuilder()
        # The PizzaDirector calls the methods in the correct order to build
        # a meat lovers Pizza
        meat: Pizza = meatBuilder.addSauce().addTomatoes().addCheese().addSausage().addPepperoni().build()
        meat.prepare()
        meat.bake()
        meat.cut()
        meat.box()
        print(meat)
            
        # There is some difference of opinion about StringBuilder and whether it's using
        # the Builder pattern or not. Some say yes, some say no.
        # StringBuilder does not provide an abstract API with multiple subclasses for
        #   creating different representations (variations). So, strictly, no, it doesn't 
        #   use the Builder Pattern, but rather the Fluent Interface Pattern.
        sb: StringBuilder = StringBuilder()
        sb.append("\nTesting String Builder\n")
        sb.append(str(veggie))
        sb[0] = "\n==== "
        print(f"Length of the String Builder: {len(sb)}")
        print(f"Result of the String Builder: {sb.toString()}")
        
        sb2 = StringBuilder()
        sb2.append("\nTesting String Builder\n")
        sb2.append(str(meat))
        sb2[0] = "==== "
        sb2: str = sb2.toString()
        print(sb2)
            
        # Builder has similarities to Abstract Factory.
        # But difference is that Builder provides a step by step API for building a product;
        #   the client is responsible for calling the steps, and those can vary in order, etc.
        #   With Builder, the client must have more knowledge of the details of the product being built.
        # Product implementations can be swapped for others; clients don't change because the use the abstract API.
        
if __name__ == "__main__":
    PizzaDirector.main()