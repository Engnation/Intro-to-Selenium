import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#Opening website
url = 'https://google.ca'
browser.get(url)

#Type in search terms
search_input_el = browser.find_element_by_name('q')
search_input_el.send_keys('python')

#Press enter
search_input_el.send_keys(Keys.ENTER)

#Pause for user to see the results
time.sleep(8)

#Get results
result_els = browser.find_elements_by_class_name('yuRUbf')

#Iterate through results and print
for result in result_els:
    link_el = result.find_element_by_tag_name('a')
    print( link_el.get_attribute('href') )

#Close the browser to keep running instances from accumulating 
browser.quit()
