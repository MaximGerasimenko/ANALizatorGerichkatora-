import os

from django.shortcuts import render, redirect


def main_redirect_view(request):
    print('REDIRECT FROM MAIN TO MAIN')
    return redirect('home')

def main_view(request):
    print('MAIN VISITED')
    return render(request, 'main/index.html')