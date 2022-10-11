import pymssql
from dotenv import load_dotenv
from os import getenv

svr = getenv("PYMSSQL_SERVER")
uid = getenv("PYMSSQL_USER")
pwd = getenv("PYMSSQL_PASSWORD")
db = getenv("PYMSSQL_DATABASE")