# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

# Create your views here.

def index(request):  #login/registration page

    return render("awards/index.html")


def profile(request, id):  #individual user profile page

    return render ("awards/profile.html")

def awards(request):   #list of all available awards

    return render("awards/awards.html")


def register(request):  #insert rout for a new user

    return redirect('/profile')

def login(request):  #login route for existing users

    return redirect('/profile')


def requestaward(request):  #route for adding a new phone tool to profile page

    return redirect('/profile')