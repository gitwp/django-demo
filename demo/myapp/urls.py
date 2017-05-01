from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'submit$', views.submit),
	url(r'logs$', views.logs),
]
