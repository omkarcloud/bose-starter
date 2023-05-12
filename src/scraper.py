from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bose import BaseTask, Wait, Output

class Task(BaseTask):
    
    def run(self, driver):
        query = 'bose web scraping framework'
        
        driver.get("https://www.google.com/")
        search_box = driver.find_element(By.NAME, "q")

        search_box.send_keys(query)
        driver.sleep(1)
        search_box.send_keys(Keys.ENTER)
        els = driver.get_elements_or_none_by_selector('.yuRUbf a', Wait.SHORT)        

        links = [el.get_attribute("href") for el in els]
        Output.write_finished(links)