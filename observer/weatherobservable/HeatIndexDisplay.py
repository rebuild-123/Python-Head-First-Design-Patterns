from DisplayElement import DisplayElement
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData


class HeatIndexDisplay(Observer, DisplayElement):
    heatIndex: float = 0.0
        
    def __init__(self, observable: Observable):
        observable.addObserver(self)
        
    def update(self, observable: Observable, arg: object) -> None:
        if isinstance(observable, WeatherData):
            weatherData: WeatherData = observable
            t: float = weatherData.getTemperature()
            rh: float = weatherData.getHumidity()
            self.heatIndex = float(
                (16.923 + (0.185212 * t)) + 
                (5.37941 * rh) - 
                (0.100254 * t * rh) + 
                (0.00941695 * (t * t)) + 
                (0.00728898 * (rh * rh)) + 
                (0.000345372 * (t * t * rh)) - 
                (0.000814971 * (t * rh * rh)) +
                (0.0000102102 * (t * t * rh * rh)) - 
                (0.000038646 * (t * t * t)) + 
                (0.0000291583 * (rh * rh * rh)) +
                (0.00000142721 * (t * t * t * rh)) + 
                (0.000000197483 * (t * rh * rh * rh)) - 
                (0.0000000218429 * (t * t * t * rh * rh)) +
                (0.000000000843296 * (t * t * rh * rh * rh)) -
                (0.0000000000481975 * (t * t * t * rh * rh * rh))
            )
            self.display()
            
    def display(self) -> None:
        print(f"Heat index is {self.heatIndex}")