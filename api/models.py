from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Models Schema

# Meals Model


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)

    # a use of UUID or SLOGs is recommended in production enviroment,
    #  it's pad practise to expose the db serial to public


    # no.rating, avg of rating
    def noOfRatings(self):
        ratings = Rating.objects.filter(meal =self)
        return len(ratings)


    def avgRatings(self):
        # sum of ratings stars (total)  / len of ratings(number of ratings)
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        for counter in ratings:
            sum += counter.stars

        if len(ratings) > 0:
            return sum / len(ratings) # logical error handle, if ratings = zero
        else:
            return 0


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
