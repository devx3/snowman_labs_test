# snowman_labs_test

# CONFIGURE 

## Download the project
Get inside the folder project and exec:

`python manage.py makemigrations`
`python manage.py migrate`

## Create a superuser
`python manage.py createsuperuser`

## Load the Initial Data
`python manage.py loaddata initial_data.json`

## Generate a Token in admin area for your user to start use the API

## Start the server
`python manage.py runserver`


# **Project Requirements**

Your team is developing an application for users to create and explore tourist spots on a map.

Your task is to create a RESTful API for the app to consume and register this information.

# **Chooses**

- Python
- Django Framework
- SQLite
- Unittests
- Docker
- Git

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


