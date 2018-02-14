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

        # She notices the page title and header mention receipts
        self.assertIn('Receipts', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Receipts',header.text)


        # She is sees the signup button and click to sign-up for an account
        signuplink = self.browser.find_element_by_link_text('Sign up')
        self.assertEquals(signuplink.get_attribute('href'),'http://localhost:8000/signup/')

    def test_can_signup_from_homepage(self):
        self.browser.get('http://localhost:8000')
        signuplink = self.browser.find_element_by_link_text('Sign up')

        signuplink.click()
        time.sleep(10)

        # Signup page invite to enter a username, email and password 2 times
        username_input = self.browser.find_element_by_name('username')
        email_input = self.browser.find_element_by_name('email')
        password1_input = self.browser.find_element_by_name('password1')
        password2_input = self.browser.find_element_by_name('password2')

        # She is invited to Login

        # She is invited to create a category

        # She is invited to save a first receipt


        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

