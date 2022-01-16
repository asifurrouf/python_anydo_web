class Login(object):


    def __init__(self,driver):
        self.driver=driver

    def email(self,email_name):
        import time
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]').click()
        time.sleep(30)
        self.driver.find_element_by_tag_name('input').click()
        self.driver.find_element_by_tag_name('input').send_keys(email_name)
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/button').click() #email submit btn
        

    def password(self,pass_name):
        import time
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input').send_keys(pass_name)
     

    def login(self):
        '''clicks on log log in button'''
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]').click()