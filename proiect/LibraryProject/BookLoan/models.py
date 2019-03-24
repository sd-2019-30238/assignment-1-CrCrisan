from django.db import models
from django.contrib.auth.models import User
from Books import models as BookModule
# Create your models here.

class BookLoan(models.Model):
    LOAN_STATUS = (
        ('P', 'Pending'),
        ('O', 'Open'),
        ('C', 'Closed'),
    )

    person = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    book = models.ForeignKey(BookModule.Book, on_delete = models.CASCADE)
    status = models.CharField(max_length = 1, choices = LOAN_STATUS, default = 'P')

    def __str__(self):
        return str(self.id) + '. User : "' + str(self.person.username) + '" Book : "' + str(self.book) + '"'