from DisplayElement import DisplayElement
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    __currentPressure: float = 29.92
    __lastPressure: float
        
    def __init__(self, observable: Observable):
        observable.addObserver(self)
        
    def update(self, observable: Observable, arg: object) -> None:
        if isinstance(observable, WeatherData):
            weatherData: WeatherData = observable
            self.__lastPressure = self.__currentPressure
            self.__currentPressure = weatherData.getPressure()
            self.display()
            
    def display(self) -> None:
        print("Forecast: ", end="")
        if self.__currentPressure > self.__lastPressure:
            print("Improving weather on the way!")
        elif self.__currentPressure == self.__lastPressure:
            print("More of the same")
        elif self.__currentPressure < self.__lastPressure:
            print("Watch out for cooler, rainy weather")