from selenium import webdriver
import time
import requests
import os

driver = webdriver.Chrome()
driver.get("https://unsplash.com")

time.sleep(5)  

if not os.path.exists('selenium_images'):
    os.makedirs('selenium_images')

images = driver.find_elements("tag name", "img")

for i, img in enumerate(images):
    src = img.get_attribute("src")
    if src:
        try:
            img_data = requests.get(src).content
            with open(f"selenium_images/img_{i}.jpg", 'wb') as f:
                f.write(img_data)
            print(f"Downloaded img_{i}.jpg")
        except:
            print("Failed to download image")

driver.quit()
