from django.shortcuts import render
import json
from django.http import JsonResponse
from django.conf import settings
import os

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


def partner_offers_api(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'main', 'data', 'partners_offers.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        return JsonResponse({'error': 'Файл не найден'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Ошибка чтения JSON'}, status=500)

