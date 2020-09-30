# Tourist Spot's API

This is an Test API created for Snowman Lab's Company. 

With this project I achieve a great experience and I had fun a lot! 

So, let's get down to the configuration. 

## Before get start with the configuration... 

Check the [demo here](https://snowmanlabs.herokuapp.com/)

Access the [admin area](https://snowmanlabs.herokuapp.com/)

- **Login:** admin
- **pass:** 123456

And the last is the link to the [API's documentation](https://documenter.getpostman.com/view/7747875/TVRd9r4d)

-----

# So now, let's configure our environment

## Download the project

First, you need to clone this repository: 

- `git clone https://github.com/devx3/snowman_labs_test.git`

As we are using the Django Rest Framework (DRF) we need to install all the dependencies. For that, just execute: 

- `python3 -m pip install -r requirements.txt`

or just: 

- `pip install -r requirements.txt`

Get inside the folder project and execute the following commands:

- `python manage.py makemigrations`
- `python manage.py migrate`

## Load the Initial Data
- `python manage.py loaddata initial_data.json`

## Create a superuser (optional, because the initial data already came with the admin user)
If you want to, create a superuser to access the Admin Area (/admin)
- `python manage.py createsuperuser`

## Start the server
- `python manage.py runserver`

## We're good to go

The next step is access our API documentation through this [documentation](https://documenter.getpostman.com/view/7747875/TVRd9r4d).

You can see a demo here: https://snowmanlabs.herokuapp.com/

**Admin area:** https://snowmanlabs.herokuapp.com/admin
**Login:** admin
**pass:** 123456

# Happy code! 

---------------


# **Project Requirements**

Your team is developing an application for users to create and explore tourist spots on a map.

Your task is to create a RESTful API for the app to consume and register this information.

# **User Stories**

## **As anonymous user I want to:**

- signup / signin with email and password.
- (bonus) signup / signin with Facebook.

## **As a logged in user, I want to:**

- see a list of tourist spots 
- search for tourist spots by name.
- register a tourist spot (picture, name, geographical location and category).
- add pictures to a tourist spot.
- remove pictures I added to a tourist spot.
- favorite a tourist spot.
- see my favorites tourist spots.
- remove a tourist spot from my favorites.
- create new categories.
- (bonus) see a list of tourist spots in a 5 km radius from a given location.

## **Business Rules**

- Anonymous users can only see things.
- Initial Categories are "Park", "Museum", "Theater", "Monument"

# **Deliverables**

- The source code in a public git repository.
- Provide a public working environment (eg. Heroku).
- An Swagger/OpenAPI documentation.
- Collections from Postman
- Instructions how to run the development environment.
- Instructions how to deploy.

# **Evaluation**

## **The evaluation will follow the criteria below.**

- Good practices.
- Code maintainability.
- Performance.
- Privacy.
- Data security.
- Data consistency.
- Full operation.
- Reliability.
- Robustness.
- Scalability.


