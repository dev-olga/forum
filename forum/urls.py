from django.conf.urls import patterns, url
import views

urlpatterns = patterns(''
    , url(r'^$', views.index, name='index')
   #  , url(r'^$', views.category, name='category')
    , url(r'^forum/(?P<subcategory_id>\d+)/', views.subcategory, name='subcategory')
   , url(r'^(?P<thread_id>\d+)/', views.thread, name='thread')
   # , url(r'^(?P<post_id>\d+)/$', views.post, name='post')
)