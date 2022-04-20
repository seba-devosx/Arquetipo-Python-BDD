
from site import execusercustomize
from selenium import webdriver
from behave import given,when,then
import time
class hakatool:
    @given(u'ingreso a la siguiente url "{url}"')
    def step_impl(context,url):
        global wdriver
        wdriver=webdriver.Chrome("selenium/webdriver/chromedriver")
        wdriver.get(url)
        wdriver.maximize_window()
        time.sleep(5)


    @when(u'seleccione el apartado de hakatool')
    def step_impl(context):
        hktool=wdriver.find_element_by_xpath("/html/body/div[2]/header/div/div/nav/div[3]/ul/li[2]/a")
        hktool.click()
        time.sleep(5)
        

    @when(u'seleccione formulario')
    def step_impl(context):
        hktoolform= wdriver.find_element_by_xpath("/html/body/app-root/app-cardsmenu/div[2]/div/div/div[2]/div/div")
        wdriver.execute_script("arguments[0].scrollIntoView(true);",hktoolform)
        hktoolform.click()
        #time.sleep(5)
        #wdriver.close()


    @when(u'ingrese el nombre {nombre} ,{correo} ,{dir1} ,{dir2}')
    def step_impl(context,nombre,correo,dir1,dir2):
        hktoolname=wdriver.find_element_by_xpath("/html/body/app-root/app-forms/div[2]/div[2]/div[1]/app-basic-form/div/div[2]/form/div/div[1]/input")
        hktoolname.send_keys(nombre)

        hktoolcorreo=wdriver.find_element_by_xpath("/html/body/app-root/app-forms/div[2]/div[2]/div[1]/app-basic-form/div/div[2]/form/div/div[2]/input")
        hktoolcorreo.send_keys(correo)

        hktooldir1=wdriver.find_element_by_xpath("/html/body/app-root/app-forms/div[2]/div[2]/div[1]/app-basic-form/div/div[2]/form/div/div[3]/input")
        hktooldir1.send_keys(dir1)

        hktooldir2=wdriver.find_element_by_xpath("/html/body/app-root/app-forms/div[2]/div[2]/div[1]/app-basic-form/div/div[2]/form/div/div[4]/input")
        hktooldir2.send_keys(dir2)
        
        hktoolbt=wdriver.find_element_by_xpath("/html/body/app-root/app-forms/div[2]/div[2]/div[1]/app-basic-form/div/div[2]/form/div/button")
        hktoolbt.click()