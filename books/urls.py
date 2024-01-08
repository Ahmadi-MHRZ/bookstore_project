from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListview.as_view(), name='book_list'),
    path('<int:pk>/', views.book_detail_view, name='book_detail'),
    path('new/', views.BookCreteView.as_view(), name='book_create'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('translator/<int:pk>/', views.TranslatorDetail.as_view(), name='translator_detail'),



]
