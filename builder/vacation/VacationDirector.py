from CityVacationBuilder import CityVacationBuilder
from OutdoorsVacationBuilder import OutdoorsVacationBuilder
from Vacation import Vacation
from VacationBuilder import VacationBuilder


class VacationDirector:
    @staticmethod
    def main(*args) -> None:
        outdoorsyVacationBuilder: VacationBuilder = OutdoorsVacationBuilder()
        outdoorsyVacation: Vacation = outdoorsyVacationBuilder\
            .addAccommodation_3("Two person tent", 2020, 7, 1, 5, 34)\
            .addEvent("Beach")\
            .addAccommodation_2("Two person tent")\
            .addEvent("Mountains")\
            .getVacation()
        print(outdoorsyVacation)
        
        cityVacationBuilder: VacationBuilder = CityVacationBuilder()
        cityVacation: Vacation = cityVacationBuilder\
            .addAccommodation_3("Grand Facadian", 2020, 8, 1, 5, 0)\
            .addAccommodation_3("Hotel Commander", 2020, 8, 6, 2, 0)\
            .addEvent("Cirque du Soleil")\
            .getVacation()
        print(cityVacation)
        
if __name__ == "__main__":
    VacationDirector.main()