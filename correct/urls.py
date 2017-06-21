from django.conf.urls import url
from correct import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'news/', views.news_input_form, name='news_input_form')
    ]
