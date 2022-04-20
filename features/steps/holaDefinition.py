import webbrowser
from behave import given,when,then
from selenium import webdriver
import time
class Hola:
    @given(u'abro la siguiente url')
    def step_impl(context):
        global wdriver
        wdriver=webdriver.Chrome("selenium/webdriver/chromedriver")
        wdriver.get("https://www.youtube.com/")
        wdriver.maximize_window()
        time.sleep(5)

@when(u'busque un video')
def step_impl(context):
    buscar= wdriver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
    buscar.send_keys("nate gentile")
    buscar.submit()