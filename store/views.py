from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Property, Instituition, Image
from .forms import PropertyForm

# Create your views here.



def property_detail(request, instituition_slug, slug):
    property = get_object_or_404(Property, slug=slug)
    images = Image.objects.filter(property=property)


    context = {
        'property': property,
        'images': images
    }
    return render(request, 'store/property_detail.html', context)


def instituition_detail(request, slug):
    instituition = get_object_or_404(Instituition, slug=slug)
    properties = instituition.properties.exclude(status=Property.DELETED)


    context =  {
        'instituition': instituition,
        'properties': properties
    }

    return render(request, 'store/instituition_detail.html', context)



def search(request):
    query = request.GET.get('query', '')
    properties = Property.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )

    context = {
        'query': query,
        'properties': properties
    }
    return render(request, 'store/search_results.html', context)

