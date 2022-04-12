from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    template = "palas/me/about.html"
    max_count = 0
    def get_admin_display_title(self):
        return "Blogovi"