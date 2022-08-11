class Roof:
    name: str
    material: str
        
    def __init__(self, material: str):
        self.name = f"Roof made out of {material}"
        
    def setName(self, name: str) -> None:
        self.name = name
        
    # toString
    def __str__(self) -> str:
        return self.name
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)