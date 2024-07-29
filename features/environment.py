from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
import os

def before_all(context):
    print('Before all executed')
    context.driver = webdriver.Chrome("helpers/selenium/webdriver/chromedriver")

def before_scenario(context, scenario):
   print('Before scenario executed')
   
def after_step(context,step):
   print('After step executed')
   try:
         # Capturar la captura de pantalla y adjuntar a Allure
         allure.attach(context.driver.get_screenshot_as_png(), name=f'Screensho-{step}', attachment_type=AttachmentType.JPG)
   except Exception as e:
         print(f"Error al tomar la captura de pantalla: {e}")
         
def after_feature(context, feature):
   print('After feature executed')
   

def after_all(context):
    print('After all executed')
    #ejecuta comando para levantar el reporte de allure 
    os.popen('helpers/allure-2.30.0/bin/allure serve helpers/allure-2.30.0/allure-result')