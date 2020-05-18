from django.shortcuts import render
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
    return render(request, 'tinyapp/signup.html', {'form': form})