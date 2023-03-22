from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
# before all
wdriver=webdriver.Chrome("/Users/sebastianaravenasandoval/Documents/projects/Arquetipo-Python-BDD/selenium/webdriver/chromedriver")
def before_all(context):
   print('Before all executed')
   context.driver = webdriver.Chrome(projectname="Python BDD", jobname="Behave")
# before every scenario
def before_scenario(scenario, context):
   print('Before scenario executed')
# after every feature
def after_feature(scenario, context):
   print('After feature executed')
   allure.attach(wdriver.get_screenshot_as_png, name='!! Screenshot Captured !!', attachment_type=allure.attachment_type.PNG)
   
# after all
def after_all(context):
   print('After all executed')
   