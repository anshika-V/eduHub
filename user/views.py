from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import LoginForm
# Create your views here.


def LoginType(request):
    return render(request, 'user/login_type.html', {'title': 'Login'})


def RegisterType(request):
    return render(request, 'user/register_type.html', {'title': 'Signup'})


class Register(FormView):
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'
    extra_context = {'title': 'Sign Up'}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            logout(request)
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ProfileUpdate(FormView):
    form_class = ProfileForm
    success_url = '/'
    template_name = 'user/new_profile.html'
    instance = None

    def get(self, request, *args, **kwargs):
        self.instance = request.user.profile
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.instance = request.user.profile
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        dic = super().get_form_kwargs()
        dic.update({'instance': self.instance})
        return dic


class CustomLogin(LoginView):
    form_class = LoginForm
    extra_context = {'title': 'Login'}
    template_name = 'user/login.html'
    success_url = '/'
    type = 'S'

    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated):
            if (self.type == request.user.profile.type):
                self.redirect_authenticated_user = True
            else:
                self.redirect_authenticated_user = False
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or self.success_url

    def get(self, request, *args, **kwargs):
        self.extra_context = {'title': 'Login'}
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            if(user.profile.type == self.type):
                return self.form_valid(form)
            else:
                self.extra_context.update(
                    {'error_msg': ' try login with ' + user.profile.get_type_display() + ' login portal', 'type': user.profile.type})
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)
