from django.shortcuts import render


def register(request):
    return render(request, 'info/info.html')

