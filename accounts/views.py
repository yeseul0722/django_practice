from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# 장고는 기본적으로 회원가입 기능을 이미 만들어서 제공하고 있었다.
# admin 페이지에서 이미 쓰고 있다.
# UserCreationForm은 장고가 이미 가지고 있다.
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm




# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('articles:index')    
    # 회원 가입을 위해 작성해야 하는 form은 ..?
    else:
        form = CustomUserCreationForm()
    context = {
        'from' : form
    }
    return render(request, 'accounts/signup.html')

def login(request):
    # 장고가 이미 가지고 있다.
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            # 있지도 않은 Model 정보로 데이터 저장 불가능
            # form.save()
            # 로그인 -> session 생성행위
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        # GET method로 로그인 페이지 보여달라고 할 때, 그려줄 form
        # 로그인 행위는 분명, 내 DB에 있는 정보를 토대로 만드는 거긴 함.
        # 내 DB에 있는 정보를 토대로 DB에 새로운 유저를 만드는 건 아님
            # User Model과 전혀 관계없는 CREATE 행위 (session)
            # Model 정보가 없는 Form을 사용해서, 인증 절차만 거칠것
            # 인증 시스템
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)