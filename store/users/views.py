from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from products.models import *

from users.forms import *
from django.contrib import auth
# Create your views here.

class LoginUserView(LoginView, SuccessMessageMixin):
    model = User
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_message = 'Вы успешно зарегистрировались!'

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')

class ProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                print('is passed validation')
                form.save()
                return redirect(request.META['HTTP_REFERER'])
            else:
                print(form.errors)
        form = ProfileForm(instance=request.user)
        return render(request, 'users/profile.html', context={'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context
def logout(request):
    auth.logout(request)
    return redirect('index')

def verify_email(request, email, code):
    message = EmailVerifyMessage.objects.filter(uuid=code)
    if User.objects.filter(email=email) and message:
        user = User.objects.get(email=email)
        user.email_is_verify = True
        user.save()
        message.delete()
        return render(request, 'users/email_verification.html')
    return redirect('index')