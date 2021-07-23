class Country: # creates a class called Country
    def __init__(self, name="", population=0, area=0, continent=""): # initializes the attributes name, population, area and continent to each instance of Country
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._population

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def setPopulation(self, population):
        self._population = population

    def setArea(self, area):
        self._area = area

    def setContinent(self, continent):
        self._continent = continent

    def __repr__(self):
        return self._name + " (Population: " + str(self._population) + ", Size: " + str(self._area) + ") in " + self._continent
