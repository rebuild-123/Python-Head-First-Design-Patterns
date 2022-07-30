from DisplayElement import DisplayElement
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData


class StatisticsDisplay(Observer, DisplayElement):
    __maxTemp: float = 0.0
    __minTemp: float = 200.0
    __tempSum: float = 0.0
    __numReadings: int = 0
        
    def __init__(self, observable: Observable):
        observable.addObserver(self)
        
    def update(self, observable: Observable, arg: object) -> None:
        if isinstance(observable, WeatherData):
            weatherData: WeatherData = observable
            temp: float = weatherData.getTemperature()
            self.__tempSum += temp
            self.__numReadings += 1
            
            if temp > self.__maxTemp:
                self.__maxTemp = temp
            
            if temp < self.__minTemp:
                self.__minTemp = temp
            
            self.display()
            
    def display(self) -> None:
        print(
            f"Avg/Max/Min temperature = {self.__tempSum/self.__numReadings}/{self.__maxTemp}/{self.__minTemp}"
        )