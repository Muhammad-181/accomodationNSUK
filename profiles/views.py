from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Userprofile
from django.utils.text import slugify
from store.forms import  ImageForm, PropertyForm
from store.models import Property, Image
# Create your views here.


def agent_profile(request, pk):
    user = User.objects.get(pk=pk)
    properties = user.properties.exclude(status=Property.DELETED)

    context = {
        'user': user,
        'properties': properties,
    }

    return render(request, 'profiles/agent_profile.html', context)



# def add_property(request):
#     if request.method == 'POST':
#         form = PropertyForm(request.POST, request.FILES)

#         if form.is_valid():
#             title = request.POST.get('title')

#             property = form.save(commit=False)
#             property.user = request.user
#             property.slug = slugify(title)
#             property.save()

#             return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': property.user.pk}))
#     else:
#         form = PropertyForm()
    
#     context = {
#         'title': 'Add product',
#         'form': form
#     }

#     return render(request, 'profiles/property_form.html', context)


def add_property(request):
    propertyform = PropertyForm()
    imageform = ImageForm()

    if request.method =='POST':
        files = request.FILES.getlist('images')

        propertyform = PropertyForm(request.POST, request.FILES)
        if propertyform.is_valid():
            title = request.POST.get('title')
            property = propertyform.save(commit=False)
            property.slug = slugify(title)
            property.user = request.user
            property.save()

            for file in files:
                Image.objects.create(property=property, images=file)
            return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': property.user.pk}))
    context = {
        'p_form': propertyform,
        'i_form': imageform,
    }

    return render(request, 'profiles/property_form.html', context)


def edit_property(request, pk):
    property = Property.objects.filter(user=request.user).get(pk=pk)
    image = Image.objects.filter(property=property)
    

    propertyform = PropertyForm(instance=property)
    imageform = ImageForm()

    if request.method =='POST':
        files = request.FILES.getlist('images')

        propertyform = PropertyForm(request.POST, request.FILES, instance=property)
        if propertyform.is_valid():
            property = propertyform.save(commit=False)
            property.save()

            for file in files:
                image.update_or_create(property=property, images=file)

            return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': property.user.pk}))
    context = {
        'p_form': propertyform,
        'i_form': imageform,
    }
    return render(request, 'profiles/property_form.html', context)



# def edit_property(request, pk):
#     property = Property.objects.filter(user=request.user).get(pk=pk)

#     if request.method == 'POST':
#         form = PropertyForm(request.POST, request.FILES, instance=property)

#         if form.is_valid():
#             form.save()

#             return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': property.user.pk}))
#     else:
#         form = PropertyForm(instance=property)

#     return render(request, 'profiles/property_form.html', {
#         'title': 'Edit product',
#         'property': property,
#         'form': form
#     })


def delete_property(request, pk):
    property = Property.objects.filter(user=request.user).get(pk=pk)
    
   
    property.delete()

   

    return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': request.user.pk}))



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    
    return render(request, 'profiles/signup.html', context)



def login_user(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

    
        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials, try again')
            return render(request, 'profiles/login.html', context, status=401)

        login(request, user)
        

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome {user.username}')

        return HttpResponseRedirect(reverse("agent_profile", kwargs={'pk': request.user.pk}))

    return render(request, 'profiles/login.html')



def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect('frontpage')
