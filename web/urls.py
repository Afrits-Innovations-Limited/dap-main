from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Static_Sitemap
from django.views.generic import TemplateView


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
    url(r'^terms-and-conditions/$', views.terms, name="terms"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url(r'^downloads/$', views.downloads, name="download"),
    url(r'^apple-app-site-association$', TemplateView.as_view(template_name="apple-app-site-association", content_type='application/json')),
    url(r'^.well-known/apple-app-site-association$', TemplateView.as_view(template_name="apple-app-site-association", content_type='application/json')),

    
]
