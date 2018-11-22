# Gandharva Web Application 2019
Gandharva Event of VIIT College tentatively in March'19

## Steps to run the project

> Prerequisites : virtualenv

```sudo pip3 install virtualenv```

Steps :
1) Clone the repository
2) Inside the main project folder
```source venv/bin/activate```
3) python3 manage.py runserver
4) Open http://127.0.0.1:8000/ in the browser.

## For future contributors :

Location of important files :

1) Service worker stored at **template root**. This is important as it can only cache files at its scope.
2) urls.py has been updated to give location of above mentioned service worker.
3) Service worker has been registered at **base.html**, so that any other page which extends base.html **is also cached**.
