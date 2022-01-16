class CreateList(object):
    def __init__(self,driver):
        self.driver=driver

    def create_list(self):
        '''clicks on list plus(+) icon'''
        import time
        click_listIcon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]')
        click_listIcon.click()
        time.sleep(2)

    def write_listName(self,list_name):
        '''write list's name'''
        import time
        write_listName=self.driver.find_element_by_tag_name('textarea')
        write_listName.click()
        write_listName.send_keys(list_name)
        time.sleep(2)
        save_listName=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button[2]')
        save_listName.click()
        time.sleep(2)

    def add_listItem(self):
        '''click newly create list name to add items'''
        import time
        click_toAdd_listItem=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[4]/a/div[2]')
        click_toAdd_listItem.click()
        time.sleep(2)
    def write_itemName(self,item_name):
        '''write list's item name'''
        import time
        from selenium.webdriver.common.keys import Keys
        write_itemName=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/section/article/form/div/div/div/input[1]')
        write_itemName.click()
        write_itemName.send_keys(item_name)
        time.sleep(5)
        write_itemName.send_keys(Keys.RETURN)
        time.sleep(2)
