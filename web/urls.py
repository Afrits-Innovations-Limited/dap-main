from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^dap/teams/$', views.teams, name="teams"),
    url(r'^support/faqs/$', views.faqs, name="faqs"),
    url(r'^dap/about-us/$', views.about, name="about"),
    url(r'^dap/contact-us/$', views.contact, name="contact"),
    url(r'^blogs/$', views.blogs, name="blogs"),
    url(r'^privacy-policy/$', views.privacy, name="privacy"),
]
