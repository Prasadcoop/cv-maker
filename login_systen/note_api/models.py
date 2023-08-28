from django.db import models

# Create your models here.
class Note_api(models.Model):
    title = models.CharField(max_length =100 )
    description = models.TextField()
    amount = models.CharField(max_length =100)
    quantity =models.CharField(max_length=100)
    iscompleted =models.BooleanField(default=False)

   
