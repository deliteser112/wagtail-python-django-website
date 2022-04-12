from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


class CorporateNewsDetailPage(Page):

    subpage_types = []
    parent_page_types = ['corporate_news.CorporateNewsListingPage']

    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]


class CorporateNewsListingPage(RoutablePageMixin, Page):
    template = "corporate_news/corporate_news_listing_page.html"
    max_count = 50
    subpage_types = ['corporate_news.CorporateNewsBlogPage']

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)

        # Get all children posts
        all_posts = self.get_children().live().public().order_by('-first_published_at')

        # Paginate all posts by 200 per page
        paginator = Paginator(all_posts, 200)
        # Try to get the ?page=x value
        page = request.GET.get("strana")
        try:
            # If the page exists and the ?strana=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?strana=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?strana=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        # context["categories"] = CorporateNewsCategory.objects.all()
        return context


# First subclassed corporate news blog page
class CorporateNewsBlogPage(CorporateNewsDetailPage):
    template = "corporate_news/corporate_news_blog_page.html"

    content_panels = [
        FieldPanel("title_me"),
        FieldPanel("content"),
    ]

    promote_panels = [
        FieldPanel("slug_me"),
    ]
