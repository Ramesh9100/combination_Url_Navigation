from django.shortcuts import render

# Create your views here.

def Ram(request):
    return render(request,'Ram.html')


def chotu(request):
    return render(request,'chotu.html')
