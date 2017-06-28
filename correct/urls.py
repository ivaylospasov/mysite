from django.conf.urls import url
from correct import views

app_name = 'correct'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^text/$', views.original_input_form, name='original_input_form'),
    url(r'^ready/$', views.ready, name='ready'),
    url(r'^ready/(?P<id>\d+)/$', views.detail, name='detail')
    ]
