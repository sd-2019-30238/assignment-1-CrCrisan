from django.db import models
from django.contrib.auth.models import User
from Books import models as BookModule
import smtplib, ssl

# Create your models here.

gEmaiFormat = """\
Subject: Update

The book """

class BookLoan(models.Model):
    LOAN_STATUS = (
        ('P', 'Pending Approval'),
        ('A', 'Approved'),
        ('O', 'Open'),
        ('C', 'Closed'),
    )

    person = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    book = models.ForeignKey(BookModule.Book, on_delete = models.CASCADE)
    status = models.CharField(max_length = 1, choices = LOAN_STATUS, default = 'P')

    def __str__(self):
        return str(self.id) + '. User : "' + str(self.person.username) + '" Book : "' + str(self.book) + '"'

    @staticmethod
    def sendEmail(email, name):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "tuturugan@gmail.com"
        receiver_email = email
        password = "TrimiteMaiMulteMailuri!"
        context = ssl.create_default_context()
        message = gEmaiFormat + name + " is available."
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    def Update(self, arg):
        if self.book == arg:
            try:    
                if not self.person.email is None:
                    self.sendEmail(self.person.email, arg.title)
            except:
                pass