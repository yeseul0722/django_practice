from django.db import models
# AbstractBaseUser와 다르다. AbstractBaseUser는 User를 구성하기 위한 가장 기본이 되는 정보
# 유저 네임, 비밀번호를 다루고 있다. -> 비밀번호는 암호화(장고가 제공해줌) 때문에 별도로 관리

# 실제로 슬 User가 가지고 있는 각종 field들이 모두 정의된 class는 AbstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here.
# django가 기본적으로 가지고 있는 auth.User를 대체할 클래스를 만들되,
# User 정보를 다루는 Class는 이미 django가 가지고 있다.
# 추상유저
class User():
    # 특별히 새로운 field가 필요한게 아니라면, 그냥 pass로 넘겨두자.
    pass