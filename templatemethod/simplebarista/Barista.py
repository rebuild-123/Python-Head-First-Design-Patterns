from Coffee import Coffee
from Tea import Tea


class Barista:
    
    @staticmethod
    def main(*args) -> None:
        tea: Tea = Tea()
        coffee: Coffee = Coffee()
        print("Making tea...")
        tea.prepareRecipe()
        print("Making coffee...")
        coffee.prepareRecipe()
        
if __name__ == "__main__":
    Barista.main()