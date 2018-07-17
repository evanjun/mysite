from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ArticlePost, ArticleColumn
from django.shortcuts import get_object_or_404

def article_titles(request):
    article_titles = ArticlePost.objects.all()
    paginator = Paginator(article_titles, 3)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list  #当前页的文章所有对象
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)#总页数最后一页
        articles = current_page.object_list

    return render(request, "article/list/article_titles.html", {"articles":articles, "page":page})


def article_details(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "article/list/article_detail.html", {"article": article})