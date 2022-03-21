from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import MyUserCreationForm


def main(request):
    context = {
        "context": Product.objects.all(),
    }
    return render(request, "mainapp/products.html", context)


class Registration(CreateView):
    form_class = MyUserCreationForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('main')



