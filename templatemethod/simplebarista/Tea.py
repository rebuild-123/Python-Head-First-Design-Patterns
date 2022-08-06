class Tea:
    
    def prepareRecipe(self) -> None:
        self.boilWater()
        self.steepTeaBag()
        self.pourInCup()
        self.addLemon()
    
    def boilWater(self) -> None:
        print("Boiling water")
        
    def steepTeaBag(self) -> None:
        print("Steeping the tea")
        
    def addLemon(self) -> None:
        print("Adding Lemon")
    
    def pourInCup(self) -> None:
        print("Pouring into cup")