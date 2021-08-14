from selenium.webdriver.common.by import By
from os.path import dirname,join

class OR:
    project_root = dirname(dirname(__file__))

    UserEmail_login_txBx         = (By.XPATH, "//input[@id='usernameOrEmail']")
    Continue_Btn                 = (By.XPATH, "//button[text()='Continue']")
    Password_txBx                = (By.XPATH, "//input[@id='password']")
    Header_myProfile             = (By.XPATH, "//h1[@class='formatted-header__title wp-brand-font']")
    First_Name_TxBx              = (By.XPATH, "//input[@id='first_name']")
    Last_Name_TxBx               = (By.XPATH, "//input[@id='last_name']")
    PublicDisplay_Name_TxBx      = (By.XPATH, "//input[@id='display_name']")
    Description_TxArea           = (By.XPATH, "//textarea[@id='description']")
    Gravatar_Profile_CheckBx     = (By.XPATH, "//*[@class='components-form-toggle__input']")
    Gravatar_Profile_Save_Btn    = (By.XPATH, "//*[text()='Save profile details']")
    Save_Profile_Details_Btn     = (By.XPATH, "//button[text()='Save profile details']")
    Profile_Link_Btn             = (By.XPATH, "//*[@class='button is-compact']")
    Add_Url_fld                  = (By.XPATH, "//*[@class ='popover__menu-item'][2]")
    Enter_Url_TxBx               = (By.XPATH, "//*[@placeholder='Enter a URL']")
    Enter_Description_TxBx       = (By.XPATH, "//*[@placeholder='Enter a description']")
    Add_Site_Button              = (By.XPATH, "//*[text()='Add Site']")
    Added_profile_link           = (By.XPATH, "//*[@class='profile-link__title']")
    delete_profile_link          = (By.XPATH, "//*[@class='button profile-link__remove is-borderless']")



