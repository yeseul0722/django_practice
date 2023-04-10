from django.db import models


# Create your models here.
# 게시글 테이블을 만들기 위한 schema 정의
# 파이선에서 클래스 이름은 파스칼 케이스를 사용한다. 라는 암묵적 약속
# WordAndWord 단어의 첫 글자를 대문자로 작성하는 것.
class Article(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    # -> 게시글이 삭제되면 그 아래의 댓글들도 삭제된다.
    # 1: N 에서 1을 맡고 있으니깐 article은 단수형으로 만들어준다.
    content = models.CharField(max_length=150)

class Comment(models.Model):
    # article 속성에 들어가야하는 값은 내가 참조하고 있는 대상의 pk
    '''
    Comment Table Column
    PK  | content   |  article_id
    1   | 댓글 내용  |   1
    '''
    # class의 속성은 참조 대상 객체의 단수형으로만 작성
    # table 생성시 column명은 알아서 _id가 붙어서 만들어진다.
    # table에는 FK의 값인 정수만 담을 것이니 column이 article_id 형태로
    # id만 입력할 것이라는 것을 명확히 하기 위함이고..

    # Comment Class -> view 함수에서 파이썬 문법에 맞춰 편하게 쓸것이다.
    # ORM -> 내 프로그래밍 언어의 문법상 편의를 위한 방법을 제공해준다.
    # Comment가 참조하고 있는 대상 객체의 id값만 가지고 있을게 아니라,
    # 객체 자체를 가지고 있으면 편하다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)