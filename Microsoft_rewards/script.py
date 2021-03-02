from selenium import webdriver
from time import sleep
from random import randint, choice
import string
from selenium.webdriver.common.keys import Keys

# Setup du driver

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("https://www.bing.com")

# Géneration d'un mot aléatoire

# len_word=randint(0,10)
# word=[]
# for i in range(len_word):
#     letter=choice(string.ascii_letters)
#     word.append(letter)
# print(word)

def random_char(y):
       return ''.join(choice(string.ascii_letters) for x in range(y))


# Login

sleep(1.5)

login=driver.find_element_by_css_selector("a#id_l.id_button")
login.click()
sleep(1)
email=driver.find_element_by_id("i0116")
email.send_keys("")
sleep(0.5)
enter=driver.find_element_by_id("idSIButton9")
enter.click()
sleep(0.5)
passwld=driver.find_element_by_id("i0118")
passwld.send_keys("")
sleep(0.4)
entre1=driver.find_element_by_id("idSIButton9")
entre1.click()
sleep(1.5)


allow=driver.find_element_by_id("bnp_btn_accept")
allow.click()

# Recherche

a=(random_char(10))
search=driver.find_element_by_css_selector("input#sb_form_q.sb_form_q")
search.send_keys(a)
btn=driver.find_element_by_class_name("search")
btn.click()

for i in range(1):
    a=(random_char(10))
    ndsearch=driver.find_element_by_class_name("b_searchbox")
    ndsearch.send_keys(a)
    btn=driver.find_element_by_class_name("b_searchboxSubmit")
    btn.click()


while 1==1:
    a=(random_char(10))
    ndsearch=driver.find_element_by_class_name("b_searchbox")
    ndsearch.send_keys(a)
    btn=driver.find_element_by_class_name("b_searchboxSubmit")
    btn.click()
    sleep(0.5)
