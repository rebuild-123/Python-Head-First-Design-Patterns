class PopcornPopper:
    description: str
        
    def __init__(self, description: str):
        self.description = description
        
    def on(self) -> None:
        print(f'{self.description} on')
        
    def off(self) -> None:
        print(f'{self.description} off')
        
    def pop(self) -> None:
        print(f'{self.description} popping popcorn!')
        
    def toString(self) -> None:
        return self.description