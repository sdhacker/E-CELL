from django.conf.urls import url
from .views import BlogHome, Blogdetails

urlpatterns = [
    url(r'^$', BlogHome.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', Blogdetails.as_view(), name="blog_body"),
]