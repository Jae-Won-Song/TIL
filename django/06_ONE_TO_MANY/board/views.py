# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (require_http_methods, require_POST, require_safe, )

from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@login_required
@require_http_methods(['GET', 'POST'])
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


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'board/index.html', context)


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_detail(request, article_pk):
    # article 상세 페이지
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 입력 창 => _comment_form.html
    form = CommentForm()
    # 좋아요 버튼 UI 결정 Flag
    is_like = article.like_users.filter(pk=request.user.pk).exists()
    
    context = {
        'article': article,
        'form': form,
        'is_like': is_like,
    }
    return render(request, 'board/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 작성자 아니면 돌려보내기
    if request.user != article.user:
        return redirect('board:article_detail', article.pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)        
        if form.is_valid():
            # 기존에 저장된 user_id 갱신할 필요가 없기때문에 commit=False 필요 X
            article = form.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
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
        # 완전 저장하려고 하면 NOT NULL 에러 뜨니까, 직전에 멈춰 주세요.
        comment = form.save(commit=False)
        # 나머지는 직접 할게요
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


@login_required
@require_POST
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    
    # article 에 좋아요 한 사람들 중에, user가 있나요?
    # is_like = user in article.like_users.all() => 효율 안좋음..
    is_like = article.like_users.filter(pk=user.pk).exists()

    # 기존에 좋아요를 했으면
    if is_like:
        # 좋아요 테이블에서 삭제
        user.like_articles.remove(article)
    # 아니라면
    else:
        # 좋아요 테이블에 추가
        user.like_articles.add(article)
    return redirect('board:article_detail', article.pk)