from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'data/index.html')



def hello(request, name):
    context = { 'name' : name}
    return render(request, 'data/hello.html', context)



def user_input(request):
    return render(request, 'data/user_input.html')

def user_output(request):
    c = int(request.POST['cel'])
    f = c * 1.8 + 32

    context = {
        'f' : f,
        'username' : request.POST['username'],
        'password' : request.POST['password'],
    }
    print(request.POST['username'], request.POST['password'])
    return render(request, 'data/user_output.html', context)