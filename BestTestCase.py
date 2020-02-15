from selenium import webdriver

from Constants import TT_Constants
import unittest
from selenium.webdriver.chrome.options import Options

class BestTestCase(object):

	def setup(self):
	
		if TT_Constants["Browser"] == 'firefox':
			self.driver = webdriver.Firefox()
			self.driver.maximize.window()
		elif TT_Constants["Browser"] == 'chrome':
			chrome_options = Options()  
			# chrome_options.add_argument("--headless")
			self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
			# self.driver.maximize.window()
		elif TT_Constants["Browser"] == 'ie':
			self.driver = webdriver.Ie()
			self.driver.maximize.window()
		else:
			raise Exception("This browser is not supported at the moment.")
	
	def navigate_to_page(self, url):
		self.driver.get(url)

	def get_current_url(self):
		return self.driver.current_url

	def get_account(self):
		return TT_Constants["UserName"]

	def get_password(self):
		return TT_Constants["Password"]

	def tearDown(self):
		self.driver.quit()

