# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages import error
from django.contrib import messages
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def validate(self, POST):
        print "111111111"
        errors = []
        try:
            new_user = User.objects.get(email = POST['email'])
            print "222222222"
        except:
        
            if len(POST['name']) < 2:
                errors.append('Put a name in dude.  You can muster at least 2 characters')
            if len(POST['alias']) < 2:
                errors.append('Bro, your alias has got to be at least 2 characters')
            if not re.match(EMAIL_REGEX, POST['email']):
                errors.append("Don't play coy, you know how emails work")
            if len(POST['password']) < 8:
                errors.append("Password. 8 characters. At least.")
            if POST['password'] != POST['cpassword']:
                errors.append("Passwords need to match bruh")
            if len(errors) > 0:
                return (False, errors)
            else:               
                new_user = User.objects.create(
                    name = POST['name'],
                    alias = POST['alias'],
                    email = POST['email'],
                    bio = POST['bio'],
                    position = POST['position'],
                    avatar = POST['avatar'],
                    password =  bcrypt.hashpw(POST['password'].encode(), bcrypt.gensalt())
                )
                print "33333333333333"
                return (True, new_user)

        errors.append("This user already exists!")
        return (False, errors)
        
    def validatelogin(self, POST):
        errors = []
        try: 
            user = User.objects.get(email = POST['email']) 

            if not bcrypt.checkpw(POST['password'].encode(), user.password.encode()):
                errors.append("The password you have entered is incorrect")
                return (False, errors)
            else:
                return (True, user)
        
        except:
            errors.append("The email you entered doesn't match anything in our database!")
        return (False, errors)


class User(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    

    def __str__(self):
        return self.name

class AwardManager(models.Manager):
    
    def addaward(self, POST):
        this_user = User.objects.get(id=POST['user_id'])
        award = Award.objects.get(id=POST['award_id'])
        this_user.has_award.add(award)


class Award(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    magicability = models.CharField(max_length=255)
    picture_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    awarded_to = models.ManyToManyField(User, related_name="has_award")

    objects = AwardManager()
    
    def __str__(self):
        return self.name

