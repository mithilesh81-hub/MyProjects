import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

engine = pyttsx3.init()
volume = engine.getProperty('volume')
r = sr.Recognizer()

Username = 'javvajimithilesh81@gmail.com'
Password = 'Mithilesh81@'

Shoppinglist = []

class AmamzonShoppinglist:
    browser = None
    timeout = 10

    def __init__(self, wait, screenshot=None, session=None):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\Mithilesh Javvaji\Downloads\chromedriver.exe")



    def login(self):
        self.browser.get("https://www.amazon.co.uk/alexaquantum/sp/alexaShoppingList?ref=nav_asl")
        self.browser.maximize_window()
        UsernameElement = self.browser.find_elements(By.ID, 'ap_email')
        UsernameElement[0].send_keys(Username)

        PasswordElement = self.browser.find_elements(By.ID, 'ap_password')
        PasswordElement[0].send_keys(Password)

        Login = self.browser.find_elements(By.ID, 'signInSubmit')
        Login[0].click()


    def getShoppinglist(self):

        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-dIvqjp,ctzszt,item-name')))
        ItemNameElement = self.browser.find_elements(By.CLASS_NAME, 'sc-dIvqjp,ctzszt,item-name')

        return ItemNameElement

    def clearShoppinglist(self):
       for i in Itemslist:
         CheckElement = self.browser.find_elements(By.CLASS_NAME, 'sc-kEqYlL,sc-iqAbSa,ccZDzm,wbQEM,action')
         for n in CheckElement:
             if n.text.lower() == 'delete':
              n.click()
         Itemslist.clear()



class Groceries:

 def finditemsainsburys(self,item):

     itemsdict = {
      'milk':"Sainsbury's British Whole Milk 2.27L (4 pint)",
      'tomatoes':"Sainsbury's Classic Round Tomatoes x6",
      'potatoes':"Sainsbury's British Maris Piper Potatoes 2.5kg"
     }
     for i in itemsdict.keys():
         if item == i:
             return itemsdict[i]

 def finditemstesco(self,item):

     itemsdict = {
      'milk':"Tesco Whole Milk 2.272L/4 Pints",
      'tomatoes':"Tesco Salad Tomatoes 6 Pack",
      'potatoes':"Tesco Baking Potatoes 2.5Kg Pack"
     }
     for i in itemsdict.keys():
         if item == i:
             return itemsdict[i]


class Sainsburys:

    browser = None
    timeout = 10
    target = "DAD"

    def __init__(self, wait, screenshot=None, session=None):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\Mithilesh Javvaji\Downloads\chromedriver.exe")
        self.browser.get("https://www.sainsburys.co.uk/webapp/wcs/stores/servlet/gb/groceries?storeId=10151&langId=44&krypto=tRrTjjU0ImS%2BufyXTbJZ8twJdEk%2B748m%2B0pNRX9hcv0cg2JUFvOD5nPjU9Rv6ZOLe2jMFmL25Pw6SS21u55fb2EgRmehSyipKHrw9VyKxBSWk2GD3o9vM9shYqBVOsILq9eKjOGjXSIrIem2yI7I39eNZhAYs%2Bgv6kWDo3NaFmk%3D&ddkey=https%3Agb%2Fgroceries")
        self.browser.maximize_window()
        self.login()
        groceries = Groceries()
        for n in Shoppinglist:
         item = groceries.finditemsainsburys(n)
         time.sleep(2)
         self.CheckPrice(item)


    def login(self):
        time.sleep(2)
        allowcookies0 = self.browser.find_elements(By.ID, 'onetrust-accept-btn-handler')
        allowcookies0[0].click()
        time.sleep(2)
        loginelement = self.browser.find_elements(By.CLASS_NAME, 'login')
        loginelement[0].click()
        time.sleep(4)
        allowcookies2 = self.browser.find_elements(By.ID, 'onetrust-accept-btn-handler')
        allowcookies2[0].click()
        time.sleep(2)
        Usernamelement  = self.browser.find_elements(By.ID, 'username')
        Passwordelelment = self.browser.find_elements(By.ID, 'password')
        Login = self.browser.find_elements(By.CLASS_NAME, 'ln-c-button,ln-c-button--full,ln-u-display-inline-flex ln-u-justify-content-center,ln-u-align-items-center,ln-c-button--filled')
        Usernamelement[0].send_keys(Username)
        Passwordelelment[0].send_keys(Password)
        time.sleep(2)
        Login[1].click()

    def CheckPrice(self,item):

        try:
            search = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'search')))
            search.send_keys(item)

            searchbutton = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'searchSubmit')))
            searchbutton.click()

            time.sleep(4)
            AddHyper = self.browser.find_elements(By.CLASS_NAME,'pt__link')
            AddHyper[0].click()

            time.sleep(2)
            self.AddElement = self.browser.find_elements(By.CLASS_NAME,'ln-c-button,ln-c-button--filled,ln-c-button--full,pt__add-button')

            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pd__cost-wrapper')))
            PriceElement = self.browser.find_elements(By.CLASS_NAME, 'pd__cost-wrapper')
            priceraw = PriceElement[0].text
            try:
                self.price = float(PriceElement[0].text.replace('£', '')[0:4])
            except:
                self.price = int(PriceElement[0].text.replace('£', '')[0:2])
            print('Sainsburys: '+ str(self.price))

        except:
            search = WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.ID, 'search-bar-input')))
            search.send_keys(item)

            searchbutton = WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-bar__button')))
            searchbutton.click()

            time.sleep(2)
            AddHyper = self.browser.find_elements(By.CLASS_NAME, 'pt__link')
            AddHyper[0].click()

            time.sleep(2)
            self.AddElement = self.browser.find_elements(By.CLASS_NAME,'ln-c-button,ln-c-button--filled,ln-c-button--full,pt__add-button')

            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pd__cost-wrapper')))
            PriceElement = self.browser.find_elements(By.CLASS_NAME, 'pd__cost-wrapper')
            priceraw = PriceElement[0].text
            try:
                self.price = float(PriceElement[0].text.replace('£', '')[0:4])

            except:
                self.price = float('0.' + PriceElement[0].text.replace('£', '')[0:2])

            print('Sainsburys: '+str(self.price))

