from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Static_Sitemap


sitemaps = {
    'pages': Static_Sitemap(),
}

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^dap/teams/$', views.teams, name="teams"),
    url(r'^support/faqs/$', views.faqs, name="faqs"),
    url(r'^dap/about-us/$', views.about, name="about"),
    url(r'^dap/contact-us/$', views.contact, name="contact"),
    url(r'^blogs/$', views.blogs, name="blogs"),
    url(r'^privacy-policy/$', views.privacy, name="privacy"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
