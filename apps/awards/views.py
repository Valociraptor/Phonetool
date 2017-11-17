# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.

def index(request):  #login/registration page
    if not 'id' in request.session:
        request.session['id'] = 0
    if not 'magic1' in request.session:
        request.session['magic1'] = "default"
    if not 'magic3' in request.session:
        request.session['magic3'] = "default"

    if not 'magic6' in request.session:
        request.session['magic6'] = "default"


    return render(request, "awards/index.html")


def profile(request, id):  #individual user profile page

    if request.session['id'] != 0:
 
        user = User.objects.get(id=id)
        awards = Award.objects.filter(awarded_to = user)
        org = User.objects.all()
        context = {
            'user':user,
            'awards':awards,
            'org': org
        }

        for award in awards:
            if award['id'] == 1:
                request.session['magic1'] = "magic1"
            if award['id'] == 2:
                user.avatar = "troll.jpg"
                user.position = "Senior Vice President of Shennanigans"
                user.bio = "The intent is to provide players with a sense of pride and accomplishment for unlocking different awards.  As for cost, we selected initial values based upon data from the Open Beta and other adjustments made to milestone rewards before launch.  "
                user.save()
            if award['id'] == 3:
                request.session['magic3'] = "magic3"
            if award['id'] == 4:
                user.avatar = "bread.png"
                user.position = "CH2OH FOR LYFE"
                user.bio = "BETTER BREAD THAN DEAD."
                user.save()
            if award['id'] == 5:
                user.avatar = null
                user.position = null
                user.bio = null
                user.save()
            if award['id'] == 6:
                request.session['magic6'] = "magic6"
                user.position = "I was fired because I make terrible decisions and eat awful food"
                user.bio = "I am a generally unlikeable person, and very difficult to work with.  I prounounce Gif with a soft G, and will die alone surrounded by cats that are indifferent to my corpse.  Seriously, they don't even care enough to eat me."
                user.save()
            if award['id'] == 7:
                user.avatar = "noah.png"
                user.name = "Infant"
                user.save()

        return render (request, "awards/profile.html", context)
    return redirect('/')

def awards(request):   #list of all available awards
    awards = Award.objects.all()
    context = {
        'awards': awards
    }

    return render(request, "awards/awards.html", context)


def register(request):  #insert rout for a new user

    result = User.objects.validate(request.POST)
    print result
    if result[0]:
        request.session['id'] =  result[1].id    
        id = str(request.session['id'])    
        return redirect("/profile/"+id)
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)

    return redirect('/registration')


def login(request):  #login route for existing users
    result = User.objects.validatelogin(request.POST)
    if result[0]:
        request.session['id'] =  result[1].id    
        id = str(request.session['id'])
        return redirect("/profile/"+id)
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)

    return redirect('/')


def requestaward(request):  #route for adding a new phone tool to profile page
    id = str(request.session['id'])
    result = Award.objects.addaward(request.POST)

    return redirect('/profile/'+id)

def registration(request):
    return render(request, 'awards/registration.html')