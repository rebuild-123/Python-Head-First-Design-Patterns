from abc import ABC, abstractmethod


class CaffeineBeverageWithHook(ABC):
    
    def prepareRecipe(self) -> None:
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments(): 
            self.addCondiments()
        
    @abstractmethod
    def brew(self) -> None:
        pass
    
    @abstractmethod
    def addCondiments(self) -> None:
        pass
    
    def boilWater(self) -> None:
        print("Boiling water")
        
    def pourInCup(self) -> None:
        print("Pouring into cup")
        
    def customerWantsCondiments(self) -> bool:
        return True