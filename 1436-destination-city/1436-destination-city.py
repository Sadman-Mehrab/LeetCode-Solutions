class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        allCities = set()
        startingCities = set()
        for path in paths:
            allCities.add(path[0])
            startingCities.add(path[0])
            allCities.add(path[1])
        for city in allCities:
            if city not in startingCities:
                return city
        return ""