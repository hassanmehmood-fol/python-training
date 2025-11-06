from selenium import webdriver

driver = webdriver.Chrome()  # Chrome browser open karega
driver.get("https://www.google.com")

print(driver.title)  # prints: Google

driver.quit()  # close browser
