from CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print("Dripping Coffee through filter")
        
    def addCondiments(self) -> None:
        print("Adding Sugar and Milk")