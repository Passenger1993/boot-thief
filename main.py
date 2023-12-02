from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json
import time

useragent = UserAgent()
headers = {"user-agent":useragent.random,"Accept":"*/*"}
all_categories_dict = {}
page_urls = []
for i in range(1,11):
    if i == 1:
        page_urls.append("https://www.rendez-vous.ru/catalog/female/?filter%5Bvideo_review%5D=&filter%5Bcan_use_bonus%5D=&filter%5Bhas_stock%5D=&filter%5Bsort%5D%5Bfield%5D=&filter%5Bsort%5D%5Bdir%5D=&filter%5BexistenceShop%5D=0&filter%5Bseason%5D%5B0%5D=2&filter%5Bprice%5D%5Bmin%5D=2000&filter%5Bprice%5D%5Bmax%5D=8000&shopType%5BcityId%5D=445")
    else:
        page_urls.append(f"https://www.rendez-vous.ru/catalog/female/page/{i}/?filter%5Bvideo_review%5D=&filter%5Bcan_use_bonus%5D=&filter%5Bhas_stock%5D=&filter%5Bsort%5D%5Bfield%5D=&filter%5Bsort%5D%5Bdir%5D=&filter%5BexistenceShop%5D=0&filter%5Bseason%5D%5B0%5D=2&filter%5Bprice%5D%5Bmin%5D=2000&filter%5Bprice%5D%5Bmax%5D=8000&shopType%5BcityId%5D=445")
remove = [" ","\n","{","}","'"]
def info():
    for page in page_urls:
        responce = requests.get(url = page, headers=headers)
        (time.sleep(6))
        with open("Index.html", "a",encoding="utf-8") as file:
            file.write(responce.text)
        soup = BeautifulSoup(responce.text, "lxml")
        boots = soup.find("ul",class_ = "list-items list-items-catalog list-view-1 js-list-items")
        data = boots.find_all(class_ = "item")
        for element in data:
            inform = element["data-productinfo"]
            for el in remove:
                inform = inform.replace(el,"")
            inform = inform.replace(":",",").split(",")
            season = (inform[9].split("/"))[3]
            all_categories_dict[inform[1]] = {"Цена":inform[5],"Бренд":inform[7],"Сезон":season,"Цвет":inform[11]}
        print(all_categories_dict)
        print("#"*100)

    with open("Boots.json","w") as file:
        json.dump(all_categories_dict,file,indent=4,ensure_ascii=False)


if __name__ == "__main__":
    info()

