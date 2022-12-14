
from django.shortcuts import render,redirect
from django import  forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.widgets import NumberInput
# Create your views here.
from fuser.models import  FriendsUser
from home.form import FriendsUserForm

def signup(request):

   if( request.method == 'POST'):
       form = FriendsUserForm(request.POST)
       form.save()
   form = FriendsUserForm()
   context = { 'User_form':form , }

   return render(request,'signup.html',context)
