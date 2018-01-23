# Simple social network in Django and demonstrate bot
![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg) ![django2.x](https://img.shields.io/badge/%20Django-2.0.1-green.svg)

## Dependencies
* Django
* BeautifulSoup

## Setting up

##### Clone the repo

```
$ git clone https://github.com/Lenainweb/simple_social_network_in_Django_and_demonstrate_bot.git
$ cd simple_social_network_in_Django_and_demonstrate_bot/social_network_Django
```

##### Initialize a virtualenv

```
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Create the database

```
$ python manage.py migrate
```

## Running the server

```
$ python manage.py runserver
```

Оpen another terminal

```
$ cd simple_social_network_in_Django_and_demonstrate_bot/robot
```

Close the browser


##### In the configuration file, set the acceptable values


* `NUMBER_OF_USERS`: Number of users to be registered.
* `MAX_POST_PER_USER`: The maximum number of records that a user can publish.
* `MAX_LIKES_PER_USER`: The maximum number of likes a user can put.
* `TIMEPAUS`: Number of seconds between requests.
* `LOGIN_LENGTH`: Number of symbols in login.
* `PASSWORD_LENGTH`: Number of symbols in password.


## Running the application

```
$ python3 robot.py
```


