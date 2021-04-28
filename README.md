# iranhotelonline.com_Web_Crawler

Download and install webdriverchrome. You have to pay attention to the version of the webdriverchrome and your chrome browser.

Next, change the path of the webdriverchrome in Crawl_seed_pages.py and Crawl_non_seed_pages.py

In both files you will find:

driver = webdriver.Chrome(
        executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")

you should change this path.


# First Step:
1 - Open Pipeline_Crawl_Seed_Pages.py

2 - initial num_of_threads

3 - Run a function called run_seed_pipeline(num_of_thread)


# Second Step:
1 - Open Pipeline_Crawl_non_Seed_Pages.py

2 - initial num_of_threads

3 - Run a function called run_non_seed_pipeline(num_of_thread)


