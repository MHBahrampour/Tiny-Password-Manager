from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from tiny.models import PasswordInstance
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """View function for home page of site."""
    
    current_user = request.user
    username = current_user.get_username()
    
    context={
        'wellcome': 'Wellcome "{}" .'.format(username),
    }
    return render(request, 'index.html', context=context)

from tiny.forms import PasswordCreateForm
@login_required
def PasswordCreate(request):
    new_password = PasswordInstance()
    form = PasswordCreateForm(request.POST)

    if form.is_valid():
        new_password.title = form.cleaned_data["title"]
        new_password.description = form.cleaned_data["description"]
        new_password.password = form.cleaned_data["password"]

        new_password.user = request.user.get_username()

        new_password.save()
        return HttpResponseRedirect(reverse('index'))

    context = {
        'form': form,
        'new_password': new_password,
    }

    return render(request, 'tiny/pass_create.html', context)

@login_required
def PasswordShow(request):
    username = request.user.get_username()
    user_passwords = PasswordInstance.objects.filter(user__exact=username)

    context={
        'user_passwords' : user_passwords,
    }
    return render(request, 'tiny/pass_show.html', context=context)

@login_required
def PasswordDetail(request, pk):
    the_password = get_object_or_404(PasswordInstance, pk=pk)

    context={
        'the_password' : the_password,
    }
    return render(request, 'tiny/pass_detail.html', context=context)

@login_required
def PasswordDelete(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'tiny/signup.html', {'form': form})