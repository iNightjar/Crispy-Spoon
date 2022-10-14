<div align="center">

## Crispy-Spoon
<p><strong>Meals Rater Using Django Restful API</strong></p>
</div>


### Business Requitements As Per The Mockup

- Meals list screen with the following information:
 
```
 Meal Name - Meal Stars Number - Meals Avarage Rate 
 Login - Register - Showing Already loged-In Users.
```

- Popup Error If Users Already Rated The Meals

- Add Rate Screen, Stars {1 to 5} Only

- Save Rates To Database


### Technical requirements

Using Django REST frame work please implement the followings

1- Models - Meal - Stars - User

2- validation if the user already rated the meal

3- validation to rate min 1 and max 5

4- CRUD API for Meals http://127.0.0.1:8000/api/meals it should return the average rating and number of rating a long with the meal name and detail

5- CRUD API for Stars http://127.0.0.1:8000/api/stars no one should be able to use this crud for rating !!

6- Rate API http://127.0.0.1:8000/api/meals/meal_pk/rate_meal create and update API

7- Token authentication

8- Login and register API

9- Token request API

10- Deploy to Heroku