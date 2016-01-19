# creating a urlconf in the polls directory.
from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index, name='index'),
]
# ^$ means start^ of the url and $end of the url, so pretty much means empty
