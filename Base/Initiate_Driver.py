# Starting and closing browser methods
# Instead of adding them in individual test cases these functions are called from here

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
# this code needs to run before all the testcases are run 
from Library import ConfigReader
# init file in library should be created to import it as a module
# this returns the key from the Config file without hardcoding link

# we have created a driver folder which contains both the chrome and firefox web drivers
# This would help in adding a relative path instead of a hardcoded path
def startbrowser():
	global driver
	# Reading the Browser details from the Configuration file
	if ConfigReader.readConfigData('Details','Browser')=="Chrome" :
		PATH = "../Driver/chromedriver.exe"
		driver = Chrome(executable_path=PATH)
	elif ConfigReader.readConfigData('Details','Browser')=="Firefox" :
		PATH = "../Driver/geckodriver.exe"
		driver = Firefox(executable_path=PATH)
	url = ConfigReader.readConfigData('Details','Application_URL')
	# driver.maximize()

	return driver

def closebrowser():
	driver.close()
