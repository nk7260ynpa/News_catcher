#此程式碼會產生一個News_list檔案
#裡面會用#分隔標題與日期
#特別注意重新run一次後先前的紀錄會洗掉
#下一版本增加驗證檔案是否存在的功能

from bs4 import BeautifulSoup
import requests
import csv

url = input("輸入聯合報的第一頁")
file=open("News_list.csv","wt")
while True:
    html = requests.get(url).text
    sp = BeautifulSoup(html, "html.parser")
    all_url_part = sp.find("span", {"class": "s"})#此段找出下一頁
    all_links = all_url_part.find_all("a")
    link_title = all_links[-1].text
    Post_link = all_links[-1].get("href")
    url = "http://udndata.com" + Post_link
    data_of_title = sp.find_all("td", {"align": "left", "class": "title02"})  # 此行找標題
    data_of_date = sp.find_all("span", {"class": "date", "lang": "EN-US", "xml:lang": "EN-US"})  # 此行找日期


    if link_title == "最末頁":#此段解決最後一頁的錯誤
        date_num = 0
        for n_of_news in data_of_title:
            ht_title = n_of_news.find_all("a")  # 往下一行從HTML取出標題
            title = ht_title[0].text
            title = "".join(title.split())  # 去掉換行符號
            date = data_of_date[date_num].text[0:10]  # 此行從HTML取出日期
            date_num += 1
            news_list = [[title, "#" + date]]#以下三行存入檔案
            fileout = csv.writer(file)
            fileout.writerows(news_list)
        break


    for n_of_news in range(0, 10):
        ht_title = data_of_title[n_of_news].find_all("a")  # 往下一行從HTML取出標題
        title = ht_title[0].text
        title = "".join(title.split())  # 去掉換行符號
        date = data_of_date[n_of_news].text[0:10]  # 此行從HTML取出日期
        news_list=[[title,"#"+date]]#以下三行存入檔案
        fileout = csv.writer(file)
        fileout.writerows(news_list)



print("完成了")
file.close()