from django.conf.urls import url

from django.views.generic import TemplateView

urlpatterns = [

    # /me pages
    url(r'me/hotel-mogren-u-budvi/pregled-hotela/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),
    url(r'me/hotel-mogren-u-budvi/smjestaj/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'me/hotel-mogren-u-budvi/konferencije/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'me/hotel-mogren-u-budvi/vjencanja/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'me/hotel-mogren-u-budvi/restorani/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'me/hotel-mogren-u-budvi/lokacija/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'me/hotel-mogren-u-budvi/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),

    # /en pages
    url(r'en/hotel-mogren-in-budva/guest-rooms/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'en/hotel-mogren-in-budva/conference-rooms/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'en/hotel-mogren-in-budva/weddings/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'en/hotel-mogren-in-budva/restaurants-and-bars/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'en/hotel-mogren-in-budva/location/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'en/hotel-mogren-in-budva/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),

    # /it pages
    url(r'it/hotel-mogren-a-budva/informazioni-generali/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),
    url(r'it/hotel-mogren-a-budva/alloggi/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'it/hotel-mogren-a-budva/sala-conferenze/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'it/hotel-mogren-a-budva/matrimoni/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'it/hotel-mogren-a-budva/ristoranti-e-bar/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'it/hotel-mogren-a-budva/posizione/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'it/hotel-mogren-a-budva/',TemplateView.as_view(template_name='mogren/hotel-overview.html')),

    # /de pages
    url(r'de/hotel-mogren-in-budva/hoteluebersicht/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),
    url(r'de/hotel-mogren-in-budva/unterkunft/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'de/hotel-mogren-in-budva/konferenzraeume/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'de/hotel-mogren-in-budva/hochzeiten/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'de/hotel-mogren-in-budva/restaurants-und-bars/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'de/hotel-mogren-in-budva/lage/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'de/hotel-mogren-in-budva/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),

    # /fr pages
    url(r'fr/hotel-mogren-a-budva/apercu/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),
    url(r'fr/hotel-mogren-a-budva/chambre-d-amis/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'fr/hotel-mogren-a-budva/salles-de-conference/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'fr/hotel-mogren-a-budva/mariages/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'fr/hotel-mogren-a-budva/restaurants-et-bars/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'fr/hotel-mogren-a-budva/localisation/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'fr/hotel-mogren-a-budva/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),


    # /ru pages
    url(r'ru/otel-mogren-v-budve/obzor/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),
    url(r'ru/otel-mogren-v-budve/nomera/', TemplateView.as_view(template_name='mogren/accommodation.html')),
    url(r'ru/otel-mogren-v-budve/konferents-zaly/', TemplateView.as_view(template_name='mogren/meetings.html')),
    url(r'ru/otel-mogren-v-budve/svadby/', TemplateView.as_view(template_name='mogren/weddings.html')),
    url(r'ru/otel-mogren-v-budve/restorany-i-bary/', TemplateView.as_view(template_name='mogren/restaurants.html')),
    url(r'ru/otel-mogren-v-budve/lokaciya/', TemplateView.as_view(template_name='mogren/location.html')),
    url(r'ru/otel-mogren-v-budve/', TemplateView.as_view(template_name='mogren/hotel-overview.html')),

    ]
