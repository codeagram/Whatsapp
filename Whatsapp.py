from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
#import pandas
import time
import pickle
import pyautogui as pg


class Whatsapp:

    def __init__(self, contacts, message):

        self.message = message
        self.contacts = contacts
        self.chrome_options = Options()
        self.chrome_options.add_argument(r"--user-data-dir=/home/ak/.config/google-chrome/Default")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.executor_url = self.driver.command_executor._url
        self.session_id = self.driver.session_id
        self.driver.get("https://web.whatsapp.com/")
        #self.driver2 = webdriver.Remote(command_executor=self.executor_url, desired_capabilities={})
        #self.driver2.session_id = self.session_id

    def execution(self):

        wait = WebDriverWait(self.driver, 20)
        search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        person_title = wait.until(lambda driver:self.driver.find_element_by_xpath(search_box))

        for num in self.contacts:
            person_title.clear()
            person_title.send_keys(num)
            person_title.send_keys(Keys.ENTER)
            input_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(self.message + Keys.ENTER)
            time.sleep(1)

        time.sleep(5)
        self.driver.close()

def main():

    # Add contacts
    contacts = []
    message = "HELLO"
    PyWhat = Whatsapp(contacts, message)
    PyWhat.execution()

if __name__ == "__main__":
    main()
