#list of urls just for this section
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.upload_csv, name='upload_csv'),
]

