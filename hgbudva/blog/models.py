import datetime

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    )
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


class BlogAuthorsOrderable(Orderable):
    """This allows us to select one or more blog authors from Snippets."""

    page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
        )

    panels = [
        SnippetChooserPanel("author"),
        ]

    @property
    def author_name(self):
        return self.author.name

    @property
    def author_website(self):
        return self.author.website

    @property
    def author_image(self):
        return self.author.image


class BlogAuthor(models.Model):
    """Blog author for snippets."""

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
        )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("image"),
                ],
            heading="Name and Image",
            ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
                ],
            heading="Links"
            )
        ]

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"


register_snippet(BlogAuthor)

class BlogListingPage(RoutablePageMixin, Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "blog/blog_listing_page.html"
    max_count = 10
    subpage_types = ['blog.ArticleBlogPage']


    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)

        # Get all children posts
        article_posts = ArticleBlogPage.objects.filter(url_path__contains=self.url_path).live().public().order_by('-first_published_at')
#        Paginate all posts by 4 per page
        paginator = Paginator(article_posts, 10)
        page = request.GET.get("page")

        try:
            #If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            #If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            #If the ?page=x is out of range (too high most likely)
            #Then return the last page
            posts = paginator.page(paginator.num_pages)

        context["paginative_posts"] = posts[1:]
        context["the_most_recent_article"] = posts[0]
        context["latest_1_to_4"] = posts[1:10]
        context["latest_4_to_7"] = posts[11:20]

        return context



class BlogDetailPage(Page):
    """Parental blog detail page."""
    subpage_types = []
    parent_page_types = ['blog.BlogListingPage']
    date = models.DateField("Post date", default=datetime.date.today)

    content = RichTextField()

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
                ],
            heading="Author(s)"
            ),
        FieldPanel('date'),
        FieldPanel("content"),
        ]

    def save(self, *args, **kwargs):
        """Create a template fragment key.
        Then delete the key."""
        key = make_template_fragment_key(
            "blog_post_preview",
            [self.id]
            )
        cache.delete(key)
        return super().save(*args, **kwargs)


# First subclassed blog post page
class ArticleBlogPage(BlogDetailPage):
    """A subclassed blog post page for articles."""
    # max_count = 10000

    template = "blog/article_blog_page.html"

    subtitle = models.CharField(
        max_length=400,
        blank=False,
        null=True,
        help_text='Podnaslov od najvise 400 karaktera - prikazace se u karticama na pocetnoj stranici'
        )

    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Best size for this image will be 1400x400'
        )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("blog_image"),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
                ],
            heading="Author(s)"
            ),
        FieldPanel('date'),
        FieldPanel("content"),
        ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        article_posts = ArticleBlogPage.objects.filter(url_path__contains=self.url_path).live().public().order_by('-first_published_at')

        # Paginate all posts by 3 per page
        paginator = Paginator(article_posts, 3)
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        context["paginative_posts_detail"] = posts[1:]
        return context
