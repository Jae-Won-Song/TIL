from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.http import (require_http_methods,
                                            require_safe, require_POST)

from django.contrib.auth.decorators import login_required

from .models import Question, Reply
from .forms import QuestionForm, ReplyForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # 이 question 객체의 user 항목은(작성자는) 요청을 보낸 사용자다.
            question.user = request.user
            question.save()
            return redirect('polls:question_detail', question.pk)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'polls/question_form.html', context)


@require_safe
def question_index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/question_index.html', context)


@require_safe
def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = ReplyForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'polls/question_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 요청 보낸 사용자가 질문 작성자가 아니라면,
    if request.user != question.user:
        return HttpResponseForbidden('권한이 없습니다.')

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect('polls:question_detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, }
    return render(request, 'polls/question_form.html', context)


@login_required
@require_POST
def delete_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 요청 보낸 사용자가 질문 작성자가 아니라면,
    if request.user != question.user:
        return HttpResponseForbidden('권한이 없습니다.')
    question.delete()
    return redirect('polls:question_index')


@login_required
@require_POST
def create_reply(request, question_pk):  # 댓글 저장만 담당
    question = get_object_or_404(Question, pk=question_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.question = question
        reply.user = request.user
        reply.save()
    return redirect('polls:question_detail', question.pk)

@login_required
@require_POST
def reply_upvote(request, question_pk, reply_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 1. reply 하나를 잡고
    reply = get_object_or_404(Reply, pk=reply_pk)
    # +1 누른사람(요청보낸사람)이 reply작성자가 아닐때만
    if request.user != reply.user:
    # 2. reply.vote += 1
        reply.vote += 1
    # 3. reply.save()
        reply.save()
    # 4. redirect()
    return redirect('polls:question_detail', question.pk)


@login_required
@require_POST
def delete_reply(request, question_pk, reply_pk):
    # 댓글 작성자와 삭제버튼 누른사람이 같을 때만 삭제
    question = get_object_or_404(Question, pk=question_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    if reply.user == request.user:
        return redirect('polls:question_index')
    else:
        return HttpResponseForbidden('권한이 없습니다!')
    

