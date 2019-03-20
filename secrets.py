# telegram bot token
TOKEN = ""

# db constants
DB_USER = "username"
DB_PWD = "password"
DB_HOST = "localhost"
DB_NAME = "database_name"

try:
    from secrets_local import *
except ImportError:
    pass
