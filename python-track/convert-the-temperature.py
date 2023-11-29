class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        fahrenheit = celsius * 1.80  + 32.000
        kelvin = celsius + 273.15
        return [kelvin, fahrenheit]
        