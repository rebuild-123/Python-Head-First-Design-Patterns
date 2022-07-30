from DisplayElement import DisplayElement
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    observable: Observable
    __temperature: float 
    __humidity: float
        
    def __init__(self, observable: Observable):
        self.observable = observable
        self.observable.addObserver(self)
        
    def update(self, obs: Observable, arg: object):
        if isinstance(obs, WeatherData):
            weatherData: WeatherData = obs
            self.__temperature = weatherData.getTemperature()
            self.__humidity = weatherData.getHumidity()
            self.display()
            
    def display(self) -> None:
        print(f"Current conditions: {self.__temperature}F degrees and {self.__humidity}% humidity")