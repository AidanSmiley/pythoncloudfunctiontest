# construct json to then POST 

from select import select
from flask import escape
import functions_framework
import sqlalchemy
import os

# connection_name = ""   <- change with connection name of my postgresql db
# db_user = "postgres"
# db_pass = ""  #delete before pushing 
# db_name = "onboarding"
# table_name = "foodtruck"

# driver_name = 'postgres+pg8000'
# query_string = dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

@functions_framework.http
def onboard_content(request):

    if request.method == 'POST':
        #POST stuff
        content_type = request.headers['content-type']
        if content_type == 'application/json':
            request_json = request.get_json(silent=True)
            #check if all data thats needed is in the json
        else:
            print("ummmm something went wrong :)")
        
        # do postgres stuff here :)
    elif request.method == 'GET':
        #GET stuff
        content_type = request.headers['content-type']
        if content_type == 'application/json':
            request_json = request.get_json(silent=True)
            #check if all data thats needed is in the json
        else:
            print("ummmm something went wrong :)")
        print("get stuff here :)")
    elif request.method == 'PUT':
        #PUT stuff
        content_type = request.headers['content-type']
        if content_type == 'application/json':
            request_json = request.get_json(silent=True)
            #check if all data thats needed is in the json
        else:
            print("ummmm something went wrong :)")
        print("update stuff here :)")


'''

database connection example

    db = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername = driver_name,
            username = db_user,
            password = db_pass,
            database = db_name,
            query = query_string,
        ),
        pool_size = 5,
        max_overflow = 2,
        pool_timeout = 30,
        pool_recycle = 1800
    )

    stmt = sqlalchemy.text('select name from users where name=\'{}\''.format(escape(input_name)))

    try:
        with db.connect() as conn:
            result = conn.execute(stmt)

            return 'the name is {}'.format(escape(result.fetchall()))
    except Exception as e:
        return 'Error: {}'.format(str(e))
'''

