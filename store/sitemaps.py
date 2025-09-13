# store/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

from .models import Project, ProjectItem, Category, Furniture


class BaseSitemap(Sitemap):
    # В dev показвай http, в production – https
    protocol = "http" if getattr(settings, "DEBUG", False) else "https"


# /project/<slug>/<project_id>/
class ProjectSitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.all().order_by('id')

    def location(self, obj):
        return f"/project/{obj.slug}/{obj.id}/"


# /project/item/<slug>/<pk>/
class ProjectItemSitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ProjectItem.objects.all()

    def location(self, obj):
        return f"/project/item/{obj.slug}/{obj.id}/"


# /category/<slug>/<category_id>/
class CategorySitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all().order_by('id')

    def location(self, obj):
        return f"/category/{obj.slug}/{obj.id}/"


# /furniture/details/<slug>/<pk>/
class FurnitureSitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Furniture.objects.all()

    def location(self, obj):
        return f"/furniture/details/{obj.slug}/{obj.id}/"


# Статични страници според реалните url name-ове: store, forus, services, contacts
class StaticViewSitemap(BaseSitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # тези имена съвпадат с твоите:
        # path('', ..., name='store')
        # path('for-us/', ..., name='forus')
        # path('services/', ..., name='services')
        # path('contacts/', ..., name='contacts')
        return ["store", "forus", "services", "contacts"]

    def location(self, name):
        return reverse(name)
