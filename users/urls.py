from django.urls import path

from . import views

app_name='users'


urlpatterns = [
    path('login/', views.f_login, name='f_login'),
    path('sign_up/', views.f_sign_up, name='f_sign_up'),
    path('logout/',views.logoutUser,name='logout')
    
]