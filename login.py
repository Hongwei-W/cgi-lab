#!/usr/bin/env python3 

import cgi, cgitb, os
from tokenize import cookie_re
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie


# set up cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# form_ok = username == secret.username and pasword == secret.password
form_okay = False
if username == secret.username and password == secret.password:
    form_okay = True

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None

if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value
cookie_okay = False
if cookie_username == secret.username and cookie_password == secret.password:
    cookie_okay = True

if cookie_okay:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_okay:
    # set cookie only when login info is correct 
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

