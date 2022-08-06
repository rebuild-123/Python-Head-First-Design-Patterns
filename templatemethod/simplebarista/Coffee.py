class Coffee:
    
    def prepareRecipe(self) -> None:
        self.boilWater()
        self.brewCoffeeGrinds()
        self.pourInCup()
        self.addSugarAndMilk()
    
    def boilWater(self) -> None:
        print("Boiling water")
        
    def brewCoffeeGrinds(self) -> None:
        print("Dripping Coffee through filter")
    
    def pourInCup(self) -> None:
        print("Pouring into cup")
        
    def addSugarAndMilk(self) -> None:
        print("Adding Sugar and Milk")