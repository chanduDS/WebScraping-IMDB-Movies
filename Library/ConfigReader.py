from configparser import ConfigParser
# readConfigData takes the section and key details and reads the corresponding data from configuration file
def readConfigData(section, key):
    config = ConfigParser()
    config.read("../ConfigurationFiles/Config.ini")
    return config.get(section, key)

# Instead of hardcoding the urls we are reading the urls from here
def read_urls(genre,val):
    url="https://www.imdb.com/search/title/?genres="+genre+"&start="+str(val)
    return url
# print(readConfigData('Details','Application_URL'))
