from django.shortcuts import render
from django.views.decorators.http import require_POST


@require_POST
def login(request):
    if request.method == 'POST':
        pass
