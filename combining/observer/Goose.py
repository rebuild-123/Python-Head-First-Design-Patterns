class Goose:
    def honk(self) -> None:
        print("Honk")
      
    # toString
    def __str__(self) -> str:
        return "Goose"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)