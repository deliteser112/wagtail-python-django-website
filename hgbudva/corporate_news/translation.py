from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import CorporateNewsDetailPage, CorporateNewsListingPage, CorporateNewsBlogPage


@register(CorporateNewsDetailPage)
class TranslatorBlogDetailPage(TranslationOptions):
    fields = ()


@register(CorporateNewsBlogPage)
class TranslatorArticleBlogPage(TranslationOptions):
    fields = ()


@register(CorporateNewsListingPage)
class TranslatorBlogListingPage(TranslationOptions):
    fields = ()
