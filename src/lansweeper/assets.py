import collections
from selenium.webdriver.common.keys import Keys
from log import Log
from exceptions import Exceptions


class Assets:

    Key = collections.namedtuple('Key', ['name', 'identifier', 'element_type'])

    allowed_keys = {
        'state': ('state', 'dropdown'),
        'assetname': ('assetname', 'textbox'),
        'ipaddress': ('ipaddress', 'textbox'),
        'manufacturer': ('manufacturer', 'textbox'),
        'model': ('model', 'textbox'),
        'domain': ('domain', 'textbox'),
        'serial': ('serial', 'textbox'),
        'dnsname': ('DNSName', 'textbox'),
        'fqdn': ('FQDN', 'textbox'),
        'systemsku': ('systemSKU', 'textbox'),
        'purchased': ('purchased', 'textbox'),
        'warranty': ('warranty', 'textbox'),
        'contact': ('contact', 'textbox'),
        'location': ('location', 'textbox'),
        'building': ('building', 'textbox'),
        'department': ('department', 'textbox'),
        'branchoffice': ('branchoffice', 'textbox'),
        'barcode': ('barcode', 'textbox'),
        'order': ('order', 'textbox'),
        'lastpatched': ('lastpatched', 'textbox'),
        'lastbackup': ('lastbackup', 'textbox'),
        'lastimage': ('lastimage', 'textbox'),
        'custom1': ('customfield1', 'textbox'),
        'custom2': ('customfield2', 'textbox'),
        'custom3': ('customfield3', 'textbox')
    }

    def __init__(self, browser):
        self.browser = browser
        self._items = {}
        self.log = Log()

    def browse_asset_page(self, value):
        #self.browser.driver.clear()
        self.browser.find_by_name('q').fill(value)
        self.browser.driver.find_element_by_name('q').send_keys(Keys.RETURN)
        if self.browser.is_text_present('Asset options'):
            self.log.info(f'Successfully browsed to asset page for {value}')
            return True
        else:
            self.log.error(f'Something went wrong whilst browsing to asset page for {value}, please ensure you are searching for an asset id/serial number.')
            return False

    def edit_asset(self):
        return self.browser.click_link_by_partial_text('Edit asset')

    def get_value(self):
        for key, value in self._items:
            result = self.browser.find_by_name(self.allowed_keys[key][0]).value
            self.log.info(f'{key} : {result}')

    def set_items(self, **kwargs):
        self._items.update((key, value) for key, value in kwargs.items() if key in self.allowed_keys)
        for key, value in kwargs.items():
            if key in self.allowed_keys:
                self.log.info(f'{key} : {value}')

    def set_textbox(self):
        for key, value in self._items.items():
            self.browser.fill(self.allowed_keys[key][0], value)

    def set_dropdown(self, key, value):
        raise NotImplementedError

    def upload_picture(self):
        raise NotImplementedError

    def save_asset(self):
        return self.browser.click_link_by_partial_text('Save asset')

    def delete_asset(self):
        raise NotImplementedError

