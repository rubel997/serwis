from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def post_list(request):
    return render(request, 'serwis/index.html', {})

def register_user(request):
    if request.method == 'Zgloszenie':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = UserCreationForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('registration/register.html',args)


def register_success(request):
    return render_to_response('registration/register_success.html')
