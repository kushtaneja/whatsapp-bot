# -*- coding: utf-8 -*-
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import csv
namelist=[]
with open("Names.csv") as f:
    for row in f:
        namelist.append(row.split(',')[0])


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-browser-side-navigation')
driver = webdriver.Chrome(chrome_options=options, executable_path='/Users/kt/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/") 


urlmessage="Book early bird tickets at: http://bit.ly/roundupvalentines"
message="Celebrate that 'perfect' valentine date under the stars only at Roundup Cafe. Cozy decor, candle light full dinner, Complimentry photoshoot, gifts on the house espcially curated for couples. Book now & thank us later!"
#convert to unicode
message = unicode(message, 'utf-8')

#encode it with string escape
message = message.encode('unicode_escape')

filepath="/Users/kt/valentinesday.png"

wait = WebDriverWait(driver, 20)
wait5 = WebDriverWait(driver, 5)
wait20 = WebDriverWait(driver, 20)

wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, 'iHhHL'
 )))

i=0
while i<len(namelist) :
	target = namelist[i]

	x_arg = "//span[contains(@title,'" + target + "')]"
	elements = driver.find_elements_by_xpath(x_arg)
	if len(elements) == 0:
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(target)
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(Keys.ENTER)
		print('Target Searched')

	cell = wait5.until(EC.presence_of_element_located((
	    By.XPATH, x_arg)))
	cell.click()
	driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/div/span").click()
	element=driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input")
	element.send_keys(filepath)

	time.sleep(2)
	# Select the Input Box
	inp_xpath = "//div[@contenteditable='true']"

	input_box = wait.until(EC.presence_of_element_located((
	    By.XPATH, inp_xpath)))

	# Send message
	input_box.send_keys(message)
	# Link Preview Time, Reduce this time, if internet connection is Good
	# time.sleep(10)
	input_box.send_keys(Keys.ENTER)
	print("Successfully Send Image to : "+ target + '\n')

	time.sleep(10)

	input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
	# Send message
	input_box.send_keys(urlmessage)
	time.sleep(2)
	input_box.send_keys(Keys.ENTER)
	print("Successfully url to : "+ target + '\n')
	# time.sleep(0.5)
	i=i+1