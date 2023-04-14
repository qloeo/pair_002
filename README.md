# TimeLine

## shureeshu
- startproject, startapp

## seho1278
- index 페이지 생성, django_extension 설치
- accounts 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보

## qloeo
- create models : User, Review, Comment
- superuser ( ID: admin , PW: admin1234)

## shureeshu
- 요구사항정리, createform

## seho1278
- accounts 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보
- ipython 설치

## qloeo
- Reviews 전체 글 조회, 글 상세 조회, 글 수정, 글 작성

## shureeshu
- merge conflicts, update readme.md
- 리뷰 삭제, 댓글 생성, 삭제
- 내가 쓴 글 조회

## seho1278
- accounts 회원정보 수정, 비밀번호 변경
- accounts user model 확장

## qloeo
- static BASE 경로 지정
- 이미지 업로드
- install Pillow 

## shureeshu
- base.html
    - body layout 변경 : header/content/footer
    - body.header : navbar 생성, 회원관련 버튼 이동
    
- index.html
    - 회원관련 기능 버튼 삭제

## qloeo
- reviews:index의 html , css 대폭 수정
- 전체 목록 테이블로 변환
- logo 만들어서 삽입
- navbar, footer html, css 수정 

## seho
- detail 페이지 이전글, 다음글 기능 추가
- review, comment 좋아요, 취소 기능 추가
- recomment 기능 추가
- account 프로필 사진 추가

# 요구사항

- [x] 사용자는 회원가입 / 로그인 / 로그아웃을 할 수 있다.
- [x] 회원가입을 할 때 아래 정보를 필수로 입력받는다.
    -  회원이름, 이메일, 비밀번호
- [x] 사용자는 영화에 대한 리뷰를 조회 / 생성 / 수정 / 삭제룰 할 수 있다.
    - 조회, 생성, 수정, 삭제
    - 단, 비로그인 사용자는 조회만 가능하다.
- [x] 리뷰를 작성할 때 아래 정보를 필수로 입력받는다.
    -  리뷰 제목, 리뷰 내용, 영화 이름
- [x] 사용자는 영화 리뷰에 댓글을 조회 / 생성 / 삭제를 할 수 있다.
    - 조회, 생성, 삭제
    - 단, 비로그인 사용자는 조회만 가능하다.
- [x] 로그인한 사용자는 자신의 사용자 프로필 페이지를 조회할 수 있으며 아래 정보를 확인할 수 있다.
    -  회원이름, 이메일, 작성한 리뷰 목록

|   | development requirements | app_name:name | url | view | *** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| o | 회원정보 조회 | accounts:index |        accounts/ | index() | |
| o | 로그인 | accounts:login |        accounts/login/ | login() | |
| o | 로그아웃 | accounts:logout | accounts/logout/ | logout() | |
| o | 회원가입 | accounts:signup | accounts/signup/ | signup() | |
| o | 회원탈퇴 | accounts:delete | accounts/delete/ | delete() | |
| o | 전체 글 조회 | reviews:index | reviews/ | index() | |
| o | 글 상세 조회 | reviews:detail | reviews/<int:review_pk>/ | detail(review_pk) | |
| o | 댓글 조회 | reviews:detail | reviews/<int:review_pk>/ | detail(review_pk) | |
| o | 글 작성 | reviews:create | reviews/create/ | create() | |
| o | 글 수정 | reviews:update | reviews/ <int:review_pk>/update/ | update(review_pk) | |
| o | 글 삭제 | reviews:delete | reviews/ <int:review_pk>/delete/ | delete(review_pk) | |
| o | 댓글 작성 | reviews: comment_create | reviews/ <int:review_pk>/comment/ | create_comment (review_pk) | |
| o | 댓글 삭제 | reviews: comment_delete | reviews/ <int:review_pk>/comment/ <int:comment_pk>/delete/ | delete_comment (review_pk,comment_pk) | |

---
---
---


# 추가구현

Try. 댓글 개수 출력
```
각 리뷰 단일 조회 페이지에서 해당 리뷰에 작성된 댓글 개수 출력
참고 문서
```

Try. 리뷰 영화 이미지 업로드 - 미영
```
사용자가 리뷰 생성시 해당 영화와 관련된 이미지를 업로드할 수 있도록 개선
업로드 한 이미지를 조회 페이지에서 출력
```

Try. 이미지 리사이즈 - 미영
```
django-imagekit 패키지를 활용하여 사용자가 업로드한 이미지 리사이즈

django-imagekit
```

Try. User 모델 확장 - 세호
```
User 모델에 추가 필드 작성하여 User 모델 확장
birthday
```
Try. 회원 정보 수정 - 세호
```
[login_required] POST accounts/update/
CustomUserChangeForm 유효성 검사 후 회원 정보 수정
redirect GET accounts/
[login_required] GET accounts/update/
Django Form을 활용하여 회원 정보 수정 폼 출력
```
Try. 비밀번호 수정 - 세호
```
[login_required] POST accounts/password/
PasswordChangeForm 유효성 검사 후 비밀번호 수정
[login_required] GET accounts/password/
Django Form을 활용하여 비밀번호 수정 폼 출력
```
