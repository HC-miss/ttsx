from django.conf.urls import url
from account import views


app_name = 'account'
urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'register/', views.register, name='register'),
]
