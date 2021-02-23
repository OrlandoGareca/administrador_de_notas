from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
#from django.contrib.auth.forms import UserCreationForm
from admin_notas.bases.forms import RegisterForm
# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password  = form.cleaned_data.get('password1')
            user  = authenticate(username=username,password=raw_password)
            login = (request,user)
            return redirect('bases:login')
    else:
        form = RegisterForm()

    return render(request,'bases/register.html',{'form':form})
#def registeruser(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password  = form.cleaned_data.get('password1')
#            user  = authenticate(username=username,password=raw_password)
#            login = (request,user)
#            return redirect('bases:home')
#        else:
#            form = RegisterForm()
#        return render(request,'register.html',{'form':form})
