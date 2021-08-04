from django.db import models

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__(self.email)


class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    message = models.TextField(default="")

    def __str__(self):
        return self.email
