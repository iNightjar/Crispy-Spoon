<div align="center">

## Crispy-Spoon
<p><strong>Meals Rater Using Django Rest framework APIs</strong></p>
</div>

<br>

### Business Requitements As Per The Mockup

- Meals List Screen Includes Following Informations:
 
```
 Meal Name - Meal Stars Number - Meals Avarage Rate 
 Login - Register - Showing Already loged-In Users
```

- Popup Error If Users Already Rated The Meals

- Add Rate Screen, Stars From 1 To 5 Only

- Save Rates To Database

<br>

### Technical Implementations

<div align="left>

<p><strong>Following Features</strong></p>

- Models 
- Meal 
- Stars 
- User

</div>



- Validate If Users Already Rated Their Meals

- Validation The Rate Min Is 1 , Max Is 5

- CRUD API For Meals [localhost:8000/api/meals/](http://127.0.0.1:8000/api/meals) 

```
Should Return Avarage Rating And Number Of Rating Along With The Meal Information
```


- CRUD API for Stars [localhost:8000/api/stars/](http://127.0.0.1:8000/api/stars) 

```
No One Should Be Able To Use This Crud For Rating 
```


- Rate API [localhost:8000/api/meals/meal_pk/rate_meal](http://127.0.0.1:8000/api/meals/meal_pk/rate_meal)

```
Create And Update API
```


- Token Authentications

- Login And Register API

- Token Request API

- Deployment To Heroku