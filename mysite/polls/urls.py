# creating a urlconf in the polls directory.
from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
# ^$ means start^ of the url and $end of the url, so pretty much means empty
