from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthLoginForm, MeasureForm
from .models import Measure


def index(request):
    if request.user.is_authenticated:
        return redirect('/tender/products/')
    else:
        return redirect('/auth')


def workers_list(request):
    return render(request, 'mainapp/index.html')


def auth(request):
    return render(request, 'mainapp/auth.html')


def auth_check(request):
    username = request.POST('username')
    password = request.POST('password')
    print(username)
    print(password)
    return redirect('/')


class AuthLoginView(LoginView):
    template_name = 'mainapp/auth.html'
    form_class = AuthLoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('auth')


def measures_list(request):
    measures = Measure.objects.all().order_by('name')
    context = {
        'measures': measures,
    }
    return render(request, 'mainapp/measures_list.html', context)


def measures_add(request):
    if request.method == 'POST':
        form = MeasureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/measures')
    return render(request, 'mainapp/measures_add.html')


def measures_edit(request, id):
    measure = get_object_or_404(Measure, id=id)

    if request.method == 'POST':
        form = MeasureForm(request.POST, instance=measure)
        if form.is_valid():
            form.save()
            return redirect('/measures')

    context = {
        'measure': measure,
    }
    return render(request, 'mainapp/measures_edit.html', context)


def measures_delete(request, id):
    measure = get_object_or_404(Measure, id=id)
    measure.delete()
    return redirect('/measures')
