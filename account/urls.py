from django.conf.urls import url
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url('exit/', authViews.LogoutView.as_view(next_page='login'), name='exit'),
]