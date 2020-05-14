from django.shortcuts import render


def index(request):
    return render(request, 'search.html')


def search_results(request):
    return render(request, 'results.html')
