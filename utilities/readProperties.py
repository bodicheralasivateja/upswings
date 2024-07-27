import configparser
import os

config = configparser.RawConfigParser()
config.read(r"C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\upswings\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'BaseURL')
        return url

    @staticmethod
    def getEmailAddress():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
