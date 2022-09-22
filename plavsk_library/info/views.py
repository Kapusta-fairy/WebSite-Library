from django.shortcuts import render


def view_info(request):
    return render(request, 'info/info.html')

