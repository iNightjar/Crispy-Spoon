from .models import Meal, Rating
from rest_framework import viewsets, status, request
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    # meals and rate them inside the meals view
    @action(detail=True, methods=['POST'])
    def rate_meal(self,  request, pk=None):
        if 'stars' in request.data:
            # create or update
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                #update
                rating = Rating.objects.get(user=user.id, meal=meal.id) # specific rate
                rating.stars = stars
                rating.save()
                serialzer = RatingSerializer(rating, many=False)

                json = {
                    'message' : 'Meal Rate Updated',
                    'result' : serialzer.data

                }
                return Response(json, status=status.HTTP_200_OK)


            except:
                #create if the rate not exist
                rating = Rating.objects.create(stars=stars,meal=meal,user=user)
                serialzer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Meal Rate Craeted',
                    'result': serialzer.data

                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'Stars Not Given'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer