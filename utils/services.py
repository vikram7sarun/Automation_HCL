import json
import logging
import os
from pathlib import Path
import allure



class Services:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def config():
        config_path = os.path.join(Path(__file__).parent.parent, 'config/config.json')
        with open(config_path) as config_file:
            data = json.load(config_file)


    def getText(self,objects):
        self.driver.find_element(*objects).text
        # logging.debug('getText | value = {} | {}'.format(text, objects))

    def setText(self,objects,text):
        self.driver.find_element(*objects).clear()
        self.driver.find_element(*objects).send_keys(text)
        logging.debug('set_text {0} | {1}'.format(text, objects))

    def click(self,objects):
        self.driver.find_element(*objects).click()
        logging.debug('Click {}'.format(objects))

    def is_element_displayed(self,objects):
        try:
            return self.driver.find_element(*objects).is_displayed()
        except Exception:
            logging.info("Unable to locate element {}".format(objects))
            return False
