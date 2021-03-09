import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
from selenium import webdriver
from urllib.parse import quote


def crawl_url(my_urls):
    list_of_data = []

    driver = webdriver.Chrome(
        executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
    driver.get(my_urls)
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
    f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
    f.write('hotel,city,comment_page_url')
    f.close()
    city = get_home_page(initialed_data)
    driver.close()
    urls = get_city_page(city)
    # store_seeds_csv(urls)
    return list_of_data


def get_home_page(list_of_data):
    web_links = []
    iterated = []
    for i in range(len(list_of_data)):
        if '<a class="city-name" href="/' in list_of_data[i] and list_of_data[i] not in iterated:
            web_links.append(['https://www.iranhotelonline.com' + list_of_data[i].split('href="')[1].split('">')[0],
                              list_of_data[i].split('/">')[1].split('</a>')[0].split('هتل های ')[1]])
            iterated.append(list_of_data[i])
    for i in range(2070, 2303):
        web_links.append(
            ['https://www.iranhotelonline.com' + list_of_data[i].split('"></i><a href="')[1].split('">')[0],
             list_of_data[i].split('/">')[1].split('</a> <')[0].split('هتل های ')[1]])
    return web_links


def get_city_page(city_url):
    comm_page = []

    for k in range(len(city_url)):
        # for k in range(2):
        list_of_data = []
        driver = webdriver.Chrome(
            executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
        driver.get(city_url[k][0])
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
        # print(city_url[0])
        urls = []
        for i in range(len(initialed_data)):
            try:
                if 'a href="' + city_url[k][0].split('https://www.iranhotelonline.com')[1] in initialed_data[i] and \
                        initialed_data[i] not in urls:
                    s = initialed_data[i].split(city_url[k][0].split('https://www.iranhotelonline.com')[1])[
                            1].split('/">')[0] + '/' + 'نظرات' + '/'
                    a = [city_url[k][0] + s, city_url[k][1],
                         initialed_data[i].split(city_url[k][0].split('https://www.iranhotelonline.com')[1])[
                             1].split('/">')[0]]
                    comm_page.append(a)
                    urls.append(initialed_data[i])
                    f = open('Data/Seed_pages.csv', 'a', encoding='utf-8')
                    f.write('\n' + str(a[2]) + ',' + str(a[1]) + ',' + str(a[0]))
                    f.close()
            except:
                print(city_url[k][0], city_url[k][1], initialed_data[i])
        driver.close()
        # print(comm_page)
    return comm_page


def store_seeds_csv(urls):
    f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
    f.write('hotel,city,comment_page_url')
    for i in range(len(urls)):
        f.write('\n' + str(urls[i][2]) + ',' + str(urls[i][1]) + ',' + str(urls[i][0]))
    f.close()


crawl_url('https://www.iranhotelonline.com/iran-hotels/')
