from django.db import models

# Create your models here.
class Factory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Drug(models.Model):
    title = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    price = models.IntegerField()
    expirate = models.DateField()
    recipe_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.title