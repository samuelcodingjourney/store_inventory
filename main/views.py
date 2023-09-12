from django.shortcuts import render

def show_main(request):
    context = {
        'application name': 'store_inventory',
        'name': 'Gregorius Samuel Hutahaean',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
