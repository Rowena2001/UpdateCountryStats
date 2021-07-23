from catalogue import CountryCatalogue
from country import Country


def processUpdates(cntryFileName, updatesFileName):
    # SECTION: GET FILES
    # get countries file
    countryFile = stubbornGetFile(cntryFileName)
    if (countryFile == None):
        return False
    print('country file found\nRetrieving updates file...')

    # get updates file
    updatesFile = stubbornGetFile(updatesFileName)
    if (updatesFile == None):
        return False
    print('updates file found.')

    # SECTION: GET UPDATES FROM FILE
    # get updates information
    # format: {'countryName': {'P': [1,2,3], 'A': [], 'C': []} }
    updatesDict = formatFileToDictionary(updatesFile)

    # SECTION: DEFINE CATALOGUE
    catalogue = CountryCatalogue(countryFile.name)

    # SECTION: UPDATE CATALOGUE
    # iterate through each update in updatesDict
    for countryName, updates in updatesDict.items():
        country = catalogue.findCountry(Country(countryName))
        if (country == None):
            country = newCountry(countryName, updates)
            catalogue.addCountry(country.getName(), country.getPopulation(), country.getArea(), country.getContinent())
        for header, updateList in updates.items():  # {'P': [1,2,3]} header: 'P', updateList: [1,2,3]
            if len(updates.keys()) <= 3: # only allows up to 3 updates
                if (header == 'P'):
                    catalogue.setPopulationOfCountry(country, updateList)
                elif (header == 'A'):
                    catalogue.setAreaOfCountry(country, updateList)
                elif (header == 'C'):
                    catalogue.setContinentOfCountry(country, updateList)
                else:
                    raise Exception(countryName, "invalid update format") # raises exception if the header is an invalid format

    # SECTION: SAVE AND OUTPUT TO FILE
    catalogue.saveCountryCatalogue('output.txt')
    return True


def newCountry(name, updates):
    country = Country(name)
    for header, updateList in updates.items():
        if (header == 'P'):
            country.setPopulation(updateList)
        elif (header == 'A'):
            country.setArea(updateList)
        elif (header == 'C'):
            country.setContinent(updateList)
        else:
            raise Exception(country, "invalid update format")  # raises exception if the header is an invalid format
    return country


def safeOpen(fileName):
    try:
        return open(fileName, 'r')
    except:
        return None


# returns a file if one is found that exists
# or returns None if user gives up
def stubbornGetFile(fileName):
    tempFile = safeOpen(fileName)
    while (tempFile == None):  # keep asking for file until user gives up or one is found
        choice = input('File Not Found. Would you like to quit? (Y/N): ')
        newFileName = ''
        if (choice == 'N'):
            newFileName = input('Enter a file name: ')
        else:  # user gives up and quits
            errFile = open('output.txt', 'w')
            errFile.write('Update Unsuccessful\n')
            errFile.close()
            return None  # return no file meaning user has quit
        tempFile = safeOpen(newFileName, 'r')
    return tempFile


def formatFileToDictionary(updatesFile):
    allUpdates = {}
    for record in updatesFile:
        listOfUpdates = record.split(';')
        # ['Brazil', 'P=1,2,3',]
        countryName = listOfUpdates.pop(0)

        allUpdates[countryName] = {}  # create empty dict for all updates of given country
        for update in listOfUpdates:
            update = update.rstrip()
            header = update[0:1]  # first character of string (P, A or C)
            update = update[2:]  # start at 3rd char to end of string
            # {'country': {'P': [1,2], 'A': [0,1]}}
            # allUpdates['Braz']['P'] = [1,2,3]
            allUpdates[countryName][header] = update

    # print(allUpdates)
    return allUpdates
