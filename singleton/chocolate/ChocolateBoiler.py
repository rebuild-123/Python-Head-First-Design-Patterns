class ChocolateBoiler:
    __empty: bool
    __boiled: bool
    __uniqueInstance = None
        
    def __init__(self):
        self.__empty = True
        self.__boiled = False
        
    @staticmethod
    def getInstance():
        if ChocolateBoiler.__uniqueInstance == None:
            print("Creating unique instance of Chocolate Boiler")
            ChocolateBoiler.__uniqueInstance = ChocolateBoiler()
        print("Returning instance of Chocolate Boiler")
        return ChocolateBoiler.__uniqueInstance
    
    def fill(self) -> None:
        if self.isEmpty():
            self.__empty = False
            self.__boiled = False
            # fill the boiler with a milk/chocolate mixture
    
    def drain(self) -> None:
        if not self.isEmpty() and self.isBoiled():
            # drain the boiled milk and chocolate
            self.__empty = True
            
    def boil(self) -> None:
        if not self.isEmpty() and not self.isBoiled():
            # bring the contents to a boil
            self.__boiled = True
            
    def isEmpty(self) -> bool:
        return self.__empty
    
    def isBoiled(self) -> bool:
        return self.__boiled