## seho1278
- index 페이지 생성, django_extension 설치
- accounts 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보

## qloeo
- create models : User, Review, Comment
- superuser ( ID: admin , PW: admin1234)

## shureeshu - 요구사항정리, createform

# 개발명세
app - reviews, accounts

accounts/urls.py
app_name = 'accounts'

name
- o "index"  회원정보 조회 - account_index
- o "signup" 회원가입 - signup
- o "login" 로그인 - login
- o "logout" 로그아웃 - logout
- o "delete" 회원탈퇴 - delete


reviews/urls.py
app_name = 'reviews'

name
- "index" 전체 글 조회
- "detail" 글 상세 조회 - <int:review_pk>/
- "create" 글 쓰기
- "update" 글 수정 - <int:review_pk>/update
- "delete" 글 삭제 - <int:review_pk>/delete
- "comment_create" 댓글 쓰기 - <int:review_pk>/comment/
- "comment_delete" 댓글 삭제 - <int:review_pk>/comment/<int:comment_pk>/delete/

reviews/views.py
- index
- detail
- create
- update
- delete
- comment_create
- comment_delete

accounts/views.py 
- account_index
- login
- logout
- signup

templates/
- base.html

accounts/templates/accounts
- account_index.html
- signup.html
- login.html

reviews/templates/reviews
- index.html
- detail.html
- update.html
- create.html






사용자는 회원가입 / 로그인 / 로그아웃을 할 수 있다.
회원가입을 할 때 아래 정보를 필수로 입력받는다.
회원이름
이메일
비밀번호
사용자는 영화에 대한 리뷰를 조회 / 생성 / 수정 / 삭제룰 할 수 있다.
단, 비로그인 사용자는 조회만 가능하다.

리뷰를 작성할 때 아래 정보를 필수로 입력받는다.
리뷰 제목
리뷰 내용
영화 이름
사용자는 영화 리뷰에 댓글을 조회 / 생성 / 삭제를 할 수 있다.
단, 비로그인 사용자는 조회만 가능하다.

로그인한 사용자는 자신의 사용자 프로필 페이지를 조회할 수 있으며 아래 정보를 확인할 수 있다.
회원이름
이메일
작성한 리뷰 목록