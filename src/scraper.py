from bose import BrowserConfig, BaseTask

class Task(BaseTask):
    def run(self, driver):
        driver.get_google()