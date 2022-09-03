from django.shortcuts import render

def index(request):
    if(request.method == 'POST'):
        print('Data received ' + request.POST['themessage'])
    return render(request, 'chat/index.html', {'name': 'MusG'})
