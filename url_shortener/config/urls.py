from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
]
