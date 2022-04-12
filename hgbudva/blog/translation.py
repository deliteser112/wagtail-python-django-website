from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import BlogDetailPage, BlogListingPage, ArticleBlogPage


@register(BlogDetailPage)
class TranslatorBlogDetailPage(TranslationOptions):
    fields = (
        'content',
        )


@register(BlogListingPage)
class TranslatorBlogListingPage(TranslationOptions):
    fields = (
        # 'content'
    )


@register(ArticleBlogPage)
class TranslatorArticleBlogPage(TranslationOptions):
    fields = (
        # 'content'
        'subtitle',
        )
