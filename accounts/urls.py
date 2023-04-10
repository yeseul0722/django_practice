from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    # 게시글 생성과 동일하다.
    # 사용자가 값을 입력할 수 있는 페이지 (회원 가입 페이지) GET method
    # 그 입력한 값으로 실제로 CERATE하는 POST method
    path('signup/', views.signup, name='signup'),
    # 로그인 이라는 것이 어떻게 CREATE 행위란 말인가? -> session이란걸 생성
]
