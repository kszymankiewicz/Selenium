from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:/Users/admin/Desktop/survival/hello/chromedriver.exe")
driver.get("https://asta.pgs-soft.com")
driver.implicitly_wait(5)
driver.implicitly_wait(3)
driver.find_element_by_xpath("//div[1]/a[@class='button']").click()
driver.implicitly_wait(3)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.maximize_window()
driver.implicitly_wait(3)
driver.save_screenshot('C:/Users/admin/Desktop/survival/hello/screenshots/screenshot2.png')
driver.implicitly_wait(3)
driver.find_element_by_xpath("//div[1]/a[@href='/task_1']").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//div/input[@class='form-control']").clear()
driver.find_element_by_xpath("//div/input[@class='form-control']").send_keys("100")
driver.implicitly_wait(3)
driver.find_element_by_xpath("//div/span/button[@class='btn btn-sm']").click()
driver.implicitly_wait(3)
driver.save_screenshot('C:/Users/admin/Desktop/survival/hello/screenshots/screenshot3.png')


#driver.quit()

