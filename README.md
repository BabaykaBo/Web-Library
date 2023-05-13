# Web Library
This is my Django-based student project from the course. It is the web library application with the base functions like registration, login and loguot, watching books and creating orders, different possibilities for user and admin etc.

### Dependencies:

* Python
* Django
* DRF
* Bootstrap4
* Selenium
* Psycopg2

For my project I used `PostgreSQL` 15.2 version. If you use another database system, some dependencies wiil be not actual.

### Installation:

1. Clone the project.
2. Create the virtual environment

Watch actual version: `https://docs.python.org/3.11/library/venv.html`.
3. Install requirements:
```commandline
pip install -r requirements.txt
```
4. Сonfigure the connection with database. I used `local_settings.py`, but you can use another methods.
5. Use command for making migrations:
```commandline
python manage.py migrate 
```
6.Create superuser:
```commandline
python manage.py createsuperuser
```
7. Use command for run server:
```commandline
python manage.py runserver   
```
Notes: I used PyCharm and for the project I have to configure my project structure. Use `Ctrl+Alt+P`, then choose `Project Structure` in the menu, click on `library` package and choose `Sources`. The package become blue and then apply.
## Features:

### User authentication system
* register new user.
* login and logout existing user.
* unauthorized users can only register or login, another  functionality will be unavailable.

### Usual user
* view a list of books.
* view an information about the specific book.
* view list of current user's orders with their information.
* create orders.
* view a list of users.
* view an information about the specific user.

### Admin
* All features accessible for usual user.
* Django admin page (`http://127.0.0.1:8000/admin/`).
* view a list of all orders with their information.
* close orders.
* view additional information about the specific user: user's ordered books.
* view a list of authors with their information.
* create a new author.
* delete the author if the author has no books.

### API
Use this url for accessing the DRF home page (`http://127.0.0.1:8000/api/v1/`).

You have all main CRUD methods for all models.
* for list of objects you are allowed to: GET, POST, HEAD, OPTIONS.

Example:
`http://127.0.0.1:8000/api/v1/user/`
* for the specific object you are allowed to: GET, PUT, PATCH, DELETE, HEAD, OPTIONS.

Example: `http://127.0.0.1:8000/api/v1/order/{id}?/`
* access to the list of the specific user's orders and every user's order.

Example:
`http://127.0.0.1:8000/api/v1/user/{id}/order/{id}?/`
`http://127.0.0.1:8000/api/v1/user/{id}/order/`

Notes: I implemented this features for looking at DRF possibilities. I didn't configure the access for them, so it may be not a safe case . But it is the student project, so it is OK :)

### Selenium
* test the authentication system using Selenium.

