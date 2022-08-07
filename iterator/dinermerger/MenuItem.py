class MenuItem:
    name: str
    description: str
    vegetarian: bool
    price: float
        
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
        
    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def getPrice(self) -> float:
        return self.price
    
    def isVegetarian(self) -> bool:
        return self.vegetarian
    
    # toString
    def __str__(self) -> str:
        return f'{self.name}, ${self.price}\n   {self.description}'