import datetime

from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404

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
    return render(request, 'auth2/project.html', {'project': project})


def catalog(request):
    catalog = Catalog.objects.all()
    return render(request, 'auth2/catalog.html', {'catalog': catalog})


def catalog_product(request, id):
    catalog = Catalog.objects.get(id=id)
    return render(request, 'auth2/catalog_product.html', {'catalog': catalog})


def consultation(request):
    return render(request, 'auth2/consultation.html')


@login_required
def request_leave(request):
    return render(request, "auth2/request_leave.html", {'form': RequestLeaveForm()})


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #instance.user = request.user
            return redirect("projects")
        else:
            print(form.errors)
    else:
        form = ProjectCreationForm()

    return render(request, "auth2/create_project.html", {'form': ProjectCreationForm(initial={'author': request.user})})


@login_required
def like(request, id):
    if request.POST.get('action') == 'post':
        result = ''
        project_id = id
        project = get_object_or_404(Projects, id=project_id)
        if project.likes.filter(id=request.user.id).exists():
            project.likes.remove(request.user)
            project.likes_count -= 1
            result = project.likes_count
            project.save()
        else:
            project.likes.add(request.user)
            project.likes_count += 1
            result = project.likes_count
            project.save()

        return JsonResponse({'result': result, })

