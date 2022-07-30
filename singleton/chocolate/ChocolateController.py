from ChocolateBoiler import ChocolateBoiler


class ChocolateController:
    @staticmethod
    def main(*args) -> None:
        boiler: ChocolateBoiler = ChocolateBoiler.getInstance()
        boiler.fill()
        boiler.boil()
        boiler.drain()
        
        # will return the existing instance
        boiler2: ChocolateBoiler = ChocolateBoiler.getInstance()
            
if __name__ == "__main__":
    ChocolateController.main()