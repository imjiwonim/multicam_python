from django.urls import path
from board.views import home, comment_add, comment_delete, post_write
# ,post_write

urlpatterns = [
    path('', home, name='home'),
    path('comment_add/', comment_add),
    path('comment_delete/<int:comment_id>/', comment_delete),
    path('post_write/', post_write),
]