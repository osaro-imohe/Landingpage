from django.db import models

class Email(models.Model):
    useremail = models.CharField(max_length = 100, blank = True,)
