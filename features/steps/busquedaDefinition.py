
from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Busqueda:

    @given(u'ingreso a la url "{url}"')
    def step_impl(context,url):
        context.driver.get(url)
        context.driver.maximize_window()
        time.sleep(5)

    @when(u'seleccione el filtro')
    def step_impl(context):
        context.driver.find_element(By.XPATH,"//*[@id='searchbox']").click()
        time.sleep(5)


    @when(u'ingrese el nombre de la marca {name}')
    def step_impl(context,name):
        find_name=context.driver.find_element(By.XPATH,"//*[@id='searchbox']")
        find_name.send_keys(name)