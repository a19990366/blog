from django.shortcuts import render
import datetime

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    context.update({'now':datetime.datetime.now()})
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')