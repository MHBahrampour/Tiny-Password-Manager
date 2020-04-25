from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # include urls.py from tiny application
    path('tiny/', include('tiny.urls')),
    # add URL maps to redirect the base URL to tiny application
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
