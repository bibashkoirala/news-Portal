
from datetime import datetime
import email
from email import message

from django.shortcuts import get_object_or_404, render, HttpResponse

from news.models import Category, News, Subscription, Tag
from django.db.models import Q
from rest_framework import status
from news.utils import TodayBS
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def test(request):
    return render(request, 'home.html')


def home(request):

    npdate = TodayBS()

    items = {}
    recent_update = []
    categoriess = Category.objects.all()
    for category in categoriess:
        items[category.title] = list(
            category.cat.order_by('-published_at').all()[0:6])
        recent_update.append(
            list(category.cat.order_by('-published_at').all()[0:1]))

    news = News.objects.all()[0:4]
    tags = Tag.objects.order_by('-created_at')
    categories = Category.objects.exclude(title='more')
    mainNews = News.objects.filter(is_main=True)[0:3]
    recent_update = News.objects.filter(
        is_main=False, is_highlighted=False).order_by('-published_at')[0:5]

    highlighted = News.objects.filter(
        is_highlighted=True, is_main=False).order_by('-published_at')[0:3]

    page = 'home'
    context = {
        'npdate': npdate,
        'page': page,
        'items': items,
        'tags': tags,
        'news': news,
        'categories': categories,
        'mainNews': mainNews,
        'recent_update': recent_update,


        'highlighted': highlighted,

    }
    return render(request, 'home.html', context)


def news(request, id):
    # news=News.objects.filter(id=id)
    npdate = TodayBS()
    news = get_object_or_404(News, id=id)
    cat_name = news.category.name
    recent_update = News.objects.filter().exclude(
        id=id).order_by('-published_at')[0:6]
    news_id_list = []
    for n in recent_update:
        news_id_list.append(n.id)
    related_news = News.objects.filter(
        category__name=cat_name).order_by('-published_at').exclude(id=id).exclude(id__in=news_id_list)
    tags = Tag.objects.order_by('-created_at')

    categories = Category.objects.exclude(title='more')
    page = "news"
    context = {
        'npdate': npdate,
        'related_news': related_news,
        'news': news,
        'tags': tags,
        'categories': categories,
        'recent_update': recent_update,
        'page': page,



    }
    return render(request, 'news.html', context)


def category(request, title):
    npdate = TodayBS()
    category = get_object_or_404(Category, title=title)
    news = News.objects.filter(category=category).order_by('-published_at')
    tags = Tag.objects.order_by('-created_at')
    categories = Category.objects.exclude(title='more')
    recent_update = News.objects.filter(
        is_main=False, is_highlighted=False).order_by('-published_at')[0:6]
    page = category.title
    context = {
        'npdate': npdate,
        'page': page,
        'category': category,
        'news': news,
        'tags': tags,
        'categories': categories,
        'recent_update': recent_update,

    }
    return render(request, 'category.html', context)


def tag(request, name):
    npdate = TodayBS()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    news = News.objects.filter(tag__name=name).order_by('-published_at')
    page = "tag"
    context = {
        'npdate': npdate,
        'title': name,
        'page': page,
        'news': news,
        'tags': tags,
        'categories': categories,


    }
    return render(request, 'tage.html', context)


def search(request):
    npdate = TodayBS()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    recent_update = News.objects.filter(
        is_main=False, is_highlighted=False).order_by('-published_at')[0:6]
    results = []
    if request.method == "GET":
        query = request.GET.get('q')
        if query == '':
            query == 'None'
        results = News.objects.filter(Q(title__icontains=query) | Q(
            description__icontains=query) | Q(content__icontains=query))
    page = "search"
    context = {
        'npdate': npdate,
        'results': results,
        'tags': tags,
        'categories': categories,
        'recent_update': recent_update,
        'page': page,
    }
    return render(request, 'search.html', context)


@api_view(['GET', 'POST'])
def subscription(request):
    message = ''
    print(request.data['email'])
    if request.method == "POST":
        subscriptionFind = Subscription.objects.filter(
            email=request.data['email'])
        if subscriptionFind:
            message = 'Email already Exist'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            Subscription.objects.create(email=request.data['email'])
            message = 'Successfully created'

            return Response({"message": message}, status=status.HTTP_201_CREATED)
