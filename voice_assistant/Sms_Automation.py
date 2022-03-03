from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def callfunction():
    Sms().unreadmessages()

class Sms:
    browser = None
    timeout = 10

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\Mithilesh Javvaji\Downloads\chromedriver.exe")
        try:
            self.browser.get("https://messages.google.com/web/conversations/1?pli=1")
        except Exception as e:
            print(e)


    def getlatestmessages(self,contactname):
        try:
            myElem = WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'name, ng-star-inserted')))
        except TimeoutException:
            print('Loading took too much time!')
        contacts = self.browser.find_elements(By.CLASS_NAME, 'name, ng-star-inserted')
        for contact in contacts:
            if contact.text == contactname:
                contact.click()
        WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'text-msg, ng-star-inserted')))
        messages = self.browser.find_elements(By.CLASS_NAME, 'text-msg, ng-star-inserted')
        for x in messages:
            print(x.text)




    def unreadmessages(self):
        try:

            contacts = self.browser.find_elements(By.CLASS_NAME, 'unread')

            for contact in contacts:
                contact.click()

            messages = self.browser.find_elements(By.CLASS_NAME, 'incoming')
            for x in messages:
                print(x.text)

        except Exception as e:
            print(e)




    def outgoingmessages(self):
        try:

            contacts = self.browser.find_elements(By.CLASS_NAME, 'unread')

            for contact in contacts:
                contact.click()

            messages = self.browser.find_elements(By.CLASS_NAME, 'xms-outgoing')

            for x in messages:
                print(x.text)
        except Exception as e:
            print(e)









