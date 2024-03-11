from django.views.generic import TemplateView


class PagesView(TemplateView):
    pass


signin = PagesView.as_view(template_name="pages/authentication/auth_signin.html")
signup = PagesView.as_view(template_name="pages/authentication/auth_signup.html")
password_reset = PagesView.as_view(template_name="pages/authentication/auth_password_reset.html")
password_change = PagesView.as_view(template_name="pages/authentication/auth_password_change.html")
lockscreen = PagesView.as_view(template_name="pages/authentication/auth_lockscreen.html")
logout = PagesView.as_view(template_name="pages/authentication/auth_logout.html")
success_msg = PagesView.as_view(template_name="pages/authentication/auth_success.html")
twostep_verification = PagesView.as_view(template_name="pages/authentication/auth_twostep_verification.html")
page_404_error = PagesView.as_view(template_name="pages/authentication/error_404.html")
page_500_error = PagesView.as_view(template_name="pages/authentication/error_500.html")
page_503_error = PagesView.as_view(template_name="pages/authentication/error_503.html")
offline = PagesView.as_view(template_name="pages/authentication/error_offline.html")

starter = PagesView.as_view(template_name="pages/starter.html")
maintenance = PagesView.as_view(template_name="pages/maintenance.html")
coming_soon = PagesView.as_view(template_name="pages/coming_soon.html")
