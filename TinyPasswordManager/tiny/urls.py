from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # create new password
    path('pass/create/', views.PasswordCreate, name='pass_create'),
]