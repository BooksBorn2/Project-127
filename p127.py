from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

from selenium.webdriver.common.by import By

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("/Users/shreyashavasarala/Desktop/VSC/Python/P127/chromedriver")
browser.get(START_URL)

time.sleep(10)
def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 1:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


planet_bf_1 = pd.DataFrame(planet_data, columns = headers)
planet_bf_1.to_csv("scrape.csv", index = True, index_label = "id")


scrape()
