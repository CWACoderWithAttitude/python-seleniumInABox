from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


browser = "firefox"

url = "https://www.heise.de"
webdriver_url = "http://selenium_devcontainer-firefox-1:4444/wd/hub"
webdriver_url = "http://webdriver:4444/wd/hub"
webdriver_url = "http://selenium-hub:4444/wd/hub"


def getRemoteDriver():
    driver = webdriver.Remote(
        command_executor=webdriver_url,
        desired_capabilities={
            "browserName": browser,
            "acceptInsecureCerts": True
        })
    return driver


def runTest():
    driver.implicitly_wait(5)
    #driver.maximize_window()  # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
    driver.get(url)
    print("Title: <"+driver.title+">")
    driver.save_screenshot("heise.png")
    assert "heise" in driver.title


if __name__ == "__main__":
    driver = None
    try:
        print("heise.py: 1")
        driver = getRemoteDriver()
        # driver = getProxyRemoteDriver()
        # driver = getProxyRemoteDriver()
        # print(f"heise.py: 2: driver: ${driver}")
        runTest()
    finally:
        if (driver != None):
          driver.quit()
        else:
          print("heise.py: driver doesn't can' be closed - it's not initialized")
