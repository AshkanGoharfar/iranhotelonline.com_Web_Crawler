# # import urllib.request
# # from bs4 import BeautifulSoup
# # from lxml import html
# # import requests
# # from selenium import webdriver
# # from urllib.parse import quote
# #
# #
# # def crawl_url(my_urls):
# #     list_of_data = []
# #
# #     driver = webdriver.Chrome(
# #         executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
# #     driver.get(my_urls)
# #     html = driver.page_source
# #     soup = BeautifulSoup(html)
# #     city = []
# #     counter_1 = 0
# #     counter_2 = 0
# #     for tag in soup.find_all('div'):
# #         if tag not in list_of_data:
# #             list_of_data.append(str(tag))
# #
# #     initialed_data = []
# #     for item in list_of_data:
# #         new_item = item.split('\n')
# #         for term in new_item:
# #             initialed_data.append(term)
# #     city = get_home_page(initialed_data)
# #     driver.close()
# #     print(city)
# #     # load_page(city[0][0])
# #     # urls = get_city_page(city)
# #     # store_seeds_csv(urls)
# #     return list_of_data
# #
# #
# # def get_home_page(list_of_data):
# #     web_links = []
# #     # 1316
# #     iterated = []
# #     for i in range(len(list_of_data)):
# #         if '<a class="city-name" href="/' in list_of_data[i] and list_of_data[i] not in iterated:
# #             web_links.append(['https://www.iranhotelonline.com' + list_of_data[i].split('href="')[1].split('">')[0],
# #                      list_of_data[i].split('/">')[1].split('</a>')[0].split('هتل های ')[1]])
# #             iterated.append(list_of_data[i])
# #     # for i in range(2070, 2303):
# #     #     web_links.append(
# #     #         ['https://www.iranhotelonline.com' + list_of_data[i].split('"></i><a href="')[1].split('">')[0],
# #     #          list_of_data[i].split('/">')[1].split('</a> <')[0].split('هتل های ')[1]])
# #     return web_links
# #
# #
# # def load_page(url):
# #     list_of_data = []
# #
# #     driver = webdriver.Chrome(
# #         executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
# #     driver.get(url)
# #     html = driver.page_source
# #     soup = BeautifulSoup(html)
# #     for tag in soup.find_all('div'):
# #         if tag not in list_of_data:
# #             list_of_data.append(str(tag))
# #
# #     initialed_data = []
# #     for item in list_of_data:
# #         new_item = item.split('\n')
# #         for term in new_item:
# #             initialed_data.append(term)
# #     for item in initialed_data:
# #         print(item)
# #     driver.close()
# #
# #
# # crawl_url('https://www.iranhotelonline.com/iran-hotels/')
# #
#
#
# def store_seeds_csv():
#     f = open('Data/Seed_pages.csv', 'w+', encoding='utf-8')
#     f.write('hotel,city,comment_page_url')
#     urls = [[
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D8%B3%D9%BE%DB%8C%D9%86%D8%A7%D8%B3-%D9%BE%D8%A7%D9%84%D8%A7%D8%B3/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-اسپیناس-پالاس'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A2%D8%B2%D8%A7%D8%AF%DB%8C/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-آزادی'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D9%87%D9%85%D8%A7/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-هما'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-استقلال'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D9%BE%D8%B1%D8%B4%DB%8C%D9%86-%D9%BE%D9%84%D8%A7%D8%B2%D8%A7/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-پرشین-پلازا'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D9%86%D9%82%D9%84%D8%A7%D8%A8/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-انقلاب'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D8%B3%D9%BE%DB%8C%D9%86%D8%A7%D8%B3-%D8%A8%D9%84%D9%88%D8%A7%D8%B1/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-اسپیناس-بلوار'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A8%D9%84%D9%88%D8%B7/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-بلوط'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D9%88%DB%8C%D9%86/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-اوین'], [
#                 'https://www.iranhotelonline.com/tehran-hotels/%D9%87%D8%AA%D9%84-%D8%A2%D9%85%D8%A7%D8%AA%DB%8C%D8%B3/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'تهران ', 'هتل-آماتیس'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D9%84%D9%85%D8%A7%D8%B3-2/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-الماس-2'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D9%84%D9%85%D8%A7%D8%B3/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-الماس'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D9%BE%D8%B1%D8%AF%DB%8C%D8%B3%D8%A7%D9%86/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-پردیسان'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D9%82%D8%B5%D8%B1-%D8%B7%D9%84%D8%A7%DB%8C%DB%8C/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-قصر-طلایی'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%A7%D9%84%D9%85%D8%A7%D8%B3-%D9%86%D9%88%DB%8C%D9%86/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-الماس-نوین'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%AF%D8%B1%D9%88%DB%8C%D8%B4%DB%8C/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-درویشی'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D9%87%D9%85%D8%A7-1/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-هما-1'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%A8%D8%B2%D8%B1%DA%AF-%D9%BE%D8%A7%D8%B1%DA%A9-%D8%AD%DB%8C%D8%A7%D8%AA/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-بزرگ-پارک-حیات'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D9%85%DB%8C%D8%A7%D9%85%DB%8C/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-میامی'], [
#                 'https://www.iranhotelonline.com/mashhad-hotels/%D9%87%D8%AA%D9%84-%D8%B3%DB%8C-%D9%86%D9%88%D8%B1/%D9%86%D8%B8%D8%B1%D8%A7%D8%AA/',
#                 'مشهد ', 'هتل-سی-نور']]
#     for i in range(len(urls)):
#         print(urls[i][0])
#         print(urls[i][1])
#         print(urls[i][2])
#         f.write('\n' + str(urls[i][2]) + ',' + str(urls[i][1]) + ',' + str(urls[i][0]))
#     f.close()
#
#
# store_seeds_csv()
#
#
#

