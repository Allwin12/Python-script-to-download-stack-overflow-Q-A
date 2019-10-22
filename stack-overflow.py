from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pdfcrowd
from bs4 import BeautifulSoup

url = input('Enter the url, press space and then hit Enter: ')
print(url + "opening firefox...........")
driver = webdriver.Firefox()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get(url)

# get the page source

html_source = driver.page_source
soup = BeautifulSoup(html_source, "html.parser")

# optimising the html code to have only required data

# to get the style properties, so that the pdf will have the same style
head = soup.find('head')

# To get the question
question = soup.find("a", {"class": "question-hyperlink"}).contents[0]

# to get the portion of the html that contains only the answer, comments ignoring all the unwanted data
soup = soup.find("div", {"id": "mainbar"})

# form = soup.find("form", {"id": "post-form"}).replaceWith('')
# bottom_notice = soup.find("h2", {"class": "bottom-notice"}).replaceWith('')

question = '<h1>'+question+'</h1>'
# generate a new html code with only required data
html_source = str(question) + str(head) + str(soup)

# create a free account from pdf crowd and replace the following with your own username and API key or you can use mine
client = pdfcrowd.HtmlToPdfClient('allwinraju', '705d1ef50bf58f16f663e3a95aa47497')
file_name = url.split('/')[-1] + '.pdf'
print("Converting to pdf...")
pdf = client.convertStringToFile(html_source, file_name)
print("File " + file_name + "created")
driver.close()
