from django.shortcuts import render

from chat.models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import redirect

@login_required(login_url='/login/')
def index(request):
    if (request.method == 'POST'):
        print('Data received ' + request.POST['themessage'])
        myChat = Chat.objects.get(id=1)
        the_message = Message.objects.create(
            text=request.POST['themessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ the_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)

    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('/chat')
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
    if (request.method == 'POST' and request.POST.get('password') == request.POST.get('password_test')):
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

def logout_view(request):
    logout(request)
    return redirect('/login')