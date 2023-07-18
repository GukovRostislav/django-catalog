from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


from .forms import *
from .models import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth2/sign-up.html'


class SignInView(CreateView):
    form_class = UserLoginForm
    success_url = reverse_lazy('home')
    template_name = 'auth2/sign-in.html'


def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    return render(request, "auth2/index.html")


def contacts(request):
    return render(request, 'auth2/contacts.html')


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'auth2/reg.html', {'projects': projects})


def project(request, id):
    project = Projects.objects.get(id=id)
    print(project.preview)
    return render(request, 'auth2/project.html', {'project': project})


def catalog(request):
    catalog = Catalog.objects.all()
    print(catalog)
    return render(request, 'auth2/catalog.html', {'catalog': catalog})


def catalog_product(request, id):
    catalog = Catalog.objects.get(id=id)
    print(catalog.first_preview)
    return render(request, 'auth2/catalog_product.html', {'catalog': catalog})


def consultation(request):
    return render(request, 'auth2/consultation.html')


@login_required
def s(request):
    return render(request, "auth2/index.html")



