from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.


def receipes(request):
    if request.method == "POST":
        data = request.POST


        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        print(receipe_name)
        print( receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image  =receipe_image        
        )
        
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()

    if request.GET.get('Search'):
       queryset = queryset.filter(receipe_name__icontains = request.GET.get('Search'))



    context = {'receipes' : queryset}

    return render(request , 'receipes.html',context)
    

def delete_receipe(request,id):

    
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')


def update_receipe(request, id):
    queryset=Receipe.objects.get(id=id)

    if request.method == "POST":
       data = request.POST


       receipe_name = data.get('receipe_name')
       receipe_description = data.get('receipe_description')
       receipe_image =request.FILES.get('receipe_image')

       queryset.receipe_name = receipe_name
       queryset.receipe_description=receipe_description
    
       if receipe_image:
            queryset.receipe_image = receipe_image

       queryset.save()
       return redirect('/receipes/')
                   
    context = {'receipe':queryset}
    return render(request , 'update_receipes.html' ,context)


def login_page(request):
    return render(request,'login.html')

def register(request):

    return render(request , 'register.html')

