from django.urls import path

from . import views

urlpatterns = [
    path("", views.display_all_books, name="all_books"),
    path('book/<book_name>', views.single_book, name='single_book'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.registration_view, name='register'),
    path('search/', views.search_book, name='search'),
    path('loan/<book_name>', views.loan_book, name='loan_book'),
    path("loanslist/", views.show_loans, name="all_loans"),
    path("return/<int:loan_id>", views.return_loan, name="return_loan"),
]