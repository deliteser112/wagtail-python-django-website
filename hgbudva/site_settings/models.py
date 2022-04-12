from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our website."""
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram profile URL")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("linkedin"),
            ], heading="Social Media Settings")
        ]

class AccomodationPricesSettings(BaseSetting):
    """Hotel Accommodation prices settings for our website."""

    homepage_palas = models.IntegerField(blank=True, null=True, help_text="Homepage Palas Starting Price")
    homepage_castellastva = models.IntegerField(blank=True, null=True, help_text="Homepage Castellastva Starting Price")
    homepage_aleksandar = models.IntegerField(blank=True, null=True, help_text="Homepage Aleksandar Starting Price")
    homepage_slovenska_plaza = models.IntegerField(blank=True, null=True, help_text="Homepage Slovenska Starting Price")
    homepage_mogren = models.IntegerField(blank=True, null=True, help_text="Homepage Mogren Starting Price")
    homepage_palas_lux = models.IntegerField(blank=True, null=True, help_text="Homepage Palas Lux Starting Price")

    slovenska_plaza_3_star_accommodation_comfort_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Comfort Twin Room")
    slovenska_plaza_3_star_accommodation_family_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Family Apartment with Balcony")
    slovenska_plaza_3_star_accommodation_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room")
    slovenska_plaza_3_star_accommodation_double_room_balcony = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room with Balcony")
    slovenska_plaza_3_star_accommodation_studio_apartment  = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Studio Apartment with Kitchen")

    slovenska_plaza_4_star_accommodation_comfort_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Comfort Twin Room")
    slovenska_plaza_4_star_accommodation_studio_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Studio Apartment")
    slovenska_plaza_4_star_accommodation_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room")
    slovenska_plaza_4_star_accommodation_double_room_with_balcony = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room with Balcony")
    slovenska_plaza_4_star_accommodation_family_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Family Apartment with Balcony")

    palas_accommodation_standard_double_room = models.IntegerField(blank=True, null=True, help_text="Palas - Standard Double Room")
    palas_accommodation_comfort_double_room_sea_view = models.IntegerField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Sea View")
    palas_accommodation_comfort_double_room_mountain_view = models.IntegerField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Mountain View")

    palas_lux_accommodation_double_room = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Double Room")
    palas_lux_accommodation_double_room_separate_beds = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Double Room with Separate Beds")
    palas_lux_accommodation_suite_mountain_view = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Suite with Mountain View")
    palas_lux_accommodation_suite_sea_view = models.IntegerField(blank=True, null=True, help_text="Palas - Lux Suite with Sea View")

    aleksandar_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room")
    aleksandar_double_twin_room_with_balcony =models.IntegerField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room with Balcony")
    aleksandar_family_room = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Family room")
    aleksandar_apartment = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Apartment")
    aleksandar_comfort_room_with_balcony = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Comfort Room with Balcony")

    castellastva_family_room = models.IntegerField(blank=True, null=True, help_text="Castellastva - Family Room")
    castellastva_double_room_with_terrace = models.IntegerField(blank=True, null=True, help_text="Castellastva - Double Room with Terrace/Balcony")
    castellastva_deluxe_suite_with_balcony = models.IntegerField(blank=True, null=True, help_text="Castellastva - Deluxe Suite With Balcony")


panels = [
        MultiFieldPanel([
            FieldPanel("palas"),
            FieldPanel("castellastva"),
            FieldPanel("aleksandar"),
            FieldPanel("slovenska_plaza"),
            FieldPanel("mogren"),
            FieldPanel("crystal_palas"),
            ], heading="Homepage minimal prices"),
    MultiFieldPanel([
        FieldPanel("slovenska_plaza_3_star_accommodation_comfort_twin_room"),
        FieldPanel("slovenska_plaza_3_star_accommodation_family_apartment"),
        FieldPanel("slovenska_plaza_3_star_accommodation_double_twin_room"),
        FieldPanel("slovenska_plaza_3_star_accommodation_double_room_balcony"),
        FieldPanel("slovenska_plaza_3_star_accommodation_studio_apartment"),
        ], heading="Slovenska Accommodation 3 Star"),
    MultiFieldPanel([
        FieldPanel("slovenska_plaza_4_star_accommodation_comfort_twin_room"),
        FieldPanel("slovenska_plaza_4_star_accommodation_studio_apartment"),
        FieldPanel("slovenska_plaza_4_star_accommodation_double_twin_room"),
        FieldPanel("slovenska_plaza_4_star_accommodation_double_room_with_balcony"),
        FieldPanel("slovenska_plaza_4_star_accommodation_family_apartment")
        ], heading="Slovenska Accommodation 4 Star"),
    MultiFieldPanel([
        FieldPanel("palas_accommodation_standard_double_room"),
        FieldPanel("palas_accommodation_comfort_double_room_sea_view"),
        FieldPanel("palas_accommodation_comfort_double_room_mountain_view"),
        ], heading="Palas Accommodation"),
    MultiFieldPanel([
        FieldPanel("palas_lux_accommodation_double_room"),
        FieldPanel("palas_lux_accommodation_double_room_separate_beds"),
        FieldPanel("palas_lux_accommodation_suite_mountain_view"),
        FieldPanel("palas_lux_accommodation_suite_sea_view"),
        ], heading="Palas Lux Accommodation"),
    MultiFieldPanel([
        FieldPanel("aleksandar_double_twin_room"),
        FieldPanel("aleksandar_double_twin_room_with_balcony"),
        FieldPanel("aleksandar_family_room"),
        FieldPanel("aleksandar_apartment"),
        FieldPanel("aleksandar_comfort_room_with_balcony"),
        ], heading="Aleksandar Accommodation"),
    MultiFieldPanel([
        FieldPanel("castellastva_family_room"),
        FieldPanel("castellastva_double_room_with_terrace"),
        FieldPanel("castellastva_deluxe_suite_with_balcony"),
        ], heading="Castellastva Accommodation"),
      ]


class AccomodationCtaLinksSettings(BaseSetting):
    """Hotel Accommodation book btn settings for our website."""

    b_slovenska_plaza_3_star_accommodation_comfort_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska *** - Comfort Twin Room")
    b_slovenska_plaza_3_star_accommodation_family_apartment = models.URLField(blank=True, null=True, help_text="Slovenska *** - Family Apartment with Balcony")
    b_slovenska_plaza_3_star_accommodation_double_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room")
    b_slovenska_plaza_3_star_accommodation_double_room_balcony = models.URLField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room with Balcony")
    b_slovenska_plaza_3_star_accommodation_studio_apartment  = models.URLField(blank=True, null=True, help_text="Slovenska *** - Studio Apartment with Kitchen")

    b_slovenska_plaza_4_star_accommodation_comfort_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska **** - Comfort Twin Room")
    b_slovenska_plaza_4_star_accommodation_studio_apartment = models.URLField(blank=True, null=True, help_text="Slovenska **** - Studio Apartment")
    b_slovenska_plaza_4_star_accommodation_double_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room")
    b_slovenska_plaza_4_star_accommodation_double_room_with_balcony = models.URLField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room with Balcony")
    b_slovenska_plaza_4_star_accommodation_family_apartment = models.URLField(blank=True, null=True, help_text="Slovenska **** - Family Apartment with Balcony")

    b_palas_accommodation_standard_double_room = models.URLField(blank=True, null=True, help_text="Palas - Standard Double Room")
    b_palas_accommodation_comfort_double_room_sea_view = models.URLField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Sea View")
    b_palas_accommodation_comfort_double_room_mountain_view = models.URLField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Mountain View")

    b_palas_lux_accommodation_double_room = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Double Room")
    b_palas_lux_accommodation_double_room_separate_beds = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Double Room with Separate Beds")
    b_palas_lux_accommodation_suite_mountain_view = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Suite with Mountain View")
    b_palas_lux_accommodation_suite_sea_view = models.URLField(blank=True, null=True, help_text="Palas - Lux Suite with Sea View")

    b_aleksandar_double_twin_room = models.URLField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room")
    b_aleksandar_double_twin_room_with_balcony =models.URLField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room with Balcony")
    b_aleksandar_family_room = models.URLField(blank=True, null=True, help_text="Aleksandar - Family room")
    b_aleksandar_apartment = models.URLField(blank=True, null=True, help_text="Aleksandar - Apartment")
    b_aleksandar_comfort_room_with_balcony = models.URLField(blank=True, null=True, help_text="Aleksandar - Comfort Room with Balcony")

    b_castellastva_family_room = models.URLField(blank=True, null=True, help_text="Castellastva - Family Room")
    b_castellastva_double_room_with_terrace = models.URLField(blank=True, null=True, help_text="Castellastva - Double Room with Terrace/Balcony")
    b_castellastva_deluxe_suite_with_balcony = models.URLField(blank=True, null=True, help_text="Castellastva - Deluxe Suite With Balcony")

    panels = [
    MultiFieldPanel([
        FieldPanel("b_slovenska_plaza_3_star_accommodation_comfort_twin_room"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_family_apartment"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_double_twin_room"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_double_room_balcony"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_studio_apartment"),
        ], heading="Links Slovenska Accommodation 3 Star"),
    MultiFieldPanel([
        FieldPanel("b_slovenska_plaza_4_star_accommodation_comfort_twin_room"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_studio_apartment"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_double_twin_room"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_double_room_with_balcony"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_family_apartment")
        ], heading="Links Slovenska Accommodation 4 Star"),
    MultiFieldPanel([
        FieldPanel("b_palas_accommodation_standard_double_room"),
        FieldPanel("b_palas_accommodation_comfort_double_room_sea_view"),
        FieldPanel("b_palas_accommodation_comfort_double_room_mountain_view"),
        ], heading="Links Palas Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_palas_lux_accommodation_double_room"),
        FieldPanel("b_palas_lux_accommodation_double_room_separate_beds"),
        FieldPanel("b_palas_lux_accommodation_suite_mountain_view"),
        FieldPanel("b_palas_lux_accommodation_suite_sea_view"),
        ], heading="Links Palas Lux Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_aleksandar_double_twin_room"),
        FieldPanel("b_aleksandar_double_twin_room_with_balcony"),
        FieldPanel("b_aleksandar_family_room"),
        FieldPanel("b_aleksandar_apartment"),
        FieldPanel("b_aleksandar_comfort_room_with_balcony"),
        ], heading="Links Aleksandar Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_castellastva_family_room"),
        FieldPanel("b_castellastva_double_room_with_terrace"),
        FieldPanel("b_castellastva_deluxe_suite_with_balcony"),
        ], heading="Links Castellastva Accommodation"),
    ]

@register_setting
class UpdateAccomodationPricesSettings(BaseSetting):
    """Hotel Accommodation prices settings for our website."""

    homepage_palas = models.IntegerField(blank=True, null=True, help_text="Homepage Palas Starting Price")
    homepage_castellastva = models.IntegerField(blank=True, null=True, help_text="Homepage Castellastva Starting Price")
    homepage_aleksandar = models.IntegerField(blank=True, null=True, help_text="Homepage Aleksandar Starting Price")
    homepage_slovenska_plaza = models.IntegerField(blank=True, null=True, help_text="Homepage Slovenska Starting Price")
    homepage_mogren = models.IntegerField(blank=True, null=True, help_text="Homepage Mogren Starting Price")
    homepage_palas_lux = models.IntegerField(blank=True, null=True, help_text="Homepage Palas Lux Starting Price")

    slovenska_plaza_3_star_accommodation_comfort_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Comfort Twin Room")
    slovenska_plaza_3_star_accommodation_family_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Family Apartment with Balcony")
    slovenska_plaza_3_star_accommodation_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room")
    slovenska_plaza_3_star_accommodation_double_room_balcony = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room with Balcony")
    slovenska_plaza_3_star_accommodation_studio_apartment  = models.IntegerField(blank=True, null=True, help_text="Slovenska *** - Studio Apartment with Kitchen")

    slovenska_plaza_4_star_accommodation_comfort_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Comfort Twin Room")
    slovenska_plaza_4_star_accommodation_studio_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Studio Apartment")
    slovenska_plaza_4_star_accommodation_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room")
    slovenska_plaza_4_star_accommodation_double_room_with_balcony = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room with Balcony")
    slovenska_plaza_4_star_accommodation_family_apartment = models.IntegerField(blank=True, null=True, help_text="Slovenska **** - Family Apartment with Balcony")

    palas_accommodation_standard_double_room = models.IntegerField(blank=True, null=True, help_text="Palas - Standard Double Room")
    palas_accommodation_comfort_double_room_sea_view = models.IntegerField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Sea View")
    palas_accommodation_comfort_double_room_mountain_view = models.IntegerField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Mountain View")

    palas_lux_accommodation_double_room = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Double Room")
    palas_lux_accommodation_double_room_separate_beds = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Double Room with Separate Beds")
    palas_lux_accommodation_suite_mountain_view = models.IntegerField(blank=True, null=True, help_text="Palas Lux - Lux Suite with Mountain View")
    palas_lux_accommodation_suite_sea_view = models.IntegerField(blank=True, null=True, help_text="Palas - Lux Suite with Sea View")

    aleksandar_double_twin_room = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room")
    aleksandar_double_twin_room_with_balcony =models.IntegerField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room with Balcony")
    aleksandar_family_room = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Family room")
    aleksandar_apartment = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Apartment")
    aleksandar_comfort_room_with_balcony = models.IntegerField(blank=True, null=True, help_text="Aleksandar - Comfort Room with Balcony")

    castellastva_family_room = models.IntegerField(blank=True, null=True, help_text="Castellastva - Family Room")
    castellastva_double_room_with_terrace = models.IntegerField(blank=True, null=True, help_text="Castellastva - Double Room with Terrace/Balcony")
    castellastva_deluxe_suite_with_balcony = models.IntegerField(blank=True, null=True, help_text="Castellastva - Deluxe Suite With Balcony")


panels = [
        MultiFieldPanel([
            FieldPanel("palas"),
            FieldPanel("castellastva"),
            FieldPanel("aleksandar"),
            FieldPanel("slovenska_plaza"),
            FieldPanel("mogren"),
            FieldPanel("crystal_palas"),
            ], heading="Homepage minimal prices"),
    MultiFieldPanel([
        FieldPanel("slovenska_plaza_3_star_accommodation_comfort_twin_room"),
        FieldPanel("slovenska_plaza_3_star_accommodation_family_apartment"),
        FieldPanel("slovenska_plaza_3_star_accommodation_double_twin_room"),
        FieldPanel("slovenska_plaza_3_star_accommodation_double_room_balcony"),
        FieldPanel("slovenska_plaza_3_star_accommodation_studio_apartment"),
        ], heading="Slovenska Accommodation 3 Star"),
    MultiFieldPanel([
        FieldPanel("slovenska_plaza_4_star_accommodation_comfort_twin_room"),
        FieldPanel("slovenska_plaza_4_star_accommodation_studio_apartment"),
        FieldPanel("slovenska_plaza_4_star_accommodation_double_twin_room"),
        FieldPanel("slovenska_plaza_4_star_accommodation_double_room_with_balcony"),
        FieldPanel("slovenska_plaza_4_star_accommodation_family_apartment")
        ], heading="Slovenska Accommodation 4 Star"),
    MultiFieldPanel([
        FieldPanel("palas_accommodation_standard_double_room"),
        FieldPanel("palas_accommodation_comfort_double_room_sea_view"),
        FieldPanel("palas_accommodation_comfort_double_room_mountain_view"),
        ], heading="Palas Accommodation"),
    MultiFieldPanel([
        FieldPanel("palas_lux_accommodation_double_room"),
        FieldPanel("palas_lux_accommodation_double_room_separate_beds"),
        FieldPanel("palas_lux_accommodation_suite_mountain_view"),
        FieldPanel("palas_lux_accommodation_suite_sea_view"),
        ], heading="Palas Lux Accommodation"),
    MultiFieldPanel([
        FieldPanel("aleksandar_double_twin_room"),
        FieldPanel("aleksandar_double_twin_room_with_balcony"),
        FieldPanel("aleksandar_family_room"),
        FieldPanel("aleksandar_apartment"),
        FieldPanel("aleksandar_comfort_room_with_balcony"),
        ], heading="Aleksandar Accommodation"),
    MultiFieldPanel([
        FieldPanel("castellastva_family_room"),
        FieldPanel("castellastva_double_room_with_terrace"),
        FieldPanel("castellastva_deluxe_suite_with_balcony"),
        ], heading="Castellastva Accommodation"),
      ]


@register_setting
class UpdateAccomodationCtaLinksSettings(BaseSetting):
    """Hotel Accommodation book btn settings for our website."""

    b_slovenska_plaza_3_star_accommodation_comfort_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska *** - Comfort Twin Room")
    b_slovenska_plaza_3_star_accommodation_family_apartment = models.URLField(blank=True, null=True, help_text="Slovenska *** - Family Apartment with Balcony")
    b_slovenska_plaza_3_star_accommodation_double_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room")
    b_slovenska_plaza_3_star_accommodation_double_room_balcony = models.URLField(blank=True, null=True, help_text="Slovenska *** - Double/Twin Room with Balcony")
    b_slovenska_plaza_3_star_accommodation_studio_apartment  = models.URLField(blank=True, null=True, help_text="Slovenska *** - Studio Apartment with Kitchen")

    b_slovenska_plaza_4_star_accommodation_comfort_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska **** - Comfort Twin Room")
    b_slovenska_plaza_4_star_accommodation_studio_apartment = models.URLField(blank=True, null=True, help_text="Slovenska **** - Studio Apartment")
    b_slovenska_plaza_4_star_accommodation_double_twin_room = models.URLField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room")
    b_slovenska_plaza_4_star_accommodation_double_room_with_balcony = models.URLField(blank=True, null=True, help_text="Slovenska **** - Double/Twin Room with Balcony")
    b_slovenska_plaza_4_star_accommodation_family_apartment = models.URLField(blank=True, null=True, help_text="Slovenska **** - Family Apartment with Balcony")

    b_palas_accommodation_standard_double_room = models.URLField(blank=True, null=True, help_text="Palas - Standard Double Room")
    b_palas_accommodation_comfort_double_room_sea_view = models.URLField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Sea View")
    b_palas_accommodation_comfort_double_room_mountain_view = models.URLField(blank=True, null=True, help_text="Palas - Comfort Double Room with Terrace and Mountain View")

    b_palas_lux_accommodation_double_room = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Double Room")
    b_palas_lux_accommodation_double_room_separate_beds = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Double Room with Separate Beds")
    b_palas_lux_accommodation_suite_mountain_view = models.URLField(blank=True, null=True, help_text="Palas Lux - Lux Suite with Mountain View")
    b_palas_lux_accommodation_suite_sea_view = models.URLField(blank=True, null=True, help_text="Palas - Lux Suite with Sea View")

    b_aleksandar_double_twin_room = models.URLField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room")
    b_aleksandar_double_twin_room_with_balcony =models.URLField(blank=True, null=True, help_text="Aleksandar - Double/Twin Room with Balcony")
    b_aleksandar_family_room = models.URLField(blank=True, null=True, help_text="Aleksandar - Family room")
    b_aleksandar_apartment = models.URLField(blank=True, null=True, help_text="Aleksandar - Apartment")
    b_aleksandar_comfort_room_with_balcony = models.URLField(blank=True, null=True, help_text="Aleksandar - Comfort Room with Balcony")

    b_castellastva_family_room = models.URLField(blank=True, null=True, help_text="Castellastva - Family Room")
    b_castellastva_double_room_with_terrace = models.URLField(blank=True, null=True, help_text="Castellastva - Double Room with Terrace/Balcony")
    b_castellastva_deluxe_suite_with_balcony = models.URLField(blank=True, null=True, help_text="Castellastva - Deluxe Suite With Balcony")

    panels = [
    MultiFieldPanel([
        FieldPanel("b_slovenska_plaza_3_star_accommodation_comfort_twin_room"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_family_apartment"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_double_twin_room"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_double_room_balcony"),
        FieldPanel("b_slovenska_plaza_3_star_accommodation_studio_apartment"),
        ], heading="Links Slovenska Accommodation 3 Star"),
    MultiFieldPanel([
        FieldPanel("b_slovenska_plaza_4_star_accommodation_comfort_twin_room"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_studio_apartment"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_double_twin_room"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_double_room_with_balcony"),
        FieldPanel("b_slovenska_plaza_4_star_accommodation_family_apartment")
        ], heading="Links Slovenska Accommodation 4 Star"),
    MultiFieldPanel([
        FieldPanel("b_palas_accommodation_standard_double_room"),
        FieldPanel("b_palas_accommodation_comfort_double_room_sea_view"),
        FieldPanel("b_palas_accommodation_comfort_double_room_mountain_view"),
        ], heading="Links Palas Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_palas_lux_accommodation_double_room"),
        FieldPanel("b_palas_lux_accommodation_double_room_separate_beds"),
        FieldPanel("b_palas_lux_accommodation_suite_mountain_view"),
        FieldPanel("b_palas_lux_accommodation_suite_sea_view"),
        ], heading="Links Palas Lux Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_aleksandar_double_twin_room"),
        FieldPanel("b_aleksandar_double_twin_room_with_balcony"),
        FieldPanel("b_aleksandar_family_room"),
        FieldPanel("b_aleksandar_apartment"),
        FieldPanel("b_aleksandar_comfort_room_with_balcony"),
        ], heading="Links Aleksandar Accommodation"),
    MultiFieldPanel([
        FieldPanel("b_castellastva_family_room"),
        FieldPanel("b_castellastva_double_room_with_terrace"),
        FieldPanel("b_castellastva_deluxe_suite_with_balcony"),
        ], heading="Links Castellastva Accommodation"),
    ]

@register_setting
class Testimonials(BaseSetting):
    #Palas
    palas_name_one = models.CharField(max_length=50, help_text="Fullname of the guest.", default="0", blank=True)
    palas_review_one= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    palas_name_two = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    palas_review_two= models.CharField(max_length=100, help_text="The review of the guest.",default="0",blank=True)

    palas_name_three = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    palas_review_three= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    #Aleksandar
    aleksandar_name_one = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    aleksandar_review_one= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    aleksandar_name_two = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    aleksandar_review_two= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    aleksandar_name_three = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    aleksandar_review_three= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    #Castellastva
    castellastva_name_one = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    castellastva_review_one= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    castellastva_name_two = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    castellastva_review_two= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    castellastva_name_three = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    castellastva_review_three= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    #Slovenska Plaza
    slovenska_plaza_name_one = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    slovenska_plaza_review_one= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    slovenska_plaza_name_two = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    slovenska_plaza_review_two= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    slovenska_plaza_name_three = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    slovenska_plaza_review_three= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    #Mogren
    mogren_name_one = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    mogren_review_one= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    mogren_name_two = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    mogren_review_two= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    mogren_name_three = models.CharField(max_length=50, help_text="Fullname of the guest.",default="0", blank=True)
    mogren_review_three= models.CharField(max_length=100, help_text="The review of the guest.",default="0", blank=True)

    panels = [
    MultiFieldPanel([
        FieldPanel("palas_name_one"),
        FieldPanel("palas_review_one"),
        FieldPanel("palas_name_two"),
        FieldPanel("palas_review_two"),
        FieldPanel("palas_name_three"),
        FieldPanel("palas_review_three")
        ], heading="Hotel Palas"),
    MultiFieldPanel([
        FieldPanel("aleksandar_name_one"),
        FieldPanel("aleksandar_review_one"),
        FieldPanel("aleksandar_name_two"),
        FieldPanel("aleksandar_review_two"),
        FieldPanel("aleksandar_name_three"),
        FieldPanel("aleksandar_review_three")
        ], heading="Hotel Aleksandar"),
    MultiFieldPanel([
        FieldPanel("castellastva_name_one"),
        FieldPanel("castellastva_review_one"),
        FieldPanel("castellastva_name_two"),
        FieldPanel("castellastva_review_two"),
        FieldPanel("castellastva_name_three"),
        FieldPanel("castellastva_review_three")
        ], heading="Hotel Castellastva"),
    MultiFieldPanel([
        FieldPanel("slovenska_plaza_name_one"),
        FieldPanel("slovenska_plaza_review_one"),
        FieldPanel("slovenska_plaza_name_two"),
        FieldPanel("slovenska_plaza_review_two"),
        FieldPanel("slovenska_plaza_name_three"),
        FieldPanel("slovenska_plaza_review_three")
        ], heading="Hotel Slovenska Plaza"),
    MultiFieldPanel([
        FieldPanel("mogren_name_one"),
        FieldPanel("mogren_review_one"),
        FieldPanel("mogren_name_two"),
        FieldPanel("mogren_review_two"),
        FieldPanel("mogren_name_three"),
        FieldPanel("mogren_review_three")
        ], heading="Hotel Mogren"),
    ]
