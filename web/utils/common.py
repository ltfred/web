from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from web.settings.dev import HAYSTACK_SEARCH_RESULTS_PER_PAGE


def paginator_func(object_list, page):
    page_size = HAYSTACK_SEARCH_RESULTS_PER_PAGE
    paginator = Paginator(object_list, page_size)
    try:
        page_list = paginator.page(page)
    except EmptyPage:
        raise Http404
    total_page = paginator.num_pages
    return page_list, total_page
