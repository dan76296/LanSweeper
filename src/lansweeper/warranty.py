from log import Log
from datetime import date
import time

# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

import splinter

from assets import Assets
from exceptions import Exceptions
from file import File

import getpass

class LanSweeper:

    _url = ""
    username = ""
    password = getpass.getpass(prompt='Enter your password:')
    #executable_path = {'executable_path': "C:\\User Files\\lansweeper\\venv\\Scripts\\chromedriver.exe"}

    def __init__(self):
        self.browser = splinter.Browser('chrome')
        self.assets = Assets(self.browser)
        self.file = File()
        self.exceptions = Exceptions()
        self._login()

    def _login(self):
        self.browser.visit(self._url)
        self.browser.find_by_name('NameTextBox').fill(self.username)
        self.browser.find_by_name('PasswordTextBox').fill(self.password)
        self.browser.find_by_name('LoginButton').click()
        if self.browser.is_text_present('Dashboard'):
            print("Successfully logged in to Lansweeper")
        else:
            raise Exceptions.GenericLanSweeperError()

ls = LanSweeper()

log = Log()

data = ls.file.read_csv("warranty.csv", encoding='unicode_escape', headers=True)

filename = input("Enter your confirmation log csv:")

for entry in data:
    serial = entry['Serial Number']
    order_number = entry['Customer Order Number']
    end_date = entry['Original Warranty End Date']

    if ls.assets.browse_asset_page(serial):
        ls.assets.edit_asset()
        if ls.assets.browser.find_by_name('customfield1').value == '':
            ls.assets.set_items(order=order_number, warranty=end_date,custom1='Updated: 7th Jan 2020')
            ls.assets.set_textbox()
            ls.assets.save_asset()
            time.sleep(2)
            ls.file.append_csv(filename, (serial, 'Warranty Assigned'))
        else:
            log.info('Device already looked at')
            ls.assets.save_asset()
            time.sleep(2)
    else:
        ls.file.append_csv(filename, (serial, 'Not in LanSweeper'))
