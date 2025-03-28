from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required # decorators >> 함수를 꾸며주는 역할(create 함수)
# -> 로그인 페이지로 redirect 시켜줌

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

@login_required # 로그인이 되어있으면 진행, 아니면 진행 안함뇨
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }

    return render(request, 'create.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'detail.html', context)

@login_required # 로그인이 되어야만 기능 실행 가능
def comment_create(request, article_id):
    form = CommentForm(request.POST) # 사용자가 입력한 데이터 인자로 받음

    if form.is_valid():
        #form.save() # 유저 정보, article 정보 빠져서 에러남
        comment = form.save(commit=False)
        # 객체를 저장하는 경우
        # comment.user = request.user
        # article = Article.odjects.get(id=article_id)
        # comment.article = article
        
        # id 값을 저장하는 경우
        comment.user_id = request.user.id
        comment.article_id = article_id

        comment.save()

        return redirect('articles:detail', id=article_id)

@login_required
def comment_delete(request, article_id, comment_id):# 인자
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user: #로그인한 사람이 comment를 작성한 유저와 같나요?
        comment.delete()

    return redirect('articles:detail', id=article_id)




