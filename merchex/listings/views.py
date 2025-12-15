# from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Band,Listings
from listings.forms import ContactUsForm,BandForm
from django.core.mail import send_mail

from django.shortcuts import render

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands, 'taille': 3})

def band_detail(request, id):
    band = Band.objects.get(id = id)
    return render(request, 'listings/band_detail.html', {'band':band})

def listings_list(request):
    listings = Listings.objects.all()
    return render(request,'listings/listings_list.html', {'listings': listings})

def listings_detail(request, id):
    listing = Listings.objects.get(id= id)
    return render(request, 'listings/listings_detail.html', {'listing' : listing})

def about(request):
    bands = Band.objects.all()
    return render(request, 'listings/about.html')
    
def contact(request):
    if request.method == 'POST' :
        form = ContactUsForm(request.POST)
        if form.is_valid():
          send_mail(subject=f'message from {form.cleaned_data["name"] or "anonyme"} via Merchex Canctact us form',
                    message= form.cleaned_data['message'],
                    from_email= form.cleaned_data['email'],
                    recipient_list= ['admin@merchex.xyz'],
                    )
          return redirect('email-sent')
    else:
        form = ContactUsForm()
    form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def band_create(request):
    if request.method == 'POST' :
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id = id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
        return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id = id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})