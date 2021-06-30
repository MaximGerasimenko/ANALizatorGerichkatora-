import os

from django.shortcuts import render, redirect


def main_redirect_view(request):
    return redirect('home')

def main_view(request):
    return render(request, 'main/index.html')