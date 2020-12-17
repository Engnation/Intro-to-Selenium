import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#Opening website
url = 'https://booking.com/'
browser.get(url)

#Type in search terms
search_input_el = browser.find_element_by_name('ss')
search_input_el.send_keys('Frankfurt')

#Find search button element and click on it
search_btn_el = browser.find_element_by_css_selector('button.sb-searchbox__button')
search_btn_el.click()

#Collect a list of Selenium web elements for each instance of the specified div
result_els = browser.find_elements_by_css_selector('div.sr_item')

#Iterate through elements to search for and print each hotel name
for result in result_els:
    name_el = result.find_element_by_class_name('sr-hotel__name')
    print( name_el.text )

#Pause for user to see the results
time.sleep(8)

#Close the browser to keep running instances from accumulating 
browser.quit()



