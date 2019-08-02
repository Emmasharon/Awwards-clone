# Awwards-clone

## Description
This is a django application that allow a user to post a project he/she has created and get it reviewed by his/her peers.

#### Link to deployed site
https://emmAwwards.herokuapp.com

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Contributing](#contributing)
4. [Bugs](#bugs)
5. [Contact me](#support-and-contact-details)
6. [Licensing](#license)

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
|request page       | click horuku link url | view images          |                    
|sign up      | registration form  | login page         |
|login        | login form  | timeline page         |
|profile  | click on profile icon | view profile page  |
|post  | click on upload icon | upload a project  |
|view all posts | click on timeline page | user goes to page containing all posts|  

## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django
    -AJAX
    -RESTful API

#### Clone the Repo and rename it to suit your needs.
```bash
git clone git@github.com:emmasharon/Awwards-clone.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <https://github.com/Emmasharon/Awwards-clone.git>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)


## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
None

#### Known bugs
 - N/A

