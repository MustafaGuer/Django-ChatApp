from django.shortcuts import render

from chat.models import Chat, Message


def index(request):
    if (request.method == 'POST'):
        print('Data received ' + request.POST['themessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['themessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
        
    return render(request, 'chat/index.html', {'messages': chatMessages})
