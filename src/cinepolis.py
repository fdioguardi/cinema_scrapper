from selenium import webdriver
from cinema import CinemaScrappy


class CinepolisScrappy(CinemaScrappy):
    """Scrapper of Cinepolis's billboard"""

    def __init__(
        self,
        driver_executable="chromedriver",
        browser_executable="/usr/bin/brave",
    ):
        super().__init__(_cinema_page="http://www.villagecines.com/")
        self.browser_executable = browser_executable
        self.driver_executable = driver_executable

    def chromium_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.browser_executable
        return webdriver.Chrome(
            executable_path=self.driver_executable, options=options
        )

    def scrape(self):
        """
        Extract information from Cinepolis' billboard
        """
        driver = self.chromium_driver()
        driver.get("https://google.com")


CinepolisScrappy().scrape()
