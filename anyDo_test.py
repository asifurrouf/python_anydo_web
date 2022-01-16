##importing necessary libraries
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from login.login import Login
from create_task.create_task import CreatTask
from create_task.create_list import CreateList
from utils.utils import Uitilities


#initiating browser executable path

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)


##openning url
driver.get("https://desktop.any.do/")
time.sleep(5)

login=Login(driver)
login.email('s.ahmed01@northsouth.edu')
time.sleep(4)

login.password('P@sswordf0ranydo')
time.sleep(4)
login.login()
time.sleep(20)
task=CreatTask(driver)
task.task()
task.write_task('My Friday Task')
time.sleep(10)
task.write_note('Hang out with friends')
task.set_reminder()
task.add_task()
time.sleep(15)
# task.create_subTask()
# task.write_subTask('Wake up early')

##########---creating list and adding items-----######
List=CreateList(driver)
List.create_list()
List.write_listName('My Shopping List')
List.add_listItem()
List.write_itemName('T-shirst')
time.sleep(5)
List.write_itemName('Pant')
time.sleep(5)
List.write_itemName('Mouse')
time.sleep(5)
List.write_itemName('Keyboard')
time.sleep(5)

#####-----------#######
Utility=Uitilities(driver)
time.sleep(5)
Utility.change_theme()
time.sleep(5)
Utility.check_notification()
time.sleep(5)
Utility.add_selection_feature()
time.sleep(10)
Utility.create_tag()
time.sleep(5)
Utility.sign_out()


