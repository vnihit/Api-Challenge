# Api-Challenge
Install mongodb

Migrate the data into respective collections
`mongoimport --host localhost --db paranuara --collection Company --file /paranuara/resources/company.json --jsonArray`

`mongoimport --host localhost --db paranuara --collection People --file /paranuara/resources/people.json --jsonArray`

`mongoimport --host localhost --db paranuara --collection FoodCategory --file /paranuara/resources/food_categories.json --jsonArray`

A third json file `food_categories.json` is created to catogorise diiferent food items as either vegetable or fruit. 

Install the requirements in a virtualenvironment with -
`pip install -r requirements.txt`

Inside the project directory run the server-
`python manage.py runserver`

Navigate to `localhost:8000` to see the list of APIs and play with them
Under the swagger documentation of each api click on execute to enter the required parameter and execute the endpoint. 


The models are defined in `government/models.py` and views logic is defined in the `government/views.py`.