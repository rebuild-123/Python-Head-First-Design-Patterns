from DisplayElement import DisplayElement
from Observer import Observer
from WeatherData import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    __currentPressure: float = 29.92
    __lastPressure: float
    __weatherData: WeatherData
        
    def __init__(self, weatherData: WeatherData):
        self.__weatherData = weatherData
        weatherData.registerObserver(self)
        
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.__lastPressure = self.__currentPressure
        self.__currentPressure = pressure
        self.display()
        
    def display(self) -> None:
        print("Forecast: ", end="")
        if self.__currentPressure > self.__lastPressure:
            print("Improving weather on the way!")
        elif self.__currentPressure == self.__lastPressure:
            print("More of the same")
        elif self.__currentPressure < self.__lastPressure:
            print("Watch out for cooler, rainy weather")