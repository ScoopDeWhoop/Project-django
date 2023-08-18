from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(default='2000-01-01')
    email=models.EmailField(max_length=100, default="email@email.com")
    def __str__(self):
        return f"{self.username}"
class Book(models.Model):
    CHOICES = (
        (1, 'Loan up to 10 days'),
        (2, 'Loan up to 5 days'),
        (3, 'Loan up to 2 days'),
    )
    name = models.CharField(max_length=100, primary_key=True ,default=True)
    author = models.CharField(max_length=100, null=True)
    year_pulished=models.DateField()
    loan_type = models.IntegerField(choices=CHOICES,default=1)
    image = models.ImageField(upload_to="book_images", default="book_images/book_placeholder.jpg")
    summary = models.TextField(null=True)
    def __str__(self):
        return f"{self.name} - {self.author}"
class Loan(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    loan_date=models.DateField()
    return_date=models.DateField()
    def __str__(self):
        return f"{self.customer} - {self.loan_date} - {self.book} "