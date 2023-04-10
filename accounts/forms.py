# 장고는 기본적으로 회원가입 기능을 이미 만들어서 제공하고 있었다.
# admin 페이지에서 이미 쓰고 있다
# UserCreationForm은 장고가 이미 가지고 있다.
from django.contrib.auth.forms import UserCreationForm
# 현재 내 프로젝트에 활성화 되어 있는 메인 User 모델을 찾아서 반환해주는 함수..
from django.contrib.auth import get_user_model


class CustomUserCreationForm():
    pass