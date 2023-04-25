
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
from selenium import webdriver
from allure_behave import hooks
import allure
import os
import time
import random

# before all
#

def before_all(context):
   print('Before all executed')
   driver_path = os.path.join(os.getcwd(), "selenium/webdriver/chromedriver")
   context.driver = webdriver.Chrome(driver_path)
   chrome_options = Options()
   #chrome_options.add_argument("--headless")
   chrome_options.add_argument('--start-maximized')
   context.driver = webdriver.Chrome(chrome_options=chrome_options)
# before every scenario
def before_scenario(scenario, context):
   print("before_scenario")
   #time.sleep(10)
# after every feature
def after_scenario(context, scenario):
    print("after_scenario")

def before_step(context, step):
   #allure.attach('Hello there!', name='attachment', attachment_type=allure.attachment_type.PNG)
   if not os.path.exists("assets/screenshots/"):
      os.makedirs("assets/screenshots/")
      print("dierectorio creado")
   print("dierectorio ya existe!")
   allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


def after_step(context, step):
   print("after_step")
   if step.status == "pass":
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


# after all
def after_all(context):
   print("after_all")
   context.driver.quit()
   os.system("sh allure-2.10.0/bin/allure serve --clean ../results      allure-2.10.0/results")
   
   