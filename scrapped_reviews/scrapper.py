from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as BS
import csv
import math
import re

import os

mobile_phones_dict = {
    "B086978F2L": "Redmi 9A (Sea Blue, 2Gb Ram, 32Gb Storage)",
    "B086977TR6": "Redmi Note 9 (Pebble Grey, 4GB RAM 64GB Storage)",
    "B07HGJJ559": "Samsung Galaxy M21 (Midnight Blue, 4GB RAM, 64GB Storage)",
    "B077PWBC78": "Redmi Note 9 Pro (Interstellar Black, 4GB RAM, 64GB Storage)",
    "B086985T6R": "Redmi 9 (Carbon Black, 4GB RAM, 64GB Storage)",
    "B07XVMDRZY": "Apple iPhone 11 (64GB)  Black (EarPods & Power Adapter in The Box)",
    "B07DJCJBB3": "Samsung Galaxy M31s (Mirage Blue, 6GB RAM, 128GB Storage)",
    "B085J1J32G": "Samsung Galaxy M51 (Electric Blue, 6GB RAM, 128GB Storage)",
    "B08695ZSP6": "OnePlus Nord 5G (Gray Onyx, 8GB RAM, 128GB Storage)",
    "B078BNQ318": "OnePlus 8 (Glacial Green 6GB RAM+128GB Storage)",
    "B089MS3GLM": "Samsung Galaxy M01 Core (Blue, 1GB RAM, 16GB Storage)",
    "B086KCDPMR": "Oppo A52 (Twilight Black, 6GB RAM, 128GB Storage)"
}


chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")

# driver with path currently available in this folder
path_to_driver = './chromedriver'



driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=path_to_driver)




# grab the title
# if soup.find('a', {'data-hook': 'product-link'}):
#     product_title = soup.find('a', {'data-hook': 'product-link'})
#     if product_title.text:
#         product_title = str(product_title.text)
#     else:
#         product_title = 'No title found'
# else:
#     product_title = 'No title found'

# print(product_title)

review_dict = {}

for code, title in mobile_phones_dict.items():

    base_url = "https://www.amazon.in/product-reviews/{0}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews".format(code)
    driver.get(base_url)
    source = driver.page_source
    soup = BS(source,'html.parser')

    total_reviews = soup.find('div', {'data-hook': 'total-review-count'})
    if total_reviews:
        total_reviews = int(total_reviews.text.replace(",","").split()[0])
        page_count = int(math.ceil(total_reviews/10))
        print(page_count)

    
    reviews = []
    for i in range(1,max(5,page_count-2)):
        if len(reviews) <= 120:    
            url = base_url + "&pageNumber={}".format(i)
            driver.get(url)

            source = driver.page_source
            soup = BS(source,'html.parser')

            reviews_body = soup.find('div', {'data-hook': 'review'})
            review_text = soup.find_all('span', {'data-hook': 'review-body'})
            review_text = [rev.text.replace('\U0001f44d', '').replace('\U0001f4a9', '') for rev in review_text]
            for review in review_text:
                review = str(review).strip()
                if len(review) > 20:
                    reviews.append(review)
                    print(review)
        else: 
            break

    review_dict[code] = reviews

    file_name = "{0}-{1}.csv".format(code,title)
    with open(file_name, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(reviews)



driver.close()




# reviews = []
# for i in range(1,max(5,page_count-2)):
#     url = base_url + "&pageNumber={}".format(i)
#     driver.get(url)

#     source = driver.page_source
#     soup = BS(source,'html.parser')
#     # review = {}

#     reviews_body = soup.find('div', {'data-hook': 'review'})
#     review_text = soup.find_all('span', {'data-hook': 'review-body'})
#     review_text = [rev.text.replace('\U0001f44d', '').replace('\U0001f4a9', '') for rev in review_text]
#     for review in review_text:
#         reviews.append(review.strip())
#         print(review)

#     driver.close()

# driver.close()


# url = "https://www.amazon.in/b?node=1389401031&pf_rd_r=WWDVPSS12WQVMG083Z23&pf_rd_p=b262e6ae-7cb7-458f-aeb1-de2bc6b14c78&nocache=1603025857846"
# driver.get(url)
# source = driver.page_source
# soup = BS(source, 'html.parser')
# all_links = soup.find_all(
#     'a', {'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})

# for each in all_links:
#     product = re.search(r'/dp/(.*?)/ref=', str(each))
#     if product:
#         print(product.group(1))
# # print(all_links)
# driver.close()

# B086978F2L - Redmi 9A (Sea Blue, 2Gb Ram, 32Gb Storage)
# B086977TR6 - Redmi Note 9 (Pebble Grey, 4GB RAM 64GB Storage)
# B07HGJJ559 - Samsung Galaxy M21 (Midnight Blue, 4GB RAM, 64GB Storage)
# B077PWBC78 - Redmi Note 9 Pro (Interstellar Black, 4GB RAM, 64GB Storage)-
# B086985T6R - Redmi 9 (Carbon Black, 4GB RAM, 64GB Storage)
# B07XVMDRZY - Apple iPhone 11 (64GB) - Black (EarPods & Power Adapter in The Box)
# B07DJCJBB3 - Samsung Galaxy M31s (Mirage Blue, 6GB RAM, 128GB Storage)
# B085J1J32G - Samsung Galaxy M51 (Electric Blue, 6GB RAM, 128GB Storage)
# B08695ZSP6 - OnePlus Nord 5G (Gray Onyx, 8GB RAM, 128GB Storage)
# B078BNQ318 - OnePlus 8 (Glacial Green 6GB RAM+128GB Storage)
# B089MS3GLM - Samsung Galaxy M01 Core (Blue, 1GB RAM, 16GB Storage)
# B086KCDPMR - Oppo A52 (Twilight Black, 6GB RAM, 128GB Storage)

