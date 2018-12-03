from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views import View

from stajedemodanas.forms import RegistrationForm


class BaseView(View, LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.context = dict()

    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)


class HomePageView(BaseView):
    def get(self, request):
        return render(request, 'home.html')


class SignupView(BaseView):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            db_user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name', None)
            last_name = form.cleaned_data.get('last_name', None)
            db_user.email = username
            db_user.refresh_from_db()
            db_user.receiver.email = username
            db_user.receiver.first_name = first_name
            db_user.receiver.last_name = last_name
            db_user.save()
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            self.context['form'] = form
            return redirect('home-page')
        else:
            form = RegistrationForm()
        return render(request, 'registration/signup.html', {'form': form})


def validate_username(request):
    username = request.GET.get('username', None)
    user_model = get_user_model()
    data = dict(is_taken=user_model.objects.filter(username__iexact=username).exists())
    if data['is_taken']:
        data['error_message'] = _('A user with this username already exists.')
    return JsonResponse(data)
