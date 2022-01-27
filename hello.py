#!/usr/bin/env python3

import os, json

# print as plain text
# print("content-Type: text/plain")
# print()
# print(os.environ)

# print as json
# print("content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

# extract query_data and give it as html
# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# extract users_browser and give it as html
print("Content-Type: text/html")
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")