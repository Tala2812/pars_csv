import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"
driver.get(url)

time.sleep(3)

svets = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = svet.find_element(By.TAG_NAME, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, url])

# Запись данных в CSV
with open('svet_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['название', 'цена', 'ссылка'])
    writer.writerows(parsed_data)

driver.quit()