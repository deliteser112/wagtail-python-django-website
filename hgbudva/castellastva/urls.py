from django.conf.urls import url

from django.views.generic import TemplateView

urlpatterns = [

    # /me pages
    url(r'me/hotel-castellastva-u-petrovcu/pregled-hotela/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
    url(r'me/hotel-castellastva-u-petrovcu/smjestaj/porodicna-soba/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'me/hotel-castellastva-u-petrovcu/smjestaj/dvokrevetna-soba-sa-terasom/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'me/hotel-castellastva-u-petrovcu/smjestaj/deluxe-apartman-sa-balkonom/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'me/hotel-castellastva-u-petrovcu/smjestaj/',
        TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'me/hotel-castellastva-u-petrovcu/restorani/',
        TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'me/hotel-castellastva-u-petrovcu/plaze-i-bazeni/',
        TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'me/hotel-castellastva-u-petrovcu/wellness-i-spa/',
        TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'me/hotel-castellastva-u-petrovcu/lokacija/',
        TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'me/hotel-castellastva-u-petrovcu/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),

    # /en pages
    url(r'en/hotel-castellastva-in-petrovac/overview/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
    url(r'en/hotel-castellastva-in-petrovac/guest-rooms/family-room/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'en/hotel-castellastva-in-petrovac/guest-rooms/double-room-terrace/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'en/hotel-castellastva-in-petrovac/guest-rooms/deluxe-suite-with-balcony/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'en/hotel-castellastva-in-petrovac/guest-rooms/',
        TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'en/hotel-castellastva-in-petrovac/restaurants-and-bars/',
        TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'en/hotel-castellastva-in-petrovac/beaches-and-pools/',
        TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'en/hotel-castellastva-in-petrovac/wellness-and-spa/',
        TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'en/hotel-castellastva-in-petrovac/location/',
        TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'en/hotel-castellastva-in-petrovac/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),

    # /it pages
    url(r'it/hotel-castellastva-a-petrovac/informazioni-generali/', TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
    url(r'it/hotel-castellastva-a-petrovac/alloggi/camera-familiare/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'it/hotel-castellastva-a-petrovac/alloggi/camera-matrimoniale-doppia-con-balcone/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'it/hotel-castellastva-a-petrovac/alloggi/suite-deluxe-con-balcone/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'it/hotel-castellastva-a-petrovac/alloggi/', TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'it/hotel-castellastva-a-petrovac/ristoranti-e-bar/', TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'it/hotel-castellastva-a-petrovac/spiagge-e-piscine/', TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'it/hotel-castellastva-a-petrovac/wellness-e-spa/', TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'it/hotel-castellastva-a-petrovac/posizione/', TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'it/hotel-castellastva-a-petrovac/', TemplateView.as_view(template_name='castellastva/hotel-overview.html')),

    # /de pages
    url(r'de/hotel-castellastva-in-petrovac/hoteluebersicht/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
    url(r'de/hotel-castellastva-in-petrovac/unterkunft/wohnzimmer/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'de/hotel-castellastva-in-petrovac/unterkunft/doppel-zweibettzimmer-mit-balkon/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'de/hotel-castellastva-in-petrovac/unterkunft/deluxe-suite-mit-balkon/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'de/hotel-castellastva-in-petrovac/unterkunft/',
        TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'de/hotel-castellastva-in-petrovac/restaurants-und-bars/',
        TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'de/hotel-castellastva-in-petrovac/straende-and-pools/',
        TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'de/hotel-castellastva-in-petrovac/wellness-und-spa/',
        TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'de/hotel-castellastva-in-petrovac/lage/',
        TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'de/hotel-castellastva-in-petrovac/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),

    # /fr pages
    url(r'fr/hotel-castellastva-a-petrovac/apercu/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
        url(r'fr/hotel-castellastva-a-petrovac/guest-rooms/chambre-de-famille/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'fr/hotel-castellastva-a-petrovac/guest-rooms/chambre-double-avec-balcon/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'fr/hotel-castellastva-a-petrovac/guest-rooms/suite-de-luxe-avec-balcon/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'fr/hotel-castellastva-a-petrovac/guest-rooms/',
        TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'fr/hotel-castellastva-a-petrovac/restaurants-et-bars/',
        TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'fr/hotel-castellastva-a-petrovac/plages-et-piscines/',
        TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'fr/hotel-castellastva-a-petrovac/bien-etre-et-spa/',
        TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'fr/hotel-castellastva-a-petrovac/localisation/',
        TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'fr/hotel-castellastva-a-petrovac/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),

    # /ru pages

    url(r'ru/otel-castellastva-v-petrovac/obzor/',
        TemplateView.as_view(template_name='castellastva/hotel-overview.html')),
        url(r'ru/otel-castellastva-v-petrovac/nomera/gostinaya/',
        TemplateView.as_view(template_name='castellastva/standard-double-separate-beds.html')),
    url(r'ru/otel-castellastva-v-petrovac/nomera/dvukhmestnyy-nomer-s-balkonom/',
        TemplateView.as_view(template_name='castellastva/comfort-double.html')),
    url(r'ru/otel-castellastva-v-petrovac/nomera/lyuks-s-balkonom/',
        TemplateView.as_view(template_name='castellastva/deluxe-suite.html')),
    url(r'ru/otel-castellastva-v-petrovac/nomera/',
        TemplateView.as_view(template_name='castellastva/accommodation.html')),
    url(r'ru/otel-castellastva-v-petrovac/restorany-i-bary/',
        TemplateView.as_view(template_name='castellastva/restaurants.html')),
    url(r'ru/otel-castellastva-v-petrovac/plyazhi-i-basseyny',
        TemplateView.as_view(template_name='castellastva/beaches.html')),
    url(r'ru/otel-castellastva-v-petrovac/sauna-i-spa/',
        TemplateView.as_view(template_name='castellastva/wellness.html')),
    url(r'ru/otel-castellastva-v-petrovac/lokaciya/',
        TemplateView.as_view(template_name='castellastva/location.html')),
    url(r'ru/otel-castellastva-v-petrovac/', TemplateView.as_view(template_name='castellastva/hotel-overview.html')),


    ]
