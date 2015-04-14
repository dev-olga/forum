from django.conf.urls import patterns, url
import views

urlpatterns = patterns(''
   , url(r'^$', views.Index.as_view(), name='index')
   , url(r'^login/$', views.Login.as_view(), name='login')
   , url(r'^logout/$', views.Logout.as_view(), name='logout')
   , url(r'^register/$', views.Register.as_view(), name='register')
   #  , url(r'^$', views.category, name='category')
   , url(r'^(?P<subcategory_id>\d+)/', views.subcategory, name='subcategory')
   # , url(r'^(?P<thread_id>\d+)/', views.thread, name='thread')
   # , url(r'^(?P<post_id>\d+)/$', views.post, name='post')
)