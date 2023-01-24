from django.db import models


class Book(models.Model):
    idbook = models.CharField(max_length=30)
    nameofbook = models.CharField(max_length=60)
    authorofbook = models.CharField(max_length=60)
    priceofbook = models.CharField(max_length=20)

    def __str__(self):
        return self.nameofbook
    
