import configparser

config=configparser.RawConfigParser()
config.read('C:/Users/thead/PycharmProjects/SeleniumNopcommerce/Configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

