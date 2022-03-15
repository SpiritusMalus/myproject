from django.shortcuts import render
from .models import *


def main(request):
    context = {
        "context": Product.objects.all(),
    }
    return render(request, "mainapp/products.html", context)