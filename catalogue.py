from country import Country

class CountryCatalogue: # creates a class called CountryCatalogue
    def __init__(self, countryFile):
      self._countryCat = []
      try: # tries to open the file, splits each line into components, sets the components to variables (name, population, area, continent)
        countryFile = open(countryFile, 'r')
        for record in countryFile:
          components = record.rstrip().split('|')
          if (components[0] == 'Country'): # skips the header in the file
            continue
          name = components[0]
          population = components[2]
          area = components[3]
          continent = components[1]
          self.addCountry(name, population, area, continent)
      except: # error: file does not exist
        print('could not open countries file.')

    def setPopulationOfCountry(self, country, population):
      _country = self.findCountry(country) # looks for object in list so changes are reflected
      _country.setPopulation(population)

    def setAreaOfCountry(self, country, area):
      _country = self.findCountry(country)
      _country.setArea(area)

    def setContinentOfCountry(self, country, continent):
      _country = self.findCountry(country)
      _country.setContinent(continent)

    def findCountry(self, country):
      for _country in self._countryCat:
        if (_country.getName() == country.getName()):
          return _country
      return None

    def addCountry(self, countryName, pop, area, continent):
      # self._data = (countryName, continent, pop, area) do not do this
      tempCountry = Country(countryName, pop, area, continent)

      # use results from finCountry method??? if findCountry == country:
      if (self.findCountry(tempCountry) == None):
        # country does not exist in the list
        self._countryCat.append(tempCountry)
        return True
      else:
        # country exists in the list. do nothing
        return False

    def printCountryCatalogue(self):
      for country in self._countryCat:
        print(country.__repr__())

    def saveCountryCatalogue(self, fileName):
      tempFile = open(fileName, "w")
      records = "Country|Continent|Population|Area\n"
      self._countryCat.sort(key=lambda country: country.getName(), reverse = False)
      for country in self._countryCat:
        record = (country.getName() + "|" + country.getContinent() + "|"
        + str(country.getPopulation()) + "|" + str(country.getArea()))
        records += record + '\n'

      try:
        tempFile.write(records)
        tempFile.close()
        return len(self._countryCat)
      except:
        return -1
