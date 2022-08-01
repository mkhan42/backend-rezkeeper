from django.db import models
from datetime import date, time
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# DISHES = (
#   ('D', 'Drinks'),
#   ('A', 'Appetizers'),
#   ('M', 'Main Course'),
# )

class Upcoming(models.Model):
    resturant_name = models.CharField('Resturant Name', max_length=100)
    resturant_img = models.CharField('Resturant Image URL', max_length=500)
    address = models.CharField('Resturant Adress', max_length=100)
    cusine_type = models.CharField('Type of Food?', max_length=100)
    date = models.DateField('Date of Visit')
    time = models.TimeField('Time of Visit')
    created_at = models.DateTimeField(auto_now_add=True)
    # myuser = models.CharField(default="", max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.resturant_name

    class Meta:
        ordering = ['date']


class Orders(models.Model):
    name = models.CharField('Menu Item Name', max_length=100)
    price = models.CharField('How Much?', max_length=100)
    # dish = models.CharField(
    #     'Dish Type?',
    #     max_length=1,
    #     choices=DISHES,
    #     default=DISHES[0][0]
    # )

    # myupcoming = models.IntegerField()

    upcoming = models.ForeignKey(Upcoming, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ratings(models.Model):
    rating = models.CharField(
        'Rating out of 5', max_length=1
    )

    upcoming = models.ForeignKey(Upcoming, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating

class Comments(models.Model):
    content = models.CharField(max_length=1000)

    upcoming = models.ForeignKey(Upcoming, on_delete=models.CASCADE)

    def __str__(self):
        return self.content