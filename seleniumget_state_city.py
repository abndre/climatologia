#Frameworks
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

#Link
link = 'https://www.climatempo.com.br/climatologia/2/santos-sp'

#Open and send link to browser
browser = webdriver.Chrome()
browser.get(link)

#Open pop up stat and city
openpopustat =browser.find_element_by_xpath("//*[@class='left font18 link-rodape icon-pin-map2']")
openpopustat.click()

#Wait for load pop
time.sleep(5)

#select all stat from popup
liststat=browser.find_element_by_id("sel-state-geo")
llistastat = liststat.text.split('\n')

z=browser.find_element_by_id("sel-state-geo")
options = [x for x in z.find_elements_by_tag_name("option")]
diciostat_abrev = {}
for element in options:
    diciostat_abrev[element.text]=element.get_attribute("value")
    #print(element.get_attribute("value"),element.text)
print(diciostat_abrev)

#Show all stats
print(llistastat)


#TODO Here we get all city from stat
dicio_stat_city = {}
for value in llistastat:
    #select state
    select = Select(browser.find_element_by_id('sel-state-geo'))
    select.select_by_visible_text(value)

    time.sleep(5)

    z=browser.find_element_by_id("sel-city-geo")
    options = [x for x in z.find_elements_by_tag_name("option")]
    diciocity_number = {}
    for index, element in enumerate(options):
        if not index ==0:
            diciocity_number[element.text]=element.get_attribute("value")

    dicio_stat_city[value]=diciocity_number

#Show dicio with stat city
print(dicio_stat_city)
#browser.quit()

browser.quit()
