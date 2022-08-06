class Duck:
    name: str
    weight: int
        
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        
    # toString
    def __str__(self) -> str: 
        return f"{self.name} weights {self.weight}"
    
    # compareTo
    def __lt__(self, otherDuck) -> bool:
        return self.weight < otherDuck.weight
    
    # compareTo
    def __le__(self, otherDuck) -> bool:
        return self.weight <= otherDuck.weight
    
    # compareTo
    def __eq__(self, otherDuck) -> bool:
        return self.weight == otherDuck.weight
    
    # compareTo
    def __gt__(self, otherDuck) -> bool:
        return self.weight > otherDuck.weight
    
    # compareTo
    def __ge__(self, otherDuck) -> bool:
        return self.weight >= otherDuck.weight