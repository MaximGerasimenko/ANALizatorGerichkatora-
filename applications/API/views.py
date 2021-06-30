from django.http import HttpResponse
from django.shortcuts import render
import logging


def main_view(request):
    return render(request, 'api/index.html')

def test_log_view(request):
    print(request)
    return HttpResponse(request)