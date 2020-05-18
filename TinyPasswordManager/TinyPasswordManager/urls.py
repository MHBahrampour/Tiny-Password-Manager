from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf.urls import url
from tiny import views as core_views

urlpatterns = [
    # admin site
    path('admin/', admin.site.urls),

    # include urls.py from tiny application
    path('tiny/', include('tiny.urls')),

    # add URL maps to redirect the base URL to tiny application
    path('', RedirectView.as_view(url='tiny/', permanent=True)),

    # for signin
    path('signin/', include('django.contrib.auth.urls')),

    # for signup
    url(r'^signup/$', core_views.signup, name='signup'),
]
