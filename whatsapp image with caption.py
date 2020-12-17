from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
contact = "shameelka"
#text = "Hey, this message was sent using python"
#filepath = 'D:/Userfiles/Desktop/Python Whatsapp/1.png'
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

#inp_xpath_search = "//input[@title='Search or start new chat']"
#input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
#input_box_search.click()
#time.sleep(2)
#input_box_search.send_keys(contact)
#time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

filesforme={1:"ss",2:"dd",3:"fff",4:"ee",5:"z",6:"t",7:"e",8:"d",9:"g",10:"h"}

for m in range (0,10):
    for key in filesforme:
            filepath_= (filesforme[key])
            for i in range(0,1):
                attachment_box=driver.find_element_by_xpath('//div[@title="Attach"]')
                attachment_box.click()

                image_box=driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)
                time.sleep(3)

                caption_button=driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
                caption_button.send_keys("LDF")
                time.sleep(1)

                send_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click()
                time.sleep(5)
                break




#inp_xpath = ('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#input_box = driver.find_element_by_xpath(inp_xpath)
#time.sleep(2)
#for i in range(0,11):
#    input_box.send_keys(text + Keys.ENTER)
#time.sleep(2)
#driver.quit()
