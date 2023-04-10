from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article, CommentForm, article, Comment

# Create your views here.
# index 경로로 요청이 들어왔을 때, 일 처리를 해줄 함수 정의
# 일 처리를 해줄 함수에는 request가 첫번째 필수 인자로 들어온다.
# request에는 사용자의 모든 요청 정보가 들어있다.

def index(request):
    # 메인 템플릿을 사용자에게 보여주는 일을 한다.
    # 그냥 html을 반환하는게 아니라,
    # 그 속에, 사용자가 요청한 정보에 맞는 내용으로 구성해서 반환
    # -> render 함수가 django template을 하나의 html로 구성
    # -> django template을 구성할 때, 필요한 정보들을 render 함수에
    # 인자로 넘겨서 구성할 수 있다.

    # 내가 가진 모든 Article 정보를 가지고 오도록 한다.
    # db.sqlite3 에서 articles_article table에서 모든 정보 요청
    # SQL -> SELECT * FROM articles_article;
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):

    # 게시글을 생성 해달라는 요청이 들어왔을 때,
    if request.method == 'POST':
        # 사용자가 작성한 내용을 토대로 구성
        form = ArticleForm(request.POST)
        # 작성한 내용에 빈칸은 없는지, 잘못된 데이터는 없는지 확인
        if form.is_valid():
            # 문제 없으면 저장
            form.save()
            # 내가 할일 (게시글 작성)이 끝났으니, 결과 확인은 결과 확인 부서로 이관
            return redirect('articles:index')
    else:
        # forms.py에 정의해둔 class를 써서,
        # Article이 필요로하는 컬럼들을 모두 채울 수 있는 input 태그들이 작성된
        # form 정보를 -> create.html에 넘겨줘야 하니까.
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    # 특정 게시글 하나만 조회
    # SQL ->
    # SELECT * FROM articles_article WHERE rowid = article_pk
    article = Article.objects.get(pk=article_pk)
    # forms.py에서 정의한 CommentForm import
    comment_form = CommentForm()
    # ? 모든 댓글 가져오는게 맞나?
    # 특정 게시글을 참조하고 있는 댓글들만 가져와야한다..?
    # comments = Comment.objects.filter(article=article_pk)
    # instance.manager.query_API
    # 나를 참조하고 있는 객체들을 다룰 수 있는 매니저 (역참조 매니저)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def comment_create(request, article_pk):
    # 댓글 생성 == 게시글 생성 | 완전히 동일한 로직
    # 사용자가 입력해서 POST 방식으로 요청 보낸 곳에 정보가 담겨있다.
    # 그 정보를 토대로 댓글을 생성한다.
    comment_form = CommentForm(request.POST)
    # 유효성 검사를 통과 하는지를 확인 (comment_form에는 애초에 content 필드만)
    if comment_form.is_valid():
        # comment가 가지고 있어야할 article (참조 대상) 정보가 누락
        # CommentForm의 fields에 content만 정의해 놨으므로
        # article에 대한 정보는 사용자가 입력하지 않도록 만들었으므로..
        # 하지만, table에 comment를 생성하려면?
        # article FK 필요하다. -> 내가 넣어주면됨.
        comment = comment_form.save(commit=False) # db에 반영하지 말고 저장만
        # comment 객체가 있어야지, 그 객체의 속성 article에 게시글 정보 담을 수 있다
        comment.article =article
        comment.save()
        return redirect('articles:detail', article.pk)