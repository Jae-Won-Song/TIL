from django.shortcuts import render

# Create your views here. (함수)

# user_input 함수 만들기
# input값은 
# 이름 => 문자열
# 나이 => 숫자
# 태어난 달  => 숫자
# user_output 함수 만들기
# out_put값은 운세or anything



def user_input(request):
    return render(request, 'saju/user_input.html')


def user_output(request):
    context = {
        'username' : request.POST['username'],
        'age' : request.POST['age'],
        'birth' : request.POST['birth'],
        'gender' : request.POST['gender'],
    }

    return render(request, 'saju/user_output.html', context)





