# -*- coding: utf-8 -*-
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import csv
namelist=[]
sentlist=[]
with open("left_Names.csv") as f:
    for row in f:
        namelist.append(row.split(',')[0])

a = {u'WAToken1': u'"t85PaRk6QPKW6M+V2euWcpa6ZV9kqbCdCBYtjv3NuOQ="', u'2Uls+st8KOZKAlLNKbVILw==': u'[{"id":"global_mute","expiration":0}]', u'storage_test': u'storage_test', u'WAToken2': u'"1@SKhgMCbleVVEyyQXyBgXGmCSlJ1xtj4f4BNQUGSl1057q7inrOUU4jSBux0w0ANlaAzqBh8c1nPt+Q=="', u'WALangPref': u'"en"', u'WASecretBundle': u'{"key":"D1yhj/W+oOcgAGoawwKCU0Wy/pmj6NWqXs26aUDaWQQ=","encKey":"5pgB7VUugg3DdTvGNUmStezBoeSQvPLuvIda1PokYEQ=","macKey":"D1yhj/W+oOcgAGoawwKCU0Wy/pmj6NWqXs26aUDaWQQ="}', u'last-wid': u'"919108904691@c.us"', u'ZXcdCxVHkMhU1JvJbvN9pQ==': u'false', u'logout-token': u'"1@TJc03l+RP8dNiX75isMlWEuOZjqjcU7eOrokUeMHhPNCZlqRkyDZPdrjiTpL8HIGuR7CbTVT+EMgD1fGeyN70m0Al/rEn25Duo6MAY7UMgyi4XWbf0BkbKF9Z+i/vLfbszzsrCHj+3hNl3sdmXDsTg=="', u'X8ahjfhRZepedxYLR9oOZQ==': u'"note.m4r"', u'ps7fTp/NEON3Q1UJoMLw9g==': u'false', u'whatsapp-mutex': u'"x391925103:init_1549893668136"', u'Dexie.DatabaseNames': u'["wawc"]', u'B5/ZHwUThP1mYU2nnsFF4Q==': u'false', u'remember-me': u'true', u'WABrowserId': u'"V6ByWH6p9mcIqLAPbvtK/A=="', u'mobile-platform': u'"smba"', u'ASvDGz3FYse4HogUrB/0BA==': u'false', u'debugCursor': u'198'}
dump = str(a)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-browser-side-navigation')
# options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options, executable_path='/Users/kt/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/") 


urlmessage="Book early bird tickets at: http://bit.ly/roundupvalentines"
message="Celebrate that 'perfect' valentine date under the stars only at Roundup Cafe. Cosy decor, candlelight full dinner, Complimentary photoshoot, gifts on the house especially curated for couples. Book now & thank us later!"
saveMessage="Save our business contact for further updates :)"
#convert to unicode
message = unicode(message, 'utf-8')

#encode it with string escape
message = message.encode('unicode_escape')

filepath="/Users/kt/valentinesday.png"

wait = WebDriverWait(driver, 20)
wait5 = WebDriverWait(driver, 10)
wait20 = WebDriverWait(driver, 20)

for key in a:
	driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, a[key])
  	print("%s: %s" % (key, a[key]))


wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, 'iHhHL'
 )))

xpathCancel="//*[@id=\"side\"]/div[1]/div/span/button"

def sendMessage(target):
	x_arg = "//span[contains(@title,'" + target + "')]"
	try:
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

		time.sleep(2)

		input_box = wait.until(EC.presence_of_element_located((
	    By.XPATH, inp_xpath)))
		# Send message
		input_box.send_keys(urlmessage)
		time.sleep(4)
		input_box.send_keys(Keys.ENTER)
		print("Successfully url to : "+ target + '\n')
		time.sleep(0.5)
		input_box = wait.until(EC.presence_of_element_located((
	    By.XPATH, inp_xpath)))
		# Send message
		input_box.send_keys(saveMessage)
		input_box.send_keys(Keys.ENTER)

		sentlist.append(target)
	except:
		driver.find_element_by_xpath(xpathCancel).click()

i=0

while i<len(namelist) :
	target = namelist[i]
	print("entered loop for: "+ target)
	try:
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys('')
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(Keys.ENTER)
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(target)
		driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(Keys.ENTER)
		print('Target Searched')
		time.sleep(2)
		sendMessage(target)
	except:
		print("entered first except for %s", target)
		try:
			driver.find_element_by_xpath(xpathCancel).click()
		except:
			print("entered second except for %s", target)
			pass
	i=i+1

w = csv.writer(open('sent_names.csv','wb'), delimiter=',',quoting=csv.QUOTE_MINIMAL)
w.writerow(sentlist)
