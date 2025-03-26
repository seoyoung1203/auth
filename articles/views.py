from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
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
