from django.shortcuts import render
from .models import HelloWorld

def hello_world(request):
    if request.method =="POST":

        temp = request.POST.get('hello_world_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'account/helloworld.html', context ={'hello_world_output': new_hello_world})
    else:        
        return render(request, 'account/helloworld.html', context ={'text': 'GET METHOD!!!'})