class Tesco:

    browser = None
    timeout = 10
    target = "DAD"

    def __init__(self, wait, screenshot=None, session=None):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\Mithilesh Javvaji\Downloads\chromedriver.exe")
        self.browser.get("https://www.tesco.com/")
        self.browser.maximize_window()
        self.login()
        groceries = Groceries()
        item = groceries.finditemstesco('milk')
        time.sleep(2)
        for n in Shoppinglist:
            item = groceries.finditemstesco(n)
            time.sleep(2)
            self.CheckPrice(item)



    def login(self):
        time.sleep(2)
        allowcookies0 = self.browser.find_elements(By.CLASS_NAME, 'styled__BaseButton-sc-3mnirm-0,styled__SecondaryButton-sc-3mnirm-3,hlwzLF eJluGd beans-cookies-notification__button beans-button__container')
        allowcookies0[0].click()
        time.sleep(2)
        loginelement = self.browser.find_elements(By.CLASS_NAME, 'link-tab,onclick-menu')
        loginelement[0].click()
        time.sleep(4)
        Usernamelement  = self.browser.find_elements(By.ID, 'email')
        Passwordelelment = self.browser.find_elements(By.ID, 'password')
        Login = self.browser.find_elements(By.ID, 'signin-button')
        Usernamelement[0].send_keys(Username)
        Passwordelelment[0].send_keys(Password)
        time.sleep(2)
        Login[0].click()


    def CheckPrice(self,item):
      try:

        search = self.browser.find_elements(By.CLASS_NAME, 'input-text-box')
        search[1].send_keys(item)

        searchbutton = self.browser.find_elements(By.CLASS_NAME, 'search-icon-button')
        searchbutton[1].click()

        time.sleep(2)
        AddHyper = self.browser.find_elements(By.CLASS_NAME,'ui__StyledLink-sc-18aswmp-0,eYySMn')
        AddHyper[0].click()

        time.sleep(2)
        self.AddElement = self.browser.find_elements(By.CLASS_NAME,'button,small,add-control,button-secondary')

        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'price-per-sellable-unit,price-per-sellable-unit--price,price-per-sellable-unit--price-per-item')))
        PriceElement = self.browser.find_elements(By.CLASS_NAME, 'price-per-sellable-unit,price-per-sellable-unit--price,price-per-sellable-unit--price-per-item')
        try:
            self.price = float(PriceElement[0].text.replace('£', '')[0:4])
        except:
            self.price = int(PriceElement[0].text.replace('£', ''))
        print('Tescos: '+str(self.price))


      except:

          time.sleep(2)
          search = self.browser.find_elements(By.ID, 'search-input')
          search[0].send_keys(item)

          searchbutton = self.browser.find_elements(By.CLASS_NAME, 'search-bar__submit,icon-search-white')
          searchbutton[0].click()

          time.sleep(4)
          AddHyper = self.browser.find_elements(By.CLASS_NAME, 'ui__StyledLink-sc-18aswmp-0,eYySMn')
          AddHyper[0].click()

          time.sleep(2)
          self.AddElement = self.browser.find_elements(By.CLASS_NAME, 'button,small,add-control,button-secondary')

          WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'value')))
          PriceElement = self.browser.find_elements(By.CLASS_NAME, 'value')

          try:
           self.price = float(PriceElement[0].text.replace('£', '')[0:5])
          except:
            print(PriceElement[0].text.replace('£', ''))
            self.price = PriceElement[0].text.replace('£', '')

          print('Tescos: '+str(self.price))


def addtocart():
    print("In Add To cart")
    if groTes.price < groSan.price:
        for n in groSan.AddElement:
            if n.text == 'Add':
                n.click()
                break
    elif groTes.price > groSan.price:
        for n in groSan.AddElement:
            if n.text == 'Add':
                n.click()
                break

amamzonshoppinglist = AmamzonShoppinglist(30)
amamzonshoppinglist.login()
ItemsListraw = amamzonshoppinglist.getShoppinglist()
Itemslistcurropt = []
Itemslist = []

for i in ItemsListraw:
    Itemslistcurropt.append(i.text.split(' '))

for i in range(len(Itemslistcurropt)):
    for i in Itemslistcurropt[i]:
        Shoppinglist.append(i)


groSan = Sainsburys(30)
groTes = Tesco(30)
addtocart()
