HomePageMap = dict(AccountXpath = "//input[@id='RJ_LoginForm_email']",
					PasswordXpath = "//input[@id='RJ_LoginForm_password']",
					LoginButtonXpath = "//input[@name='yt0']"
)

TicketPageMap = dict(TicketXpath = "//div[@id='milestone']//span[@class='num']",
				BookmarkXpath = "//div[@id='milestone']//a[@href='/reservation/bookmark/']",
				TicketAreaXpath = "//div[@id='milestone']/div[@class='suggest-inner']"
)


TimeSlotMap = dict(sixteenXpath = "//div[@id='weekly_slot_list']/table/tbody[4]/tr[9]/",
					sixteen30Xpath = "//div[@id='weekly_slot_list']/table/tbody[4]/tr[10]/",
					seventeenXpath = "//div[@id='weekly_slot_list']/table/tbody[4]/tr[11]/",
					seventeen30Xpath = "//div[@id='weekly_slot_list']/table/tbody[6]/tr[13]/",
					skypeXpath = "//ul[@id='howToLesson']//div[@class='label_container']/label[@class='checkboxlabel']",
					notMaterialXpath = "//form[@id='submitReservation']//div[@class='lesson_request_content request_block rjxRequestBlock']/ul[@class='request_list']/li[2]/div[@class='label_container']/label[@class='checkboxlabel']",
					weeklyNewsXpath = "//form[@id='submitReservation']//div[@class='lesson_request_content request_block rjxRequestBlock']/ul[@class='request_list']//ul[@class='request_list request_list_child rjxMaterialRequest']/li[3]/div",
					confirmXpath = "//form[@id='submitReservation']//input[@name='yt0']"
	)



