from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Car

class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'photo', 'is_available', 'phone_number', 'description']
    template_name = 'cars/car_edit.html'

    def get_success_url(self):
        return reverse_lazy('my_cars')

    def get_queryset(self):
        # Ограничиваем редактирование только владельцем
        return Car.objects.filter(owner=self.request.user)




def cars_home(request):
    cars = Car.objects.filter(is_available=True)  # только доступные машины
    return render(request, 'cars/catalog.html', {'cars': cars})






def create(request):
    if not request.user.is_authenticated:
        form = None
        error = None
    else:
        error = ""
        if request.method == 'POST':
            form = CarForm(request.POST, request.FILES)
            if form.is_valid():
                car = form.save(commit=False)
                car.owner = request.user
                car.save()
                return redirect('cars_home')
            else:
                error = "Форма заполнена не верно"
        else:
            form = CarForm()

    return render(request, 'cars/create.html', {
        'form': form,
        'error': error
    })




@login_required
def my_cars(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/my_cars.html', {'cars': cars})



def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})
