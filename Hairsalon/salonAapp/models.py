from django.db import models


# Create your models here.

class Customer(models.Model):
    c_id = models.BigAutoField(primary_key=True)
    c_name = models.CharField(max_length=256)
    c_surname = models.CharField(max_length=256)
    c_email = models.EmailField(max_length=256)
    c_number = models.CharField(max_length=256)
    c_message = models.TextField(max_length=1000)

    def __str__(self):
        return f'Name : {self.c_name},Surname : {self.c_surname},Email : {self.c_email}, Number : {self.c_number} '

    class Meta:
        db_table = "customer"
