from django.shortcuts import render
import random

# Create your views here. (함수)

# user_input 함수 만들기
# input값은 
# 이름 => 문자열
# 나이 => 숫자
# 태어난 달  => 숫자
# user_output 함수 만들기
# out_put값은 운세or anything



def user_input(request):
    return render(request, 'saju/user_input.html', )


def user_output(request):
    horoscopes = [
    "오늘은 자신의 사랑 생활에 있어서 새로운 시작을 준비할 수 있는 기회가 생길 것입니다. 새로운 사람과의 인연이 생길 수 있고, 기존에 있던 사랑관계도 새로운 방향으로 진행될 수 있습니다.",
    "오늘은 자신과 상대방의 소통이 잘 될 것으로 예상됩니다. 상대방의 생각과 의견을 잘 수용하고, 상호 이해가 잘 될 수 있는 기회가 생길 것입니다.",
    "오늘은 자신의 사랑 생활에 있어서 일부 어려움이 있을 수 있습니다. 상대방과의 의견 차이가 생길 수 있고, 조금은 시간이 걸리는 일도 있을 수 있습니다. 그러나 소통과 이해를 통해 극복할 수 있는 하루입니다."
  ]
    #  id = request.POST['name'], id = request.POST['age'], id = request.POST['data']
    print(request.POST['username'], request.POST[''])
    return render(request, 'user_input.html', horoscopes)


# random import 사용
# 받아올 값 id 지정



