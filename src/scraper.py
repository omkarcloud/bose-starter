from selenium.webdriver.common.by import By

from bose import BaseTask, Wait, Output

class Task(BaseTask):

    def run(self, driver):
        driver.get("https://quotes.toscrape.com/")
        els = driver.get_elements_or_none_by_selector('div.quote', Wait.SHORT)
        
        items = []

        for el in els: 
            text = driver.get_element_text(el.find_element(By.CSS_SELECTOR, "span.text")) 
            author = driver.get_element_text(el.find_element(By.CSS_SELECTOR, "small.author")) 
            item = {
                "text" : text, 
                "author" : author, 
            }
            items.append(item)

        Output.write_finished(items)