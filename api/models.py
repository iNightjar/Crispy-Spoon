from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Models Schema

# Meals Model


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)

# a use of UUID or SLOGs is recommended in production enviroment, it's pad practise to expose the db serial to public

    def __str__(self):
        return self.title


# rating model for each meal, with foriegn key for users and for meals,
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal
    
    
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
