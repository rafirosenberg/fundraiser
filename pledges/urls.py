from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.pledge, name='pledge'),
    #url(r'^donor/', views.newDonor, name='donor' ),
)