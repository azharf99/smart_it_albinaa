from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver    

# Create your views here.

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.teachers.is_online = True
    user.teachers.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
    user.teachers.is_online = False
    user.teachers.save()