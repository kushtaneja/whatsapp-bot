from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
target = input("enter the name of the target in the list")
message=input("enter the Message")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-browser-side-navigation')
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/lib/chromium-browser/chromedriver')
driver.get("https://web.whatsapp.com/") 

input("Scan the QR code and wait the page to load then press Enter")
  

time.sleep(10)
wait5 = WebDriverWait(driver, 5)
wait = WebDriverWait(driver, 20)
x_arg = '//span[contains(@title,' + target + ')]'
try:
    wait5.until(EC.presence_of_element_located((
        By.XPATH, x_arg
    )))
    print("Try Block Ran")
except:
	driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(target)
	driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input").send_keys(Keys.ENTER)
	print('Target Searched')
	# Increase the time if searching a contact is taking a long time
	time.sleep(4)

# Select the target
time.sleep(10)
#print(x_arg)
try:
	k=driver.find_element_by_xpath("//span[contains(@title,'" + target + "')]")
	k.click()
	print("Target Successfully Selected")
	
except:
	print(target +' Not found ' )
	exit()

#print(k)


time.sleep(2)

# Select the Input Box
inp_xpath = "//div[@contenteditable='true']"
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
time.sleep(1)

# Send message
# taeget is your target Name and msgToSend is you message
input_box.send_keys(message)
# Link Preview Time, Reduce this time, if internet connection is Good
time.sleep(10)
input_box.send_keys(Keys.ENTER)
print("Successfully Send Message to : "+ target + '\n')
time.sleep(0.5)
