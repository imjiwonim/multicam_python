from django.urls import path
from board import views
from board.views import home, comment_add, comment_delete, post_write, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('comment_add/', views.comment_add, name='comment_add'),
    path('comment_delete/<int:comment_id>/', comment_delete),
    path('post_write/', views.post_write, name='post_write'),
    path("<int:post_id>/", post_detail, name="post_detail"),
]