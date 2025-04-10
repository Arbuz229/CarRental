from django.shortcuts import render


def index(request):
    data = {
        'tittle': 'Магазин аренды',
        'values': ['asd', '123', 'hello']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def contact(request):
    return render(request, 'main/contact.html')


