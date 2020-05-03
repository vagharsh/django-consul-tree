import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/accounts/login/')
def load_home(request):
    project_root = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(project_root, 'version')) as f:
        app_version = f.read()

    context = {
        'app_version': app_version,
    }

    return render(request, 'home.html', context)
