from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_display_website(self):  
        # User has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Receipts', self.browser.title)   

        # She is sees the signup button and click to sign-up for an account
        signuplink = self.browser.find_element_by_id('signuplink')
        self.assertEquals(signuplink.text,'Sign up')

        # She is invited to enter a username, email and password 2 times

        # She is invited to Login

        # She is invited to create a category

        # She is invited to save a first receipt


        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

