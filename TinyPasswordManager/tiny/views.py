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