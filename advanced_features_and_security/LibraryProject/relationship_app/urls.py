from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

# urls.py
from . import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view.admin_view, name='admin_view'),
    path('librarian-view/', librarian_view.librarian_view, name='librarian_view'),
    path('member-view/', member_view.member_view, name='member_view'),
]

from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('book/add/', add_book, name='add_book/'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book/'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]

