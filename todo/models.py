from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self): #overides a default value of original programming, __str__ can be found in the original file
        return self.name