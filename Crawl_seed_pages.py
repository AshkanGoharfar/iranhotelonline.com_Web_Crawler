import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
from selenium import webdriver
from urllib.parse import quote
import pandas as pd
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

# multi-processing

# split a list into evenly sized chunks
def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def do_job(job_id, data_slice):
    for city in data_slice:
        crawl_city_page(city)


def crawl_seeds():
    f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
    f.write('hotel,city,comment_page_url,hotel_star')
    f.close()
    df = pd.read_csv('Data/Early_seed_pages.csv')
    cities = df.values.tolist()
    return cities


def crawl_home_page():
    f = open('Data/Early_seed_pages.csv', 'w+', encoding='utf-8')
    f.write('city_name,city_url')
    f.close()

    with open('data.txt', 'r') as file:
        webdriver_chrome = file.read().replace('\n', '')
    list_of_data = []
    # print(webdriver_chrome)

    # This example requires Selenium WebDriver 3.13 or newer
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)

        # a = r"C:\ProgramData\chocolatey\bin\chromedriver.exe"
        #
        # driver = webdriver.Chrome(
        #     executable_path=webdriver_chrome)
        # r"C:\ProgramData\chocolatey\bin\chromedriver.exe"
        driver.get('https://www.iranhotelonline.com/iran-hotels/')
        html = driver.page_source
        soup = BeautifulSoup(html)
        for tag in soup.find_all('div'):
            if tag not in list_of_data:
                list_of_data.append(str(tag))

        initialed_data = []
        for item in list_of_data:
            new_item = item.split('\n')
            for term in new_item:
                initialed_data.append(term)
        list_of_data = initialed_data
        # f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
        # f.write('hotel,city,comment_page_url,hotel_star')
        # f.close()
        web_links = []
        iterated = []
        for i in range(len(list_of_data)):
            if '<a class="city-name" href="/' in list_of_data[i] and list_of_data[i] not in iterated:
                web_links.append(['https://www.iranhotelonline.com' + list_of_data[i].split('href="')[1].split('">')[0],
                                  list_of_data[i].split('/">')[1].split('</a>')[0].split('هتل های ')[1]])
                iterated.append(list_of_data[i])
                f = open('Data/Early_seed_pages.csv', 'a', encoding='utf-8')
                f.write('\n' + 'https://www.iranhotelonline.com' + list_of_data[i].split('href="')[1].split('">')[0] + ',' +
                        list_of_data[i].split('/">')[1].split('</a>')[0].split('هتل های ')[1])
                f.close()
        for i in range(2062, 2295):
            f = open('Data/Early_seed_pages.csv', 'a', encoding='utf-8')
            f.write('\n' + 'https://www.iranhotelonline.com' + list_of_data[i].split('"></i><a href="')[1].split('">')[
                0] + ',' + list_of_data[i].split('/">')[1].split('</a> <')[0].split('هتل های ')[1])
            f.close()
            web_links.append(
                ['https://www.iranhotelonline.com' + list_of_data[i].split('"></i><a href="')[1].split('">')[0],
                 list_of_data[i].split('/">')[1].split('</a> <')[0].split('هتل های ')[1]])
        driver.close()
    return web_links


def crawl_city_page(city_url):
    time1 = time.time()
    comm_page = []
    flag_page = 0
    page_counter_1 = 1
    while flag_page == 0:
        list_of_data = []

        with open('Data/Metadata.txt', 'r') as file:
            webdriver_chrome = file.read().rsplit('\n')[0]
        driver = webdriver.Chrome(
            executable_path=webdriver_chrome)

        # driver = webdriver.Chrome(
        #     executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")

        city_url_page = city_url[0] + '?p=' + str(page_counter_1)
        driver.get(city_url_page)
        html = driver.page_source
        soup = BeautifulSoup(html)
        for tag in soup.find_all('div'):
            if tag not in list_of_data:
                list_of_data.append(str(tag))

        initialed_data = []
        for item in list_of_data:
            new_item = item.split('\n')
            for term in new_item:
                initialed_data.append(term)

        urls = []
        num_of_items_in_page = 0
        for i in range(len(initialed_data)):
            if 'a href="' + city_url_page.split('https://www.iranhotelonline.com')[1].split('?p')[0] in \
                    initialed_data[
                        i] and \
                    initialed_data[i] not in urls:
                num_of_items_in_page += 1
                s = initialed_data[i].split(
                    city_url_page.split('https://www.iranhotelonline.com')[1].split('?p')[0])[
                        1].split('/">')[0] + '/' + 'نظرات' + '/'
                a = [city_url_page.split('?p')[0] + s, city_url[1],
                     initialed_data[i].split(
                         city_url_page.split('https://www.iranhotelonline.com')[1].split('?p')[0])[
                         1].split('/">')[0],
                     initialed_data[i + 8].split('src="/Persian/Images/hotel-list/star')[1].split('-1')[0]]
                comm_page.append(a)
                urls.append(initialed_data[i])
                f = open('Data/Seed_pages.csv', 'a', encoding='utf-8')
                f.write('\n' + str(a[2]) + ',' + str(a[1]) + ',' + str(a[0]) + ',' + str(a[3]))
                f.close()
            elif '' + '/ecolodge/' in initialed_data[
                i] and '" style="width:auto;' in initialed_data[i] and \
                    initialed_data[i] not in urls:
                num_of_items_in_page += 1
                city_hotel_name = initialed_data[i].split('href="/ecolodge/')[1].split('/" ')[0].split('/')
                city_name = city_hotel_name[0]
                hotel_name = city_hotel_name[1]
                url = "https://www.iranhotelonline.com" + initialed_data[i].split('href="')[1].split('" style')[
                    0] + 'نظرات' + '/'
                a = [url, city_name, hotel_name,
                     initialed_data[i + 3].split('src="/Persian/Images/hotel-list/star')[1].split('-1')[0]]
                comm_page.append(a)
                urls.append(initialed_data[i])
                f = open('Data/Seed_pages.csv', 'a', encoding='utf-8')
                f.write('\n' + str(a[2]) + ',' + str(a[1]) + ',' + str(a[0]) + ',' + str(a[3]))
                f.close()
        driver.close()
        page_counter_1 += 1
        if num_of_items_in_page < 10:
            flag_page = 1
    print('Elapsed time: ', time.time() - time1)
    # return comm_page


def store_seeds_csv(urls):
    f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
    f.write('hotel,city,comment_page_url')
    for i in range(len(urls)):
        f.write('\n' + str(urls[i][2]) + ',' + str(urls[i][1]) + ',' + str(urls[i][0]))
    f.close()

# crawl_seeds('https://www.iranhotelonline.com/iran-hotels/')
