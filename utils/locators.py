from selenium.webdriver.common.by import By
class LoginPageLocator(object):
    LOGIN_WITH_EMAIL_BUTTON\
        = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]')
    EMAIL_TEXTBOX = (By.TAG_NAME, 'input')
    EMAIL_SUBMIT_BTN = (By.XPATH, ('//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]'))
    PASSWORD_TEXTBOX = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]')

class HomePageLocator(object):
    CREATE_TASK_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/div[2]/div/button/span[2]')

    WRITE_TASK_TEXTBOX = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[1]/div/div/div/textarea')
    WRITE_NOTE_TEXTBOX = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea')
    WEEKLY_REMINDER_BTN = (By.XPATH, '//button[contains(text(), "Next")]')
    ADD_TASK_BTN = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button/strong')
    # SUB_CREATE_TASK = (By.XPATH, '/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/button/div')
    LIST_ICON = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]')
    LIST_NAME_TEXTBOX = (By.TAG_NAME, 'textarea')
    ITEM_NAME_TEXTBOX = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/section/article/form/div/div/div/input[1]')
    '''add enter button command for  adding the items'''


    SETTINGS_ICON = (By.XPATH, '//*[@id="root"]/div[2]/header/div/div/div[3]/button')
    THEME_OPTIONS = (By.XPATH, '/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[5]/div[1]')
    DARK_THEME = (By.XPATH, '/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[4]/div/div/div/form/div[3]/div[1]/label')
    NOTIFICATION_ICON = (By.XPATH, '//*[@id="root"]/div[2]/header/div/div/button[2]')
    NOTIFICATION_UPDATE = (By.XPATH, '/html/body/div[6]/div/div/div[1]/div/ul/li[1]/button')

    MULTIPLE_SELECTION_ICON = (By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button')
    MULTIPLE_SELECTION_CLOSE_ICON = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/button[5]')

    CREATE_TAG_BTN = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[4]/div[1]/div[2]/button[2]')
    NO_THANKS_BTN = (By.XPATH, '//button[contains(text(), "No")]')
    MY_PROFILE = (By.XPATH, '/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]')
    SIGN_OUT = (By.XPATH, '/html/body/div[6]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]')






