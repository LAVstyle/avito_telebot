from bs4 import BeautifulSoup
from selenium import webdriver
import time


url = "https://www.avito.ru/tomsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104"


def get_sourse_html():

    url = "https://www.avito.ru/tomsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104"
    driver  = webdriver.Edge(executable_path="D:\!!_AVL\Desktop\COMPUTER_SCIENCE\Python\Bots\Bot_3\msedgedriver.exe")
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(4)

        with open("")   ###################################
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()

        bs = BeautifulSoup(src, "lxml")

        all_links = bs.find_all("a", class_="iva-item-title")

        for link in all_links:
            return link

def main():
    print(get_items_urls(file_path=""))


if __name__=="__main__":
    main()



# request = requests.get(url)
#
