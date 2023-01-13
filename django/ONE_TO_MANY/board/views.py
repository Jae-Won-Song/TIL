from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (require_http_methods, require_POST, require_safe)
from django.contrib.auth.decorators import login_required 
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@login_required
@require_http_methods(['POST', 'GET'])
def create_article(request):    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('board:article_detail', article.pk)

    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'board/form.html', context)

@require_safe
def article_index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'board/index.html', context)
@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        'article':article,
        'form' : form,
    }
    return render(request, 'board/detail.html',context)

@login_required
@require_http_methods(['POST','GET'])
def article_edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 작성자가 아닐때 돌려보냄
    if request.user != article.user:
        return redirect('board:article_detail', article.pk)
    
    if request == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request, 'board/form.html', context)
    



@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()    
        return redirect('board:article_index')
    else:
        return redirect('board:article_detail', article.pk)







@login_required    
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 완전 저장시 NOT NULL 에러가 뜨기 때문에 직전에 멈춰라
        comment = form.save(commit=False)
        # ㄴ나머지는 직접 하겠다.
        comment.user = request.user
        comment.article = article
        comment.save()
    return redirect('board:article_detail', article.pk)

@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == comment.user:
        comment.delete()    
    return redirect('board:article_detail', article.pk)