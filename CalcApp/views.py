from django.shortcuts import render
from CalcApp import *


def operations(request):
    return render(request,'operations.html')

