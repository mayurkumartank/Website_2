import time
import undetected_chromedriver as uc
import csv
import pandas as pd
from selenium.webdriver.common.by import By


def write_output(datas):
    with open('output_task_2.csv', mode='w', encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Header
        writer.writerow(['School Name','Address', 'State', 'Zip', 'First Name', 'Last Name', 'Title', 'Phone', 'Email'])

        # Body
        for row in datas:
            writer.writerow(row.values())
    pd.read_csv("output.csv")

driver = uc.Chrome()
driver.get('https://isd110.org/our-schools/laketown-elementary/staff-directory')
driver.maximize_window()
time.sleep(1)

datas = []
def fetch_data():
    while True:
        time.sleep(1)

        school_name = "Waconia Public Schools"
        for i in driver.find_elements(By.XPATH,'//div[@class="node staff teaser"]'):
            row_data = {}
            address = ",".join([j.text for j in i.find_elements(By.XPATH, './/div[@class="field locations label-above"]/div[2]/span')])
            state = "Data Not Available"
            zip = "Data Not Available"
            title = i.find_element(By.XPATH, './div[2]/h2').text
            first_name = title.split(", ")[0]
            last_name = title.split(", ")[-1]
            phone = i.find_element(By.XPATH, './div[3]/div[1]/a').text
            email = i.find_element(By.XPATH, './div[3]/div[2]/a').text

            row_data["school_name"] = school_name
            row_data["address"] = address
            row_data["state"] = state
            row_data["zip"] = zip
            row_data["first_name"] = first_name
            row_data["last_name"] = last_name
            row_data["title"]  =title
            row_data["phone"] = phone
            row_data["email"] = email

            datas.append(row_data)
        next_page= driver.find_elements(By.XPATH,'//a[@title="Go to next page"]')
        if next_page != []:
            next_page[0].click()
            time.sleep(3)
            return fetch_data()
        else:
          break

fetch_data()
write_output(datas)
driver.close()
