from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options


s = Service('/usr/local/bin/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("http://carrel.cnu.edu.tw/login.aspx")

account = driver.find_element(by=By.NAME, value="tbUserID")
account.send_keys("B1001184")

password = driver.find_element(by=By.NAME, value="tbPassword")
password.send_keys("5255")

test = driver.find_element(by=By.NAME, value="tbCaptcha")
keys = driver.find_element(by=By.NAME, value="captchaText")
password.send_keys(keys)

submit_button = driver.find_element(by=By.NAME, value="pbLogin")
submit_button.click()

reserve = driver.find_element(by=By.LINK_TEXT, value="按日借用研究小間")
reserve.click()

select_submit = driver.find_element(By.XPATH, '//button[@name="Button1" and @class="btn_submit"]')

for i in range(21):
    xpath = f'//a[@href="javascript:__doPostBack(\'GridView1\',\'Select${i}\')"]'
    select = driver.find_element(By.XPATH, xpath)
    select.click()
    select_submit.click()