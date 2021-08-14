import pytest
from utils.services import Services
from pages.profile_page import ProfilePage

@pytest.mark.usefixtures("driver_setup")
class TestProfile:


    @pytest.mark.smoke
    def test_Login(self):
        ProfilePage.user_login()

    @pytest.mark.smoke
    def test_profile(self):
        ProfilePage.user_login()
        ProfilePage.profile_enter()

    @pytest.mark.smoke
    def test_profile_Link(self):
        ProfilePage.user_login()
        ProfilePage.profile_links()

    @pytest.mark.smoke
    def test_Login_with_Invalid_Cred(self):
        ProfilePage.user_login_with_invalid_Cred()

    @pytest.mark.smoke
    def test_Delete_profile_Link(self):
        ProfilePage.delete_profile_link()

    @pytest.mark.smoke
    def test_hide_Gravatar_Profile(self):
        ProfilePage.hide_Gravatar_Profile()

