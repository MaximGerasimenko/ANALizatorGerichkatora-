import os

from flask import Flask, request, abort
from django.shortcuts import render, redirect

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

def main_redirect_view(request):
    print('REDIRECT FROM MAIN TO MAIN')
    return redirect('home')

def main_view(request):
    print('MAIN VISITED')
    return render(request, 'main/index.html')