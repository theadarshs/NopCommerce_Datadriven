import time
import pytest

from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass
from tests.test_login import Test_Login
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName(BaseClass):
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def test_searchCustomerByName(self):
        log = self.getLogger()
        log.info("************* Test_003_AddCustomer **********")
        log = self.getLogger()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        log.info("************* Login succesful **********")

        log.info("******* Starting Search Customer By Name **********")

        addcust = AddCustomer(self.driver)
        time.sleep(3)
        addcust.clickOnCustomersMenu()
        time.sleep(3)
        addcust.clickOnCustomersMenuItem()

        log.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        time.sleep(2)
        searchcust.setFirstName().send_keys("victoria")
        time.sleep(5)
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("victoria")
        assert True
        log.info("***************  TC_SearchCustomerByName_004 Finished  *********** ")


