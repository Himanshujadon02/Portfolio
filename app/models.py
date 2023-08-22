from django.db import models

# Create your models here.
class Contactustb(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=90)
    email=models.CharField(max_length=50)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    