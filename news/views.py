from django.shortcuts import render, redirect
from news.models import Headline, UserProfile
from datetime import timedelta, timezone, datetime
from .forms import HeadlinesForm
import math
from newsapi import NewsApiClient
import requests
requests.packages.urllib3.disable_warnings()

def news_list(request):
    # user can only scrape once every 24 hours
    user_p = UserProfile.objects.filter(user=request.user).first()
    now = datetime.now(timezone.utc)
    time_difference = now - user_p.last_scrape
    time_difference_in_hours = time_difference / timedelta(minutes=60)
    next_scrape = 24 - time_difference_in_hours
    if (time_difference_in_hours >=0 and time_difference_in_hours <= 24):
        hide_me = True
    else:
        hide_me = False

    headlines = Headline.objects.all()
    context = {
        'object_list': headlines,
        'hide_me': hide_me,
        'next_scrape': math.ceil(next_scrape)
    }
    return render(request,'news/home.html',context)

def news_headlines(request):
    top_headlines = None
    form = HeadlinesForm()
    if request.POST:
        country_code = request.POST['country_field']
        country_text = request.POST
        print(country_text)
        # Init
        newsapi = NewsApiClient(api_key='10fde3f0859148acbd339e6458bbc492')
        # top-headlines
        result = newsapi.get_top_headlines(language='en',
                                            country=country_code)
        top_headlines = result['articles']
        context = {
            'country': country_code,
            'headlines': top_headlines,
            'form': form,
        }
        return render(request, 'news/headlines.html', context)
    else:
        context = {
            'headlines': None,
            'form': form,
        }
        return render(request, 'news/headlines.html', context)

def scrape(request):
    session = requests.Session()
    session.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=10fde3f0859148acbd339e6458bbc492')
    response = requests.get(url).json()

    for i in response['articles']:
        new_headline = Headline()
        new_headline.title = i['title']
        new_headline.author = i['author']
        new_headline.image_url = i['urlToImage']
        new_headline.url = i['url']
        new_headline.description = i['description']
        new_headline.save()
    user_p = UserProfile.objects.filter(user=request.user).first()
    user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()

    return redirect('news:home')
