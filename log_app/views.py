from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from log_app.models import *


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            Log.objects.create(time=datetime.now(),
                               level=request.POST['level'],
                               message=request.POST['message'],
                               name_logger=request.POST['name_logger'],
                               sender=request.user)
            return render(request, 'index.html')
    else:
        logger = Log.objects.filter(sender_id=request.user.id).all()
        return render(request, 'index.html', {'logger': logger})


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        login(request, user)
        return redirect('/')
    else:
        my_form = AuthenticationForm()
        return render(request, 'login.html', {'form': my_form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


# def register_user(request):
#     if request.method == 'POST':
#         User.objects.create_user(username=request.POST['username'],
#                                  password=request.POST['password2'])
#         return HttpResponseRedirect('/login/')
#     else:
#         my_form = UserCreationForm
#         return render(request, 'register.html', {'form': my_form})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    # form_class = RegistrForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        self.object = form.save()
        return super(RegisterFormView, self).form_valid(form)

# class IndexView(TemplateView):
#     template_name = "index.html"
# #     # logger.error('Something went wrong!')


# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#     template_name = "login.html"
#     success_url = "/"
#
#     def form_valid(self, form):
#         self.user = form.get_user()
#         login(self.request, self.user)
#         return super(LoginFormView, self).form_valid(form)
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect("/")
