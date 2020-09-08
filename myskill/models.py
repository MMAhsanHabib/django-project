from django.db import models

class skill(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'picture/')
    desc = models.TextField(max_length = 500)
    datetime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class Contactinfo(models.Model):
    cname = models.CharField(max_length = 50)
    cemail = models.EmailField(max_length = 50)
    cquery = models.TextField(max_length = 50)
    

    

    def __str__(self):
        return self.cname 


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    pdf = models.FileField(upload_to = 'books/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)