from django.shortcuts import render

from chat.models import Chat, Message
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def index(request):
    if (request.method == 'POST'):
        print('Data received ' + request.POST['themessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['themessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)

    return render(request, 'chat/index.html', {'messages': chatMessages})


def login_view(request):
    if (request.method == 'POST'):
        user = authenticate(username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True})

    return render(request, 'auth/login.html')
