from django.shortcuts import render

from chat.models import Chat, Message
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login/')
def index(request):
    if (request.method == 'POST'):
        print('Data received ' + request.POST['themessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['themessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)

    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    redirect = request.GET.get('next')
    if (request.method == 'POST'):
        user = authenticate(username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            # return HttpResponseRedirect(request.POST.get('redirect'))
            return HttpResponseRedirect('/chat')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})

    return render(request, 'auth/login.html', {'redirect': redirect})

def register_view(request):
    redirect = request.POST.get('None')
    if(request.method == 'POST' and request.POST.get('password') == request.POST.get('password_test')):
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'), 
            request.POST.get('password'), 
            first_name = request.POST.get('first_name'), 
            last_name = request.POST.get('last_name'),
            is_active = True)
        user.save()
        return HttpResponseRedirect('/login')
        
    
    return render(request, 'register/register.html', {'redirect': redirect})