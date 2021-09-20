from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.views.generic import ListView, CreateView

from core.form import LoginForm
from core.models import Timetable


def main_page(request):
    return render(request, 'main_page.html', {

    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponse('account is ok')
                return render(request, 'timetable.html', {
                    'form': form
                })
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'entrance.html', {
        'form': form
    })


class TimetableList(ListView):
    queryset = Timetable.objects.all()
    template_name = "timetable.html"
    context_object_name = "timetable"
