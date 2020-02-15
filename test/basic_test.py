
import __init__
from Constants import TT_Constants
from Constants import LocatorMode
from BestTestCase import BestTestCase
from pages.MainPage import MainPage
import time
import unittest
import nose
from nose.plugins.attrib import attr


class CheckLive(unittest.TestCase):

    def setUp(self):

        super(CheckLive, self).setUp()
        BestTestCase.setup(self)
        BestTestCase.navigate_to_page(self, TT_Constants["Base_URL"])

    # @attr(priority="high")
    def test_checkLive(self):

        MainPage._verify_page(self)
        MainPage._login(self)
        MainPage._check_if_ticket(self)
        MainPage._get_timestamp(self)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





