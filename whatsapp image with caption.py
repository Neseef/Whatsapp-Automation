from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

contact = "Contact name" #specify the contact or group to whome you will send the msgs
#text = "Hey, this message was sent using python"
#filepath = 'D:/Userfiles/Desktop/Python Whatsapp/1.png'
driver = webdriver.Chrome() #we need to download chromedriver to the script directory for this to work.
driver.get("https://web.whatsapp.com") #Open whatsapp web and scan qr code. then hit enter.
print("Scan QR Code, And then Enter")
input()
print("Logged In")

#inp_xpath_search = "//input[@title='Search or start new chat']"
#input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
#input_box_search.click()
#time.sleep(2)
#input_box_search.send_keys(contact)
#time.sleep(2)

#find your contact on the left pane and click on them to select.
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

#filepaths for your images.
filesforme={1:"filepath1",2:"filepath2",3:"filepath3",4:"filepath4",5:"filepath5",6:"filepath6",7:"filepath7",8:"filepath8",9:"filepath9",10:"filepath10"}

#number of time the loop should run, each time sending one msg.
for m in range (0,10):
    #change the filepath each time.
    for key in filesforme:
            filepath_= (filesforme[key])

            #send an image then break out of loop. I think this loop is actually not needed.
            #i will work on it later
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
