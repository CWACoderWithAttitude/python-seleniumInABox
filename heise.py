import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browsers = ["firefox", "chrome", "MicrosoftEdge"]
browsers = ["chrome", "MicrosoftEdge"]
browsers = ["chrome"]
# browsers = ["MicrosoftEdge"]
versions = ["109.0", "110.0"]

url = "https://www.heise.de"

webdriver_url = "http://selenium-hub:4444/wd/hub"


def getRemoteDriver(browser, version):
    driver = webdriver.Remote(
        command_executor=webdriver_url,
        desired_capabilities={
            "browserName": browser,
            "browserVersion": version,
            "acceptInsecureCerts": True,
        })
    return driver


def runTest(browser, version):
    driver.implicitly_wait(5)
    driver.get(url)
    file = image_file(browser, version)
    print("runTest: {}".format(file))
    try:
        driver.save_screenshot(file)
    except:
        print("runTest > problem saving screenshot - continue anyways...")
    finally:
        print("runTest > finally")
    assert "heise" in driver.title


def image_file(browser, version):
    today = datetime.date.today()
    now = current_time()
    file = f"{today}_{now}-{browser}_{version}.png"
    return file


def current_time():
    t = time.localtime()
    current_time = time.strftime("%H_%M", t)
    return current_time


if __name__ == "__main__":
    driver = None
    try:
        print("heise.py: 1")
        for browser in browsers:
            for version in versions:
                driver = getRemoteDriver(browser, version)
                # image_file(browser)
                runTest(browser, version)
    finally:
        if (driver != None):
            driver.quit()
        else:
            print("heise.py: driver doesn't can' be closed - it's not initialized")
