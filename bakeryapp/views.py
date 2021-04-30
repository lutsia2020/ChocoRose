from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Bakery, BakeryCategory, BakeryСonsist
from django.views import generic
from django.views.generic import ListView, DetailView
from . forms import BakeryForms, OrderForms
# Create your views here.
def search_view (request):
    if request.method =="POST":
        searched=request.POST['searched']
        bakyries=Bakery.objects.filter(name__iexact=searched)
        return render(request, 'search.html', {'searched':searched, 'bakyries':bakyries })
    else:
        return render(request, 'search.html', {})

class BakeryMainView (generic.ListView):
    model = Bakery
    context_object_name = 'bakery_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = BakeryCategory.objects.all()
        return context

class BakeryView(ListView):
    model = Bakery
    context_object_name = 'bakery_list'
    template_name = 'index.html'

    # Фильтрация списка позиций меню по категории
    def get_queryset(self):
        self.BakeryCategory = get_object_or_404(BakeryCategory, id=self.kwargs['category_id'])
        return Bakery.objects.filter(category=self.BakeryCategory)

    # Добавление дополнительного контента
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = BakeryCategory.objects.all()
        return context


def create (request):
    error=''
    if request.method=="POST":
        form =BakeryForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('http://127.0.0.1:8000/')
        else:
            error='Форма неверно заполнена!'
    form=BakeryForms()
    data = {
        'form':form,
        'error':error
    }
    model = Bakery
    return render(request, 'create.html',data)



class OrderView(ListView):
    model = Bakery
    template_name = 'order_ajax.html'
    context_object_name = 'bakery'
    def get(self, request):
        error = ''
        if request.method == "POST":
            form = OrderForms(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Спасибо за заказ!')
            else:
                error = 'Форма неверно заполнена!'
        form = OrderForms()
        data = {
            'form': form,
            'error': error
        }
        model = BakeryСonsist
        return render(request, 'order_ajax.html', data)


class BakeryDetailView (DetailView):
    model=Bakery
    template_name = 'details_view.html'
    context_object_name = 'bakery'





