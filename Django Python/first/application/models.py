from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.CharField(max_length=120)
    Email=models.CharField(max_length=120)
    Feedback=models.TextField()

    def __str__(self):
        return self.Name +" "+self.Email
    

# Creating voice models here.

class Audio(models.Model):
    audio=models.FileField(upload_to="audio")

    def __str__(self):
        return self.audio


# Creating commands models here.

class Additional_information(models.Model):
    Command=models.CharField(max_length=200)

    def __str__(self):
        return self.Command