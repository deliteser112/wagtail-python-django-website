from django.conf.urls import include, url, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from search import views as search_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls
from django.views.generic import TemplateView
from palas import urls as palas_urls

from aleksandar import urls as aleksandar_urls
from castellastva import urls as castellastva_urls
from mogren import urls as mogren_urls
from slovenska_plaza import urls as slovenska_plaza_urls

from home import urls as home_urls

urlpatterns = [

    url(r'', include(home_urls)),

    url(r'', include(palas_urls)),
    url(r'', include(aleksandar_urls)),
    url(r'', include(castellastva_urls)),
    url(r'', include(mogren_urls)),
    url(r'', include(slovenska_plaza_urls)),

    url(r'^django-admin/', admin.site.urls),
    url(r'^azuriranje/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^sitemap.xml$', sitemap),
    re_path(r'^prevodi/', include('rosetta.urls')),
    ]


urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    url(r'', include(wagtail_urls)),
    )

from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
