#list of urls just for this section
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='register'),
]

