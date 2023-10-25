from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import News, Article, Post


def news_list(request):
    news = Post.objects.order_by('-date_create')
    paginator = Paginator(news, 10)  # Разбиваем на страницы, по 10 новостей на каждой
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news_list.html', {'news': news})


def news_search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) |  # Поиск по названию
        Q(author__icontains=query) |  # Поиск по автору
        Q(date_create__gte=query)  # Поиск по дате
    )
    return render(request, 'news/news_search.html', {'results': results})


def news_detail():
    return None


class NewsForm:
    pass


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')


class ArticleForm:
    pass


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'news/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
