# WhatsApp-Bot-

This is a simple Web WhatsApp Bot developed in python using Selenium. 
Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation


### Installation

Step 1: Install Selenium 
```sh
$ pip3 install selenium
```

Step 2: Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
> For [Click for FireFox](https://github.com/mozilla/geckodriver/releases)
> For [Click for safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

Step 3: Extract the downloaded driver onto a folder

Step 4: Set path variable to the environment. Paste this command to the terminal
```sh
$ export PATH=$PATH:/home/path/to/the/driver/folder/
Eg: $ export PATH=$PATH:/home/harshit/Desktop/WhatsAppBot
```
Step 5: run whatsapp.py using Python3
```sh
$ python3 whatsapp_bot.py
```
Step 6: When the browser is opened web.whatsapp.com will be opened and will ask to scan a QR code when you it first time

Step 7: After Scanning the QR code, you will be asked to press Enter Key in the terminal.
