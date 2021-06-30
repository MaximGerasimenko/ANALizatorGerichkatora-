from django.shortcuts import render

import logging

def main_view(request):
    logging.debug(request)
    return render(request, 'api/index.html')