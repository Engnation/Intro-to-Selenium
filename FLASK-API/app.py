from flask import Flask, render_template, request
from selenium import webdriver

import json
import requests

app = Flask(__name__)

@app.route('/about') # <-this is a decorator, whenever you call the /about route, the about() function gets called.
def about():
    return 'Hello: User'

@app.route('/') #<- index route
def index():
    '''
    This function renders index.html with some pre-defined data
    '''
    return render_template('index.html', name='User', cities=['Mississauga','Brampton','Toronto'])

@app.route('/api')
def scrape_booking():
    '''
    This function scrapes bookings.com and returns a json list of hotel names
    '''
    # start Chrome session
    browser = webdriver.Chrome()

    # opening web site
    url = 'https://www.booking.com/'
    browser.get(url)

    # type in location
    search_input_el = browser.find_element_by_name('ss')
    search_input_el.send_keys('Mississauga')

    # click search button
    search_btn_el = browser.find_element_by_css_selector('button.sb-searchbox__button')
    search_btn_el.click()  

    # read results
    list = []
    result_els = browser.find_elements_by_css_selector('div.sr_item')
    for result in result_els:    
        name_el = result.find_element_by_class_name('sr-hotel__name')
        hotel_obj = {}
        hotel_obj['name'] = name_el.text
        list.append(hotel_obj)
        
    # close Chrome session
    browser.quit()

    return json.dumps(list)