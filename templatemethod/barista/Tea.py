from CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print("Steeping the tea")
    def addCondiments(self) -> None:
        print("Adding Lemon")