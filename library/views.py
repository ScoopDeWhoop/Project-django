from django.http import HttpResponse
from django.shortcuts import render, redirect
from library.models import Book,Customer,Loan
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.timezone import datetime,timedelta

# Create your views here.
def display_all_books(request):
    all_books = Book.objects.all()
    context = {
        'books': all_books}
    return render(request, 'book.html', context)

def single_book(request, book_name):
    book = Book.objects.get(name=book_name) #book_name is a primary key
    context = {
        'book': book
    }
    return render(request, 'single_book.html', context)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #Takes input information
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #Login the user based on the input
        if user is not None:
            login(request, user)
            return redirect('all_books') 
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('all_books')

def registration_view(request):
    if request.method == 'POST': #Takes all the information from inputs
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        city = request.POST.get('city')
        date_of_birth = request.POST.get('date_of_birth')

        if password == confirm_password: #checks if password and confirm password are the same
            if not Customer.objects.filter(username=username).exists() and not Customer.objects.filter(email=email).exists():
                user = Customer.objects.create_user(username=username, email=email, password=password, city=city, date_of_birth=date_of_birth)
                return redirect('login') #After user is created redirect to login page
            else:
                messages.error(request, "Username or email already exists.")
        else:
            messages.error(request, "Passwords dont match.")
    return render(request, 'register.html')
def search_book(request):
    if request.method == 'POST':
        search=request.POST.get('searchBook')
        searched_book=Book.objects.filter(name__contains=search) #Checks if the search input exist at least with one letter in the db
        context = {
        'books_found': searched_book}
    return render(request, 'search.html', context)
def loan_book(request,book_name):
    if request.method == 'POST':
        book = Book.objects.get(name=book_name)
        context = {
        'book': book
    }
        if request.user.is_authenticated:
            customer = Customer.objects.get(username=request.user.username)
            loan_date = datetime.now().date()
            if book.loan_type == 1: #Checks what loan type is the book and calulate the return date based on it
                return_date = loan_date + timedelta(days=10)
            elif book.loan_type == 2:
                return_date = loan_date + timedelta(days=5)
            elif book.loan_type == 3:
                return_date = loan_date + timedelta(days=2)

            loan = Loan.objects.create(book=book, customer=customer, loan_date=loan_date, return_date=return_date)
            loan.save() #Creates the loan

            messages.success(request, "Book successfully loaned")
        else:
            messages.error(request, "Please log in.")
    return render(request, 'single_book.html', context)
def show_loans(request):
    all_loans = Loan.objects.all()
    today = datetime.now().date()
    if request.user.is_superuser: #Checks if the user is admin
        context = {
            'loans': all_loans,
            'today': today
        }
    elif request.user.is_authenticated: #Checks if the user is logged in
        current_customer = Customer.objects.get(username=request.user.username)
        customer_loans = Loan.objects.filter(customer=current_customer)
        context = {
            'loans': customer_loans,
            'today': today
        }
    return render(request, 'loans.html', context)
def return_loan(request,loan_id): #if the return loan button pressed it searching for the id and then delete it from the database
    if request.method == 'POST': 
        loan_return=Loan.objects.get(id=loan_id)
        loan_return.delete()
    messages.success(request, "Book successfully returned")
    return redirect ("all_loans")
def add_book(request): #Creates new book with the inputs its gets from add book page
    if request.method == 'POST':
        book=request.POST.get('name')
        author=request.POST.get('author')
        year=request.POST.get('year_published')
        type=request.POST.get('loan_type')
        image=request.FILES.get('image')
        summary=request.POST.get('summary')
        new_book = Book.objects.create(name=book, author=author ,year_pulished=year ,loan_type=type ,image= image, summary=summary)
        new_book.save()
        messages.success(request, "Book successfully added")
    return render(request, 'add_book.html')
def remove_book(request,book_name): #Add option to delete books
    book = Book.objects.get(name=book_name)
    book.delete()
    return redirect ("all_books")