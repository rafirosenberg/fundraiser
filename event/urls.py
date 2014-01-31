from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^update_total', views.updateTotal),
    url(r'^update_recent', views.updateRecent),
    url(r'^update_top', views.updateTop),
)