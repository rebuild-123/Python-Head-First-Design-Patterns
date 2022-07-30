from typing import List

from Observer import Observer
from Subject import Subject


class WeatherData(Subject):
    __observers: List[Observer]
    __temperature: float
    __humidity: float
    __pressure: float
        
    def __init__(self):
        self.__observers: List[Observer] = []
        
    def registerObserver(self, o: Observer) -> None:
        self.__observers.append(o)
        
    def removeObserver(self, o: Observer) -> None:
        self.__observers.remove(o)
        
    def notifyObservers(self) -> None:
        for observer in self.__observers:
            observer.update(self.__temperature, self.__humidity, self.__pressure)
            
    def measurementsChanged(self) -> None:
        self.notifyObservers()
        
    def setMeasurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()
        
    def getTemperatur(self) -> float:
        return self.__temperature
    
    def getHumidity(self) -> float:
        return self.__humidity
    
    def getPressure(self) -> float:
        return self.__pressure