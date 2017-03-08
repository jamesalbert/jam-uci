#!/usr/bin/env python

"""submit.py

Usage:
  submit.py --course=<number> --assignment=<path> --name=<name>

Options:
  -h --help              Show this screen.
  --course=<number>      Course number
  --assignment=<path>    Full path to assignment
  --name=<name>          Name of eee folder

"""

from bs4 import BeautifulSoup
from docopt import docopt
from json import loads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re

url = 'https://eee.uci.edu'


def wait_for(cn):
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "myclass"))
        )
        return element
    except Exception:
        return False


def login():
    signin = driver.find_element_by_xpath("//input[@value='Secure Sign In']")
    signin.click()
    usern = driver.find_element_by_name('ucinetid')
    passw = driver.find_element_by_name('password')
    login = driver.find_element_by_name('login_button')
    usern.send_keys(conf['username'])
    passw.send_keys(conf['password'])
    login.click()
    wait_for('myclass')


def find_class():
    html = BeautifulSoup(driver.page_source, 'html.parser')
    all_courses = html.findAll('table', attrs={'class': 'myclass'})
    courses = [course for course in all_courses
               if course.find('span', text=re.compile(args['--course']))]
    upload_link = str()
    for course in courses:
        link = course.find('a', text=re.compile('Dropbox'))
        if link:
            upload_link = "{0}{1}".format(url, link['href'])
    driver.get(upload_link)
    wait_for('file-viewer')


def find_assignment():
    html = BeautifulSoup(driver.page_source, 'html.parser')
    link = html.find('a', text=re.compile(args['--name']))
    driver.get('{0}{1}'.format(url, link['href']))
    wait_for('module-wrapper')


def find_submission():
    html = BeautifulSoup(driver.page_source, 'html.parser')
    link = html.find('a', text=re.compile('AssignmentSubmission'))
    print('getting {0}'.format('{0}{1}'.format(url, link['href'])))
    driver.get('{0}{1}'.format(url, link['href']))
    wait_for('time_loaded')


def upload():
    link = '/toolbox/dropbox/index.php?op=uploadfileform'
    driver.get('{0}{1}'.format(url, link))
    driver.find_element_by_name('files0').send_keys(args['--assignment'])
    driver.find_element_by_id('upload').click()


if __name__ == '__main__':
    args = docopt(__doc__, version='submit.py 1.0')
    confpath = "{0}/.eee".format(os.path.expanduser('~'))
    conf = dict()
    if os.path.isfile(confpath):
        with open(confpath, 'r') as conffile:
            conf = loads(conffile.read())
    elif os.environ.get('EEE_USERNAME') and \
         os.environ.get('EEE_PASSWORD'):
         conf = dict(username=os.environ['EEE_USERNAME'],
                     password=os.environ['EEE_PASSWORD'])
    else:
        exit('username and password must be specified')
    driver = webdriver.Chrome(conf['chromedriver'])
    driver.get(url)
    login()
    find_class()
    find_assignment()
    find_submission()
    upload()
    driver.quit()
