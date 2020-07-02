# Verilog Master

![](https://img.shields.io/github/license/CybSec-NITW/WeaponHEX)
![](https://img.shields.io/pypi/pyversions/django.svg)

Verilog is a hardware descriptive language used to model modern day digital systems like flip-flops, memories and microprocessors. It is a very powerful tool to design and simulate digital hardwares at any level.

This project is about providing an interactive environment for hardware enthusiasts to learn this language.

## Instructions

Make sure you have Git and Python installed on your machine. If not, you can download and install them from here: https://git-scm.com/downloads https://www.python.org/downloads/

Open a terminal and change current directory to your dev or projects folder.

Then follow these steps

```
$ pip3 install virtualenv
$ mkdir verilog-master
$ cd verilog-master
$ git clone https://github.com/codingforentrepreneurs/Reactify-Django .
$ virtualenv -p python3 .
$ source bin/activate   #For MAC/Linux -> . bin/activate
(verilog-master) $ pip3 install -r requirements.txt
(verilog-master) $ cd src
(verilog-master) $ python3 manage.py makemigrations
(verilog-master) $ pyton3 manage.py migrate
(verilog-master) $ python3 manage.py runserver

It will deploy the website on your localhost https://127.0.0.1:8000
```

## Admin login

Django provides a default admin interface which can be used to perform create, read, update and delete operations on the models and manage users directly.

Open https://127.0.0.1:8000/admin

Default credentials are

Username -> admin

Password -> admin
