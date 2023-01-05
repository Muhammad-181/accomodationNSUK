from django.shortcuts import render
from store.models import Property

# Create your views here.


def frontpage(request):
    properties = Property.objects.exclude(status=Property.DELETED)

    context = {
        'properties': properties
    }

    return render(request, 'core/frontpage.html', context)



def about(request):
    return render(request, 'core/about.html')


def contact_us(request):
    return render(request, 'core/contact_us.html')