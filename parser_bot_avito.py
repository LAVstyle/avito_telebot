# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
from bs4 import BeautifulSoup

# def get_source_html(url):

#     # url = "https://www.avito.ru/tomsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104"
#     driver  = webdriver.Firefox(executable_path="D:\!!_AVL\Desktop\COMPUTER_SCIENCE\Python\Bots\Bot_3\geckodriver.exe")
    # driver.maximize_window()

    # try:
    #     driver.get(url=url)
    #     time.sleep(7)

    #     with open("index_selenium.html", 'w', encoding="utf-8") as file:
    #         file.write(driver.page_source)

    # except Exception as _ex:
    #     print(_ex)
    # finally:
    #     driver.close()
    #     driver.quit()
def get_links():
    with open("D:\!!_AVL\Desktop\index_selenium.html", 'r', encoding="utf-8") as file:
        src = file.read()
        soup = BeautifulSoup(src, 'html.parser')
        all_links = soup.find_all("div", class_="iva-item-titleStep-pdebR")
        for link in all_links:
            link = "https://www.avito.ru" + link.find("a").get("href")
            print(link)

## def get_items_urls(file_path):
#     with open(file_path) as file:
#         src = file.read()

#         bs = BeautifulSoup(src, "lxml")

#         all_links = bs.find_all("a", class_="iva-item-title")

#         for link in all_links:
#             return link

def main():
    # get_source_html("https://www.avito.ru/tomsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104")
    # print(get_items_urls(file_path=""))
    get_links()

if __name__=="__main__":
    main()



# request = requests.get(url)
#
