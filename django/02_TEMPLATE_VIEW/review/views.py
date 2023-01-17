from django.shortcuts import render

# Create your views here.

def index(request):
    




    # Res(응답) => HTML render
    # render (1. requese | 2. HTML 이름 | 3. 넘길 데이터)
    return render(request, 'review/index.html')


def hello(request):
    return render(request, 'review/hello.html')

