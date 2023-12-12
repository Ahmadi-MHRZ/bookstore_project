from django.urls import path
from .views import BookListview

urlpatterns = [
    path('', BookListview.as_view(), name='book_list'),

]