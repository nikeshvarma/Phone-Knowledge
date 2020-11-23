from django.shortcuts import render

from .models import Brands


def brand_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        brands = Brands.objects.filter(brands__icontains=query)
        print(brands)
        return render(request, 'Home/BrandSearch.html', {'company': brands})
