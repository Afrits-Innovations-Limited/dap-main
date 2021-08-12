from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['home', 'teams', 'faqs', 'about', 'contact', 'privacy']

    def location(self, item):
        return reverse(item)
