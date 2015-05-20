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
    url(r'^thread/(?P<id>\d+)/check-new-posts/last_loaded=(?P<last_loaded>\d+)/$', views.CheckNewPostsView.as_view(),
        name='check_new_posts'),
    url(r'^thread/(?P<pk>\d+)/edit$', views.UpdatePostView.as_view(), name='update_thread'),
    url(r'^thread/(?P<pk>\d+)/delete', views.DeletePostView.as_view(), name='delete_thread'),
    url(r'^thread/(?P<id>\d+)/$', views.ThreadView.as_view(), name='thread'),

    url(r'^posts/(?P<pk>\d+)/edit$', views.UpdatePostView.as_view(), name='update_post'),
    url(r'^posts/(?P<pk>\d+)/delete', views.DeletePostView.as_view(), name='delete_post'),
)