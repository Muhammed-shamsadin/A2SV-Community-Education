class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        F = (celsius * 9/5) + 32
        K = celsius + 273.15
        a = []
        a.append(K + 0.00000)
        a.append(F + 0.00000)
        return a

        