from DisplayElement import DisplayElement
from Observer import Observer
from WeatherData import WeatherData


class StatisticsDisplay(Observer, DisplayElement):
    __maxTemp: float = 0.0
    __minTemp: float = 200
    __tempSum: float = 0.0
    __numReadings: int = 0
    __weatherData: WeatherData
        
    def __init__(self, weatherData: WeatherData):
        self.__weatherData = weatherData
        weatherData.registerObserver(self)
        
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.__tempSum += temp
        self.__numReadings += 1
        
        if temp > self.__maxTemp:
            self.__maxTemp = temp
        
        if temp < self.__minTemp:
            self.__minTemp = temp
            
        self.display()
        
    def display(self) -> None:
        print(f"Avg/Max/Min temperature = {self.__tempSum/self.__numReadings}/{self.__maxTemp}/{self.__minTemp}")