import psycopg2
import yaml

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def database(action):
    try:
        #   connect to exist database
        connection = psycopg2.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['db_name']
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            if action == 'insert':
                cursor.execute(
                     """INSERT INTO "cmngr_user" (name) VALUES 
                    ('petuhan');""")
                print("[INFO] Data inserted successfully")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

