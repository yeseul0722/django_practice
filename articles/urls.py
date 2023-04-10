from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index' ),
    # 게시글 생성 부서에게
    # 게시글 생성을 위해 필요한 정보를 입력할 수 있는 *페이지를 주세요*
    # 페이지 주세요 -> GET method
    path('create/', views.create, name='create'),
    # 특정 게시글의 pk값 하나를 요청 받으면,
    # 그 정수를 'article_pk'라는 변수에 담아서 넘긴다.
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
]
