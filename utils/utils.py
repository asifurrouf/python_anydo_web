class Uitilities(object):
    def __init__(self,driver):
        self.driver=driver

    def change_theme(self):
        '''change the theme into dark'''
        import time
        click_settings_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/div[3]/button')
        click_settings_icon.click()
        time.sleep(5)

        click_theme=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[5]/div[1]')
        click_theme.click()
        time.sleep(5)

        select_theme=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[4]/div/div/div/form/div[3]/div[1]/label')
        select_theme.click()
        time.sleep(5)
        click_settings_icon.click()
        time.sleep(5)

    def check_notification(self):
        '''checks updates notification'''
        import time
        click_notification_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/button[2]')
        click_notification_icon.click()
        time.sleep(1)
        click_notification_update=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/ul/li[1]/button')
        click_notification_update.click()
        time.sleep(2)
        click_notification_icon.click()
        time.sleep(2)

    def add_selection_feature(self):
        '''clicks on multiple selection icon and dismiss thw window later'''
        import time
        click_more_Option=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/button[3]')
        click_more_Option.click()
        time.sleep(1)
        click_multiple_selection=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button')
        click_multiple_selection.click()
        time.sleep(1)
        close_selection_window=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[2]/div/button[5]')
        close_selection_window.click()
        time.sleep(4)


    def create_tag(self):
        '''clicks on tag's plus(+) icon and NO, THANKS ltaer'''
        import time
        try:
            click_tag=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[4]/div[1]/div[2]/button[2]')
            click_tag.click()
            time.sleep(5)
            click_noThanks=self.driver.find_element_by_xpath('//button[contains(text(), "No")]')
            click_noThanks.click()
            time.sleep(10)
        except:
            pass

    def sign_out(self):
        '''signing out'''
        import time
        click_settings_icon=self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div/div/div[3]/button')
        click_settings_icon.click()
        time.sleep(5)

        my_profile=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]')
        my_profile.click()
        time.sleep(5)
        sign_out=self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]')
        sign_out.click()
        time.sleep(3)
