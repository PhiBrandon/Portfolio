from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^portfolio/', views.app_display, name='apps_display'),
	url(r'^about/', views.about, name="about"),
	url(r'^contact_me/', views.contact, name="contact_me"),
	url(r'^article/([0-9]+)/', views.article, name="article")
]