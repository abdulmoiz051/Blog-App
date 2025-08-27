from django.shortcuts import render,redirect,HttpResponse
from django.http import request

def show(request):
    return render(request,'index.html')