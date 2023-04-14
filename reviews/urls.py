from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:review_pk>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:review_pk>/update', views.update, name="update"),
    path('<int:review_pk>/delete', views.delete, name="delete"),
    path('<int:review_pk>/comment', views.create_comment, name="create_comment"),
    path('<int:review_pk>/comment/<int:comment_pk>/delete', views.delete_comment, name="delete_comment"),
    path('<int:review_pk>/prev', views.prev, name="prev"),
    path('<int:review_pk>/next', views.next, name="next"),
    path('<int:review_pk>/review_like', views.review_like, name="review_like"),
    path('<int:review_pk>/comment/<int:comment_pk>/comment_like', views.comment_like, name="comment_like"),
    path('<int:review_pk>/comment/<int:comment_pk>/recomment', views.create_recomment, name="create_recomment")
]
