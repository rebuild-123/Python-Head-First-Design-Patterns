class Screen:
    description: str
        
    def __init__(self, description: str):
        self.description = description
        
    def up(self) -> None:
        print(f'{self.description} going up')
        
    def down(self) -> None:
        print(f'{self.description} going down')
        
    def toString(self) -> None:
        return self.description