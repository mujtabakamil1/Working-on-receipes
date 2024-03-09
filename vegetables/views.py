from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

@login_required(login_url='/login/')
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
    if request.method == "POST":
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(request ,username = username,password = password)

        if user:
              login(request,user)
              return redirect('/receipes/')
        else:
          messages.error(request,'incorrect password')
          return redirect('/login/')
        
        




    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken")

            return redirect('/register/')
        


        user = User.objects.create(
           first_name = first_name,
           last_name = last_name,
           username = username,
                 )

        user.set_password(password)
        user.save()

        messages.success(request, "Account created succesfully")

        return redirect('/register/')


    return render(request , 'register.html')

