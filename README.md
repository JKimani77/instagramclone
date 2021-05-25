# Instagram Clone
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Description
This a web application built using Python and Django. The app is basically a clone of the instagram app, you can post photos under your account and view them. You can also follow other users and ccomment on photos.


## Author

Joshua Kimani

## Link to site
https://eansta.herokuapp.com/

# Installation

## Clone
    
```bash
    git clone https://github.com/JKimani77/instagramclone.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Create SQLDatabase and configure settings


## Run initial migration
```bash
   $ python3.6 manage.py makemigrations insta
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```

## Known Bugs
-The search functionality is not working properly
-User profile page

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    
    Python 3.6
    Django
    Bootstrap Materialize
    HTML
    PostgreSQL



## License
[LICENSE](LICENSE)
