
from django.conf.urls import url
from django.contrib import admin
from main.views import MultipleFormView, FormsList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MultipleFormView.as_view(), name='home'),
    url(r'^list/$', FormsList.as_view(), name='list'),
]
