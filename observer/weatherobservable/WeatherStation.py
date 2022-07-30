from CurrentConditionsDisplay import CurrentConditionsDisplay
from ForecastDisplay import ForecastDisplay
from Observable import Observable
from StatisticsDisplay import StatisticsDisplay
from WeatherData import WeatherData


class WeatherStation:
    @staticmethod
    def main(*args) -> None:
        weatherData: WeatherData = WeatherData()
        currentConditions: CurrentConditionsDisplay = CurrentConditionsDisplay(weatherData)
        statisticsDisplay: StatisticsDisplay = StatisticsDisplay(weatherData)
        forecastDisplay: ForecastDisplay = ForecastDisplay(weatherData)
            
        weatherData.setMeasurements(80.0, 65.0, 30.4)
        weatherData.setMeasurements(82.0, 70.0, 29.2)
        weatherData.setMeasurements(78.0, 90.0, 29.2)
        
if __name__ == "__main__":
    WeatherStation.main()