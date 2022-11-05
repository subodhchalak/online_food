from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register_user(request):
    template_name = 'accounts/register_user.html'
    return render(request, template_name=template_name)