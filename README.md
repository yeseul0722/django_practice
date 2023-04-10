# Django Project 명세서
1. 가상환경 설정
```bash
$ python -m venv venv
```

2. 가상환경에서 django를 설치
```bash
# 가상환경 실행
$ source venv/Scripts/Activate

# django 3.2.18 버전 설치
$ pip install django==3.2.18

# requirements 생성
$ pip freeze > requirements.txt

```
3. django project를 생성
3-1. django app 생성
  - articles(게시글 관련)
3-2. 생성된 app을 project에 등록

4. articles app의 model을 설계
  - Article Class
    -title, content, Comment와 1: N 관계 형성
  - Comment Class
    content, Article과 1: N 관계 형성

5. articles의 각종 기능들을 구현
  - CRUD 작업
  - 전체목록, 상세페이지, 생성, 수정, 삭제
  - 요청 가능 경로 -> 요청 처리 -> 사용자에게 반환할 템플릿

6. 베이스 템플릿

7. form과 관련된 작업
  - django가 제공해주는 ModelForm을 사용

