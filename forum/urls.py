from django.conf.urls import patterns, url
import views

urlpatterns = patterns(''
   , url(r'^$', views.Index.as_view(), name='index')
   , url(r'^login/$', views.Login.as_view(), name='login')
   , url(r'^logout/$', views.Logout.as_view(), name='logout')
   , url(r'^register/$', views.Register.as_view(), name='register')
   , url(r'^(?P<id>\d+)/', views.SubCategory.as_view(), name='subcategory')
   , url(r'^thread/(?P<id>\d+)/', views.Thread.as_view(), name='thread')
)