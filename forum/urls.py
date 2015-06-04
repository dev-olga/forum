from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^account/login/$', views.LoginView.as_view(), name='login'),
    url(r'^account/logout/$', views.logout_view, name='logout'),
    url(r'^account/registration/$',
        views.RegistrationView.as_view(), name='registration'),
    url(r'^(?P<id>\d+)/$', views.SubCategoryView.as_view(), name='subcategory'),

    url(r'^thread/(?P<id>\d+)/reply-to/(?P<reply_to_id>\d+)$', views.ThreadView.as_view(), name='reply_to_post'),
    url(r'^thread/(?P<id>\d+)/check-new-posts/last_loaded=(?P<last_loaded>\d+\.*\d*)/$', views.CheckNewPostsView.as_view(),
        name='check_new_posts'),
    url(r'^thread/(?P<pk>\d+)/update$', views.ThreadUpdateView.as_view(), name='thread_update'),
    url(r'^thread/(?P<pk>\d+)/delete$', views.ThreadDeleteView.as_view(), name='thread_delete'),
    url(r'^thread/(?P<id>\d+)/$', views.ThreadView.as_view(), name='thread'),

    url(r'^post/(?P<pk>\d+)/update$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete$', views.PostDeleteView.as_view(), name='post_delete'),
)