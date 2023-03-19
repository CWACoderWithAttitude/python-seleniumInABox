import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browsers = ["firefox", "chrome", "MicrosoftEdge"]

url = "https://www.heise.de"

webdriver_url = "http://selenium-hub:4444/wd/hub"


def getRemoteDriver(browser):
    driver = webdriver.Remote(
        command_executor=webdriver_url,
        desired_capabilities={
            "browserName": browser,
            "acceptInsecureCerts": True
        })
    return driver


def runTest(browser):
    driver.implicitly_wait(5)
    driver.get(url)
    file =image_file(browser)
    print("runTest: {}".format(file))
    try:
        driver.save_screenshot(file)
    except:
        print("runTest > problem saving screenshot - continue anyways...")
    finally:
        print("runTest > finally")
    assert "heise" in driver.title
    image_file(browser)

def image_file(browser):
    today = datetime.date.today()
    file = "{}-{}.png".format(today, browser)
    return file

if __name__ == "__main__":
    driver = None
    try:
        print("heise.py: 1")
        for browser in browsers:
            driver = getRemoteDriver(browser)
            #image_file(browser)
            runTest(browser)
    finally:
        if (driver != None):
          driver.quit()
        else:
          print("heise.py: driver doesn't can' be closed - it's not initialized")
