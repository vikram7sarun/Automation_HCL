from objectRepo.object_repository import OR
from utils.services import Services



class ProfilePage:

    def __init__(self, driver):
        self.driver = driver


    def user_login(self):
        s = Services(self.driver)
        email = s.config()['email']
        password = s.config()['password']
        s.setText(OR.UserEmail_login_txBx,email)
        s.setText(OR.UserEmail_login_txBx, password)
        s.click(OR.Continue_Btn)

    def profile_enter(self):
        s = Services(self.driver)
        first_name = s.config()['First_Name']
        last_name = s.config()['Last_Name']
        public_display_name = s.config()['Public_Display_Name']
        about_me = s.config()['About_me']
        s.is_element_displayed(OR.Header_myProfile)
        s.setText(OR.First_Name_TxBx, first_name)
        s.setText(OR.Last_Name_TxBx, last_name)
        s.setText(OR.PublicDisplay_Name_TxBx, public_display_name)
        s.setText(OR.Description_TxArea, about_me)
        s.click(OR.Gravatar_Profile_CheckBx)


    def profile_links(self):
        s = Services(self.driver)
        profile_link = s.config()['Profile_Link']
        Url = s.config()['Profile_Link']
        Desc = s.config()['description']
        s.click(OR.Profile_Link_Btn)
        s.click(OR.Add_Url_fld)
        s.setText(OR.Enter_Url_TxBx,Url)
        s.setText(OR.Enter_Description_TxBx,Desc)
        s.click(OR.Add_Site_Button)
        s.is_element_displayed(OR.Added_profile_link)

    def user_login_with_invalid_Cred(self):
        s = Services(self.driver)
        email = s.config()['invalid_email']
        password = s.config()['password']
        s.setText(OR.UserEmail_login_txBx,email)
        s.setText(OR.UserEmail_login_txBx, password)
        s.click(OR.Continue_Btn)

    def delete_profile_link(self):
        s = Services(self.driver)
        s.click(OR.delete_profile_link)

    def hide_Gravatar_Profile(self):
        s = Services(self.driver)
        s.click(OR.Gravatar_Profile_CheckBx)
        s.click()
