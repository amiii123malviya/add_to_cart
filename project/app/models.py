from django.db import models

# Create your models here.
class Form(models.Model):
    Name=models.CharField(max_length=250)
    Desc=models.CharField(max_length=250)
    Img=models.ImageField(upload_to='images/')
    Ammt=models.IntegerField()
    

    class Meta():
        db_table='Form'
