from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Laptops,Desktops,Mobiles,predict

from .forms import LaptopForm,DesktopForm,MobileForm,Predict
from .ML_Algorithm import prediction
import itertools

def index(request):
    laptops = Laptops.objects.all()
    desktops = Desktops.objects.all()
    mobiles = Mobiles.objects.all()
    items=[]
    # print(laptops)
    # print(desktops)
    # print(mobiles)
    for item in laptops:
        items.append(item)
    for item in desktops:
        items.append(item)
    for item in mobiles:
        items.append(item)
    context = {
        'items': items,
        'header': 'All',
    }
    return render(request, 'inv/index.html', context)

def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'inv/index.html', context)


def display_desktops(request):
    items = Desktops.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'inv/index.html', context)


def display_mobiles(request):
    items = Mobiles.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'inv/index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_laptop(request):
    return add_item(request, LaptopForm)


def add_desktop(request):
    return add_item(request, DesktopForm)


def add_mobile(request):
    return add_item(request, MobileForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops, LaptopForm)


def edit_desktop(request, pk):
    return edit_item(request, pk, Desktops, DesktopForm)


def edit_mobile(request, pk):
    return edit_item(request, pk, Mobiles, MobileForm)


def delete_laptop(request, pk):

    template = 'inv/index.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_desktop(request, pk):

    template = 'inv/index.html'
    Desktops.objects.filter(id=pk).delete()

    items = Desktops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobile(request, pk):

    template = 'inv/index.html'
    Mobiles.objects.filter(id=pk).delete()

    items = Mobiles.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def predict(request):  
    if request.method == "POST":  
        form = Predict(request.POST)  
        type = request.POST['type']
        post_date = request.POST['date']
        splited_date=post_date.split('-')
        list=[]
        date_list=[]
        for x in range(10):
            send_date=''
            date=int(splited_date[2])+x
            send_date+=splited_date[0]
            send_date+='-'
            send_date+=splited_date[1]
            send_date+='-'
            if(date<10):
                send_date+='0'
            send_date+= str(date)
            date_list.append(send_date)
            list.append(prediction.getPrediction(type, send_date))
        zipped_list = zip(list,date_list)
        return render(request, 'inv/predict.html',{"context":zipped_list})
        
        
    else:  
        form = Predict()  
    return render(request,'inv/predict.html',{'form':form})