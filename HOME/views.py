from itertools import chain

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from USER.forms import ReviewForm, QuestionForm
from USER.models import Review, QuestionAnswers
from .models import CarouselPhotos, Mobile, MobilePictures, LatestNews, UpcomingPhones
from FILTER.models import RAM, PriceRange, Brands
from django.core import exceptions


def home_page(request):
    carouse_images = CarouselPhotos.objects.all()
    mobiles = Mobile.objects.all().order_by('publish_date').reverse()[0:10]
    news = LatestNews.objects.all().order_by('datetime').reverse()[0:4]
    upcoming_phones = UpcomingPhones.objects.all().order_by('datetime').reverse()[0:5]
    args = {
        'upcoming_phones': upcoming_phones,
        'newses': news,
        'carouse_images': carouse_images,
        'mobiles': mobiles,
        'user': request.user,
    }

    return render(request, 'Home/HomePage.html', args)


def post_page(request, pk):
    form = ReviewForm()
    phone = Mobile.objects.get(id=pk)
    images = MobilePictures.objects.filter(phone_id=pk)

    args = {
        'phone': phone,
        'images': images,
        'form': form,
        'reviews': Review.objects.filter(mobile=pk).order_by('publish_date').reverse(),
        'QuestionForm': QuestionForm(),
        'questions': QuestionAnswers.objects.filter(phone_id=pk)
    }

    return render(request, 'Home/Post.html', args)


def news_page(request, pk):
    news = LatestNews.objects.get(datetime=pk)
    args = {'news': news}
    return render(request, 'Home/NewsPage.html', args)


def search(request):
    phone = request.GET.get('phone')
    mobiles = Mobile.objects.filter(phone_name__icontains=phone)

    if mobiles is None:
        mobiles = ''

    return render(request, 'Home/Search.html', context={'phones': mobiles})


def compare(request):
    phone = request.GET.get('phone')
    mobiles = Mobile.objects.filter(phone_name__icontains=phone)

    if mobiles is None:
        mobiles = ''

    return render(request, 'Home/CompareList.html', context={'phones': mobiles})


def comparison(request):
    if request.method == 'GET':
        try:
            p1 = Mobile.objects.get(phone_name__exact=request.GET.get('first'))
            p2 = Mobile.objects.get(phone_name__exact=request.GET.get('second'))

            args = {
                'first_phone': p1,
                'second_phone': p2
            }

            return render(request, 'Home/ComparePage.html', args)

        except exceptions.ObjectDoesNotExist:
            messages.add_message(request, messages.WARNING, message='Select Phone First')
            return redirect('homepage')
    else:
        HttpResponse('Not Found')


def filter_homepage(request):
    brands = Brands.objects.all()
    price = PriceRange.objects.all()
    ram = RAM.objects.all()

    args = {
        'brands': brands,
        'price': price,
        'ram': ram
    }

    return render(request, 'Home/Filter.html', args)


def complete_filter(request):
    brand_phones, price_phones, ram_phones = [[], [], []]

    if request.method == 'GET':
        brands = request.GET.getlist('brand')
        prices = request.GET.getlist('price_range')
        ram = request.GET.getlist('RAM')

        # search by brand
        if brands:
            brand_phones = Mobile.objects.filter(brand__in=brands)

        # search by price
        if prices:
            price_list = []
            new_list = []
            for price in prices:
                item = str(price).split('.')
                price_list.append(item)

            def flat_list(lists):
                for i in lists:
                    if type(i) == list:
                        flat_list(i)
                    else:
                        new_list.append(i)

            flat_list(price_list)
            price_phones = Mobile.objects.filter(starting_price__range=(new_list[0], new_list[len(new_list) - 1]))

        # search by RAM
        if ram:
            if len(ram) > 1:
                ram.sort()
                ram_phones = Mobile.objects.filter(base_model_RAM__in=(ram[0], ram[len(ram) - 1]))
            else:
                ram_phones = Mobile.objects.filter(base_model_RAM__in=ram)

        phones = list(chain(brand_phones, price_phones, ram_phones))
        phones = list(set(phones))

        brands = Brands.objects.all()
        price = PriceRange.objects.all()
        ram = RAM.objects.all()

        args = {
            'brands': brands,
            'price': price,
            'ram': ram,
            'phones': phones
        }

        return render(request, 'Home/Filter.html', context=args)
