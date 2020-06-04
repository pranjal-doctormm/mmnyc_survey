###### Importing libraries ######
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from oauth2client.service_account import ServiceAccountCredentials
import gspread, time
import constants as c

###### Login to google account #####
# driver = webdriver.Chrome(c.driver_path)
# driver.get(c.g_link)
# driver.find_element_by_name(c.identifier_element).send_keys(c.gmail_id)
# driver.find_element_by_xpath(c.xpath_next).click()
# driver.implicitly_wait(10)
# driver.find_element_by_name(c.pass_element).send_keys(c.gmail_pass)
# driver.find_element_by_xpath(c.xpath_login).click()

###### Open Google spreadsheet from selenium  ######
# driver.get(c.ss_url)
# time.sleep(4)
# driver.implicitly_wait(15)

## DELETE DATA FROM SPREADSHEET
creds = ServiceAccountCredentials.from_json_keyfile_name(c.json_cred_path, c.ss_api)
client = gspread.authorize(creds)
sheet = client.open(c.ss_name).worksheet(c.s_name)
sheet.delete_row(c.delete_row)

###### Open Google spreadsheet from selenium  ######
# driver.get(c.ss_url)
# #driver.implicitly_wait(20)
# time.sleep(15)
# driver.find_element_by_xpath(c.xpath_ss_tools).click()  ##tools
# driver.implicitly_wait(20)
# #'//div[@class="menu-button goog-control goog-inline-block goog-control-open docs-menu-button-open-below" and contains(text(), "<> Script editor")]'
# driver.find_element_by_xpath(c.xpath_ss_tools_script_editor).click()  ##script editor
# #driver.implicitly_wait(20)
# time.sleep(15)
# driver.switch_to_window(driver.window_handles[-1])  ## gs code active window command
# #driver.implicitly_wait(20)
# driver.find_element_by_xpath(c.xpath_gs_publish).click() ## click on publish
# #driver.implicitly_wait(20)
# driver.find_element_by_xpath(c.xpath_gs_deploy).click() ## click on deploy
# #driver.implicitly_wait(20)
# driver.find_element_by_xpath(c.xpath_gs_web_new).click() ## click on New project version
# #driver.implicitly_wait(20)
# time.sleep(10)
# driver.find_element_by_xpath(c.xpath_gs_update).click() ## click on update
# driver.implicitly_wait(20)
# time.sleep(10)
# driver.find_element_by_xpath(c.xpath_gs_latest_c).click() ## click on latest code
# time.sleep(30)

#driver.close()
#driver.quit()
