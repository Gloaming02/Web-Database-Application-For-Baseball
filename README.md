# Web-Database-Application-For-Baseball
Web-database application for the most recent Lahman baseball database.

Group Project

Group Name: KHz

Group Member:

    Zhengyan Hu
    
    Jingke Shi
    

Using Instructions
    1. unzip the project
    2. cd <project-dir>
Set Up Environment:
    3. python -m venv venv
    4  Linux/Mac: source venv/bin/activate 
        Windows: venv\Scripts\activate
    5. pip install -r requirements.txt
Create database:
    6. mysql -u root -p
    7. source KHz.sql
    8. exit;
Load data: 
    9. python data.py
    (Before: Change csi3335fall2021.py to your database username and password)
Run flask server:
    python baseball.py

Python Modules Imported:
import os
import mysql.connector
import sys
import csv
import csi3335fall2021
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy
from flask import request, render_template, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import and_
from sqlalchemy.orm import aliased
from sqlalchemy.sql.functions import concat, sysdate, func
from werkzeug.utils import redirect
from flask_login import UserMixin
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

PS: 
1. At the top left of the page, left of the MLB picture, you can select your favorite team or switch to display the standings.


