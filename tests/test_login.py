import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig

class Test_Login(BaseClass):

    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self):
        log = self.getLogger()
        log.info("****Started Login Test****")
        homepage=LoginPage(self.driver)
        homepage.setUserName(self.username)
        homepage.setPassword(self.password)
        homepage.clickLogin()
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            log.info("****Login test passed ****")
            assert True
        else:
            log.error("****Login test failed ****")
            self.driver.save_screenshot("C:/PycharmProject/Selenium_practice/reports/screenshot/test_homePageTitle.png")
            assert True
        time.sleep(5)





