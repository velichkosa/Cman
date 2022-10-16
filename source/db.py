import psycopg2
import yaml

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def database(action, user_id, first_name):
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
            if action == 'registration':
                cursor.execute(
                     f"INSERT INTO cmngr_user (name, user_id) VALUES ('{first_name}', {user_id});")
                print("[INFO] Data inserted successfully")
                return True
            if action == 'start':
                print(user_id)
                cursor.execute(
                     f"SELECT name FROM cmngr_user WHERE user_id={user_id};")
                return cursor.rowcount

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

