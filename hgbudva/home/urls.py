from django.conf.urls import include, url

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^search-hgbr/$', views.search_hgbr),

    url(r'^$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^search-results/$', TemplateView.as_view(template_name='home/search-results.html')),
    url(r'^en/$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^me/$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^fr/$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^de/$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^it/$', TemplateView.as_view(template_name='home/index.html')),
    url(r'^ru/$', TemplateView.as_view(template_name='home/index.html')),

    # /me pages
    url(r'me/pocetna/', TemplateView.as_view(template_name='home/index.html')),
    url(r'me/vjencanja/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'me/o-nama/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'me/kontakt/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'me/wellness/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'me/aktivnosti/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'me/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'me/faq/', TemplateView.as_view(template_name='faq/faq.html')),
    url(r'me/nabavke/', TemplateView.as_view(template_name='nabavke/nabavke.html')),
    url(r'me/restorani/', TemplateView.as_view(template_name='restaurants-index/restaurants-index.html')),

    # /en pages
    url(r'en/home/', TemplateView.as_view(template_name='home/index.html')),
    url(r'en/weddings/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'en/hotel-group/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'en/contact/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'en/wellness/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'en/activities/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'en/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'en/faq/', TemplateView.as_view(template_name='faq/faq.html')),
    url(r'en/restaurants/', TemplateView.as_view(template_name='restaurants-index/restaurants-index.html')),

    # /it pages
    url(r'it/pagina-iniziale/', TemplateView.as_view(template_name='home/index.html')),
    url(r'it/matrimoni/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'it/info-sul-gruppo/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'it/contatti/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'it/wellness/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'it/attività/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'it/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'it/faq/', TemplateView.as_view(template_name='faq/faq.html')),

    # /de pages
    url(r'de/startseite/', TemplateView.as_view(template_name='home/index.html')),
    url(r'de/hochzeiten/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'de/ueber-uns/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'de/kontakt/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'de/wellness/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'de/aktivitaeten/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'de/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'de/faq/', TemplateView.as_view(template_name='faq/faq.html')),

    # /fr pages
    url(r'fr/accueil/', TemplateView.as_view(template_name='home/index.html')),
    url(r'fr/mariages/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'fr/nous-connaitre/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'fr/contactez-nous/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'fr/bien-etre/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'fr/activites/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'fr/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'fr/faq/', TemplateView.as_view(template_name='faq/faq.html')),

    # /ru pages
    url(r'ru/doma/', TemplateView.as_view(template_name='home/index.html')),
    url(r'ru/svadby/', TemplateView.as_view(template_name='weddings-index/weddings-index.html')),
    url(r'ru/o-nas/', TemplateView.as_view(template_name='hotel-group/hotel-group.html')),
    url(r'ru/kontakt/', TemplateView.as_view(template_name='contact/contact.html')),
    url(r'ru/khorosheye-zdorovye/', TemplateView.as_view(template_name='wellness-index/wellness-index.html')),
    url(r'ru/deyatelnost/', TemplateView.as_view(template_name='activities/activities.html')),
    url(r'ru/karijera/', TemplateView.as_view(template_name='karijera/karijera.html')),
    url(r'ru/faq/', TemplateView.as_view(template_name='faq/faq.html')),
    ]