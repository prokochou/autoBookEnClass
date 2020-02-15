from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import LocatorMode
from .BasePage import BasePage
from .BasePage import IncorrectPageExpection
from UIMap import HomePageMap, TicketPageMap, TimeSlotMap

from BestTestCase import BestTestCase
from selenium.webdriver.support.select import Select
import time
import names
import random
import datetime
# from datetime import datetime

class MainPage(object):

	def __init__(self, driver):
		super(MainPage, self).__init__(driver)

	def _verify_page(self):
		try:
			self.assertEqual(self.driver.title, "ログイン | オンライン英会話No.1 レアジョブ英会話")

		except:
			raise IncorrectPageExpection

	def _login(self):
		account = BestTestCase.get_account(self)
		password = BestTestCase.get_password(self)

		account_input = BasePage.find_element(self, "xpath", HomePageMap['AccountXpath'])
		account_input.send_keys(account)

		password_input = BasePage.find_element(self, "xpath", HomePageMap['PasswordXpath'])
		password_input.send_keys(password)
		
		# Click login button
		button = BasePage.wait_until_element_clickable(self, 10, "xpath", HomePageMap['LoginButtonXpath'])
		button.click()
		print('login passed')


	def _check_if_ticket(self):
		can_book = "予約できます"
		bodyText = BasePage.wait_until_element_clickable(self, 10, "xpath", TicketPageMap['TicketAreaXpath']).text
		print(bodyText)
		self.assertTrue(can_book in bodyText)

		# Go to tutor page
		tutor_dic = {
			"Rhech" : "https://www.rarejob.com/teacher_detail/16773/",
			"Jess" : "https://www.rarejob.com/teacher_detail/19240/",
			"Yana" : "https://www.rarejob.com/teacher_detail/25384/",
			"Velaine" : "https://www.rarejob.com/teacher_detail/24654/"
		}

		for m in tutor_dic:
			print(m, tutor_dic[m])
			BestTestCase.navigate_to_page(self, tutor_dic[m])

			# Check time difference
			now = datetime.datetime.now().strftime("%H:%M")
			compared_time = '16:00' # Because of time zone
			if (now < compared_time):
				range_start = 2
				range_end = 3
			else:
				range_start = 1
				range_end = 2	
			
			for i in range(range_start, range_end): 
				time_map_ls = ['seventeenXpath','sixteen30Xpath','seventeen30Xpath'] 

				for x in range(len(time_map_ls)):
					print(time_map_ls[x])
					slotPath = TimeSlotMap[time_map_ls[x]] + "td[" + str(i) + "]"

					slot_text = BasePage.wait_until_element_clickable(self, 10, "xpath", slotPath).text
						
					print(slot_text)
					string = "予約可能"
					if string in slot_text:
						slot_button = BasePage.wait_until_element_clickable(self, 10, "xpath", slotPath)
						slot_button.click()
			
						select_skype = BasePage.wait_until_element_clickable(self, 10, "xpath",  TimeSlotMap['skypeXpath'])
						select_skype.click()

						outMaterial = BasePage.wait_until_element_clickable(self, 10, "xpath", TimeSlotMap['notMaterialXpath'])
						outMaterial.click()

						weekly_news = BasePage.wait_until_element_clickable(self, 10, "xpath", TimeSlotMap['weeklyNewsXpath'])
						weekly_news.click()
						print('pass')

						confirm_button = BasePage.wait_until_element_clickable(self, 10, "xpath", TimeSlotMap['confirmXpath'])
						confirm_button.click()
						time.sleep(3)
						break

	def _get_timestamp(self):
		# now = datetime.now()
		now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")		
		print("now =", now)







