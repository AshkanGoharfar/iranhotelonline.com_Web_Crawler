# iranhotelonline.com_Web_Crawler

Download and install webdriverchrome. You need to pay attention to the version of the webdriverchrome and your chrome browser.

Clone the project.

Next, change path of the webdriverchrome which is in first line of Data/Metadata.txt. For this perpose, you should find path of chromedriver.exe in your pc and write it in the Metadata.txt.

After that, change num_of_thread variable which is in the second line of Data/Metadata.txt. For this perpose, you should change the value in order to test your device capacity for execution of different number of threads.

After you find best number of threads, delete Iran Hotels Data.csv in Data folder and copy Iran Hotels Data.csv in github project to this path again.(Because you need empty Iran Hotels Data.csv for next step while Iran Hotels Data.csv is not empty due to the previous runs)

# Next Step:

You have 6 csv files which are Seed_Pages_Rouzbeh_i.csv (0<i<7). In each stage you should choose on of files and copy the file to Data folder, Next change name of csv file to Seed_Pages.csv and save the file.
Next, Run Pipeline_Crawl_non_Seed_Pages.py

After that, do this stage for next 5 csv files.


