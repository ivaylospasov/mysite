from django.conf.urls import url
from correct import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'text/', views.original_input_form, name='original_input_form')
    ]
