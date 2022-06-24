from email import message
from http import client
from mimetypes import init
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

#new import
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.template import RequestContext

from django.http import HttpResponse

# Create your views here.
from .models import * 
from .forms import *

def email(request):
    form = CreateUserForm()

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                # MAIL SYSTEM ###########################################
                user = form.save()
                user.is_active = False
                user.save()
                
                current_site = get_current_site(request)
                mail_subject = 'Activation link has been sent to your email'
                message = render_to_string('accounts/acc_active_email.html',{
                    'user':user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })

                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()

                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                
                htmly = get_template('accounts/email.html')
                d = {'user':user}
                subject, from_email, to = 'Thank you! Registration Successful', user, email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                ########################################################
                # messages.success(request, 'Please confirm your email address for ' + user + ' to complete the registration')
                return redirect('confirmation')
        else:
            form = CreateUserForm()
    context = {'form':form, 'title':'register here'}
    return render(request, 'accounts/register.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('link_invalid')


def linkValid(request):
    context = {}
    return render(request, 'accounts/link_invalid.html', context)    

def confirmation(request):
    context = {}
    return render(request, 'accounts/confirmation.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    diarys = Diary.objects.all()

    context = {'diarys':diarys}

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def diary(request, pk_test):
    user = User.objects.get(id=pk_test)

    
    diarys = Diary.objects.all()
    diarys = user.diary_set.all()

    context={'diarys':diarys, 'user':user,}
    return render(request, 'accounts/diary.html', context)

@login_required(login_url='login')
def canvas(request, pk_test):
    user = User.objects.get(id=pk_test)

    canvass = Canvas.objects.all()
    canvass = user.canvas_set.all()
    posts=[dict(id=i.id,title=i.canvas_name) for i in Canvas.objects.order_by('id')]

    context = {'canvass':canvass, 'user':user, 'posts':posts}
    return render(request, 'accounts/canvas.html', context)

@login_required(login_url='login')
def collage(request, pk_test):
    user = User.objects.get(id=pk_test)

    collages = Collage.objects.all()
    collages = user.collage_set.all()
    posts=[dict(id=i.id,title=i.collage_name) for i in Collage.objects.order_by('id')]

    context = {'collages':collages, 'user':user, 'posts': posts}
    return render(request, 'accounts/collage.html', context)

@login_required(login_url='login')
def canvasCreator(request, pk_test):
    user = User.objects.get(id=pk_test)

    context={}
    return render(request, 'accounts/canvas_creator.html', context) 

@login_required(login_url='login')
def client(request, pk_test):
    user = User.objects.get(id=pk_test)

    all_users = User.objects.all()

    context = {'user':user, 'all_users':all_users}
    return render(request, 'accounts/users.html/', context)


@login_required(login_url='login')
def createDiary(request, pk):
    user = User.objects.get(id=pk)
    form = DiaryForm(initial={'user':user})
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/diary_form.html', context)

@login_required(login_url='login')
def uploadCanvas(request, pk):
    user = User.objects.get(id=pk)
    form = CanvasForm(initial={'user':user})
    if request.method == 'POST':
        form = CanvasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'accounts/upload_canvas.html', context) 

@login_required(login_url = 'login')
def uploadCollage(request, pk_test):
    user = User.objects.get(id=pk_test)
    form = CollageForm(initial={'user':user})
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'accounts/upload_collage.html', context)

@login_required(login_url='login')
def updateDiary(request, pk_test):

    diary = Diary.objects.get(id=pk_test)
    form = DiaryForm(instance=diary)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/diary_form.html', context)

@login_required(login_url='login')
def deleteDiary(request, pk):
    diary = Diary.objects.get(id=pk)
    if request.method == 'POST':
        diary.delete()
        return redirect('home')


    context = {'name':diary}
    return render(request, 'accounts/delete.html', context)

def landingPage(request):
    context = {}
    return render(request, 'accounts/landing_page.html', context)

@login_required(login_url='login')
def savingCanvas(request):
    user = User.objects.all();
    form = CanvasForm(initial={'user':user})

    context={'form':form, 'user':user}
    return render(request, 'accounts/redirect.html', context) 

@login_required(login_url='login')
def deleteCanvas(request, pk):
    canvas = Canvas.objects.get(id=pk)
    if request.method == 'POST':
        canvas.delete()
        return redirect('home')

    context = {'name':canvas}
    return render(request, 'accounts/delete_canvas.html', context)

@login_required(login_url = 'login')
def deleteCollage(request, pk):
    collage = Collage.objects.get(id=pk)
    if request.method == 'POST':
        collage.delete()
        return redirect('home')

    context = {'name':collage}
    return render(request, 'accounts/delete_collage.html', context)

@login_required(login_url='login')
def editCanvas(request, pk):
    canvas = Canvas.objects.get(id=pk)

    form = CanvasForm(instance=canvas)
    if request.method == 'POST':
        canvas.delete()
        
        return redirect('saving_canvas')
    context = {'name':canvas}

    context = {'form':form, 'name':canvas,}
    return render(request, 'accounts/edit_canvas.html', context)

@login_required(login_url='login')
def createCollage(request, pk_test):
    user = User.objects.get(id=pk_test)
    form = CollageForm(initial={'user':user})
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/collage_creator.html', context)



