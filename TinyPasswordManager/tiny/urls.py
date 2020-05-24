from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # create new password
    path('pass/create/', views.PasswordCreate, name='pass_create'),

    # show all user passwords
    path('pass/show/', views.PasswordShow, name='pass_show'),

    # show password detail
    path('pass/<int:pk>', views.PasswordDetail, name='pass_detail'),

    path('pass/<int:pk>/delete/', views.PasswordDelete, name='pass_delete'),
]