# import os
# os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'








# import pandas as pd
# from Crawl_non_seed_pages import *
#
# df = pd.read_csv('Data/Seed_pages.csv')
#
# # category -> comment_page_url
#
# f = open('Data/Iran Hotels Data.csv', 'w+')
# f.write('hotel,city,subject,comment_time,enter_time,stay_duration,permanent_residence,travel_type,comment,user_score,')
#
# f.close()
#
# # print(df)
# for i in range(len(df['comment_page_url'])):
#     # print(df['comment_page_url'][i])
#     comment = crawl_url(df['comment_page_url'][i])
#     print(comment)
#     for key in comment:
#         f = open('Data/Iran Hotels Data.csv', 'a', encoding='utf-8')
#         # f.write('hotel,city,subject,time,comment,user_score')
#         f.write('\n' + str(df['hotel'][i]) + ',' + str(df['city'][i]) + ',' + str(comment[key]['subject']) + ',' + str(
#             comment[key][
#                 'comment_time']) + ',' + str(comment[key]['enter_time']) + ',' + str(
#             comment[key]['stay_duration']) + ',' + str(comment[key]['permanent_residence']) + ',' + str(
#             comment[key]['travel_type']) + ',' + str(comment[key]['comment']) + ',' + str(comment[key]['user_score']))
#         f.close()
#         # 'comment': comm, 'subject': subject, 'user_score': score, 'time': time
#     # f.close()



import pandas as pd

# # df = pd.read_csv('Data/Seed_pages.csv')
# df = pd.read_csv('Data/Iran Hotels Data.csv')
# # df['comment_time']
# for item in df:
#
#     print(item)
#     print(df[item])
#     print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
#


# import time
#
#
# def basic_func(x):
#     if x == 0:
#         return 'zero'
#     elif x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
#
# starttime = time.time()
# for i in range(0, 10):
#     y = i * i
#     time.sleep(2)
#     print('{} squared results in a/an {} number'.format(i, basic_func(y)))
#
# print('That took {} seconds'.format(time.time() - starttime))

# import time
# import multiprocessing
#
#
# def basic_func(x):
#     if x == 0:
#         return 'zero'
#     elif x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
#
# def multiprocessing_func(x):
#     y = x * x
#     # time.sleep(2)
#     print('{} squared results in a/an {} number'.format(x, basic_func(y)))
#
#
# if __name__ == '__main__':
#     starttime = time.time()
#     processes = []
#     for i in range(0, 10):
#         p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
#         processes.append(p)
#         p.start()
#
#     for process in processes:
#         process.join()
#
#     print('That took {} seconds'.format(time.time() - starttime))
#



from sklearn.pipeline import make_pipeline
import dask_ml.model_selection

def puls(a):
    a *= a
    return a


param_grid = {
    'a': [0.1, 1, 10],
}

# X, y = make_classification(n_samples=10_000)

pipe = make_pipeline(
    puls()
)
gs = dask_ml.model_selection.GridSearchCV(pipe, param_grid, scheduler='multiprocessing')

