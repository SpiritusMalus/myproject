from django.shortcuts import render

from .models import *
from .forms import MyUserCreationForm
from django.contrib import auth


def main(request):
    context = {
        "context": Product.objects.all(),
    }
    # if request.method == 'POST':
    #     form = MyUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         form = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password2'])
    #         auth.login(request, form)
    #         context['form'] = form
    #         return render(request, "mainapp/products.html", context)
    # else:
    #     form = MyUserCreationForm()
    #     context['form'] = form
    #     return render(request, "mainapp/products.html", context)

    return render(request, "mainapp/products.html", context)


"""Test func"""
# def register(request):
# if request.method == 'POST':
#     form = MyUserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         form = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password2'])
#         auth.login(request, form)
#         return form
# else:
#     form = MyUserCreationForm()
#     context = {
#         'form': form,
#     }
#     return context
