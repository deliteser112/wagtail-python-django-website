from blog.models import ArticleBlogPage


def homepage_processor(request):

    #collecting recent blog posts for preview section on homepage
    all_specials = ArticleBlogPage.objects.filter(url_path_en__contains="special-offers").live().public().order_by('-first_published_at')
    if len(all_specials) < 2:
        special_offers = []
    else:
        special_offers = ArticleBlogPage.objects.filter(url_path_en__contains="special-offers").live().public().order_by('-first_published_at')[:5]
    all_news = ArticleBlogPage.objects.filter(url_path_en__contains="news").live().public().order_by('-first_published_at')
    if len(all_news) < 3:
        news = []
    else:
        news = ArticleBlogPage.objects.filter(url_path_en__contains="news").live().public().order_by('-first_published_at')[:5]

    all_events = ArticleBlogPage.objects.filter(url_path_en__contains="events").live().public().order_by('-first_published_at')

    if len(all_events) < 2:
        events = [None,None]
    else:
        events = ArticleBlogPage.objects.filter(url_path_en__contains="events").live().public().order_by('-first_published_at')[0:2]

    return {
        'homepage_special_offers': special_offers,
        'homepage_news': news,
        'homepage_first_event': events[0],
        'homepage_second_event': events[1],
        }
