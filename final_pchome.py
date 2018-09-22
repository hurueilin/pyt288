from bs4 import BeautifulSoup
from selenium import webdriver
import time


# times: 捲動次數
def execute_times(times):
    for i in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


chrome_path = r"C:\chromedriver(2.32)\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = input('Enter the url you want to request: ')
driver.get(url)

# 讓driver捲動網頁至最下方
execute_times(10)

# 捲動完畢後再丟進soup
soup = BeautifulSoup(driver.page_source,"html.parser")


f = open('search_output.csv', 'w', encoding='big5')
f.write('title' + ',' + 'price\n')

total_items = 0
total_errors = 0

container = soup.find('div', id ='ItemContainer')
for each_item in container:
	try:
		
		# title = each_item.find('h5', class_='prod_name').find('a').text
		# title = each_item.select('dd[class="c2f"] > h5[class="prod_name"] > a')[0].text
		title = each_item.select_one('dd[class="c2f"] > h5[class="prod_name"] > a').text

		nick = each_item.select_one('dd[class="c2f"] > span[class="nick"]').text

		price = each_item.select_one('dd[class="c3f"] > ul[class="price_box"] > li > span > span').text

		print('標題:', title)
		print('價錢:', price)
		print(nick)
		print('----------------------')

		f.write(title + ',' + price + '\n')

		total_items += 1

	except:
		print('Something`s wrong')
		total_errors += 1

print('共找到{}筆資料'.format(total_items))
print('有{}處怪怪的，無法被讀出'.format(total_errors))

f.close()

# driver.close()