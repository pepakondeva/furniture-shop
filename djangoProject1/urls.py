from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from store.sitemaps import (
    ProjectSitemap,
    ProjectItemSitemap,
    CategorySitemap,
    FurnitureSitemap,
    StaticViewSitemap,
)

sitemaps_dict = {
    "projects": ProjectSitemap,
    "project_items": ProjectItemSitemap,
    "categories": CategorySitemap,
    "furnitures": FurnitureSitemap,
    "static": StaticViewSitemap,
}

# robots.txt view
def robots_txt(_request):
    sitemap_url = (
        "http://127.0.0.1:3031/sitemap.xml"
        if settings.DEBUG
        else "https://www.dekat-furniture.org/sitemap.xml"
    )
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

    # sitemap.xml
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),

    # robots.txt
    path("robots.txt", robots_txt, name="robots"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
