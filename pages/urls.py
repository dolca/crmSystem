from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('signin', views.signin, name="authentication.signin"),
    path('signup', views.signup, name="authentication.signup"),
    path('password-reset', views.password_reset, name="authentication.password_reset"),
    path('password-change', views.password_change, name="authentication.password_change"),
    path('lockscreen', views.lockscreen, name="authentication.lockscreen"),
    path('logout', views.logout, name="authentication.logout"),
    path('success', views.success_msg, name="authentication.success_msg"),
    path('twostep-verification', views.twostep_verification, name="authentication.twostep_verification"),
    path('404error', views.page_404_error, name="authentication.404_error"),
    path('500error', views.page_500_error, name="authentication.500_error"),
    path('503error', views.page_503_error, name="authentication.503_error"),
    path('offline', views.offline, name="authentication.offline"),

    path('starter', views.starter, name="pages.starter"),
    path('maintenance', views.maintenance, name="pages.maintenance"),
    path('coming-soon', views.coming_soon, name="pages.coming_soon")
]
