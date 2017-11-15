from django.conf.urls import url
from . import views

urlpatterns = [
    #home page_post
    url(r'^$', views.index, name='index'),

    # posts/1
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
]
