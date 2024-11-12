from django.urls import path
from board.views import home, post_write

urlpatterns = [
    path('', home),
    path('post_write/', post_write),
]