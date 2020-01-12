from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='../venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
        self.vars = {}
        self.driver.implicitly_wait(60)

    def open_home_page(self):
        # 1 | open | / |  |
        self.driver.get("https://ayfigroup.com/contact/")

    def fill_form_fields(self):
        self.driver.find_element(By.NAME, "your-name").click()
        # 3 | type | name=your-name | test |
        self.driver.find_element(By.NAME, "your-name").send_keys("test")
        # 4 | click | name=your-company |  |
        self.driver.find_element(By.NAME, "your-company").click()
        # 5 | type | name=your-company | test |
        self.driver.find_element(By.NAME, "your-company").send_keys("test")
        # 6 | click | name=your-email |  |
        self.driver.find_element(By.NAME, "your-email").click()
        # 7 | type | name=your-email | testloc@gmail.com |
        self.driver.find_element(By.NAME, "your-email").send_keys("testloc@gmail.com")
        # 8 | click | name=your-telephone |  |
        self.driver.find_element(By.NAME, "your-telephone").click()
        # 9 | type | name=your-telephone | 283837124 |
        self.driver.find_element(By.NAME, "your-telephone").send_keys("283837124")
        # 10 | click | name=your-message |  |
        self.driver.find_element(By.NAME, "your-message").click()
        # 11 | type | name=your-message | test message please ignore |
        self.driver.find_element(By.NAME, "your-message").send_keys("test message please ignore")
        # 12 | click | css=.wpcf7-form-control:nth-child(2) |  |
        self.driver.find_element(By.CSS_SELECTOR, ".wpcf7-form-control:nth-child(2)").click()

    def destroy(self):
        self.driver.quit()
