from Coffee import Coffee
from CoffeeWithHook import CoffeeWithHook
from Tea import Tea
from TeaWithHook import TeaWithHook


class BeverageTestDrive:
    @staticmethod
    def main(*args):
        tea: Tea = Tea()
        coffee: Coffee = Coffee()
            
        print("\nMaking tea...")
        tea.prepareRecipe()
        
        print("\nMaking coffee...")
        coffee.prepareRecipe()
        
        teaHook: TeaWithHook = TeaWithHook()
        coffeeHook: CoffeeWithHook = CoffeeWithHook()
            
        print("\nMaking tea...")
        teaHook.prepareRecipe()
        
        print("\nMaking coffee...")
        coffeeHook.prepareRecipe()
        
if __name__ == "__main__":
    BeverageTestDrive.main()