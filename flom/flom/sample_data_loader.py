# create table in db
# fill with sample test data

import psycopg2
 
def connect(params):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=params['HOST'],database=params['NAME'], user=params['USER'], password=params['PASSWORD'])
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_tables(config):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE library_occupancy (
            id          SERIAL PRIMARY KEY,
            room_number INTEGER UNIQUE NOT NULL,
            time_entered timestamptz,
            time_exited timestamptz
        );
        """,
        """
        CREATE TABLE room_stats (
                room_number INTEGER PRIMARY KEY,
                total_time_occupied INTEGER NOT NULL,
                total_times_used INTEGER NOT NULL,
                FOREIGN KEY (room_number)
                REFERENCES library_occupancy (room_number)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """)
    conn = None
    try:
        # read the connection parameters

        # connect to the PostgreSQL server
        params ={}
        params['host'] = config['HOST']
        params['database'] = config['NAME']
        params['user'] = config['USER']
        params['password'] = config['PASSWORD']
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        # for command in commands:
        cur.execute(commands[0])
        cur.execute(commands[1])
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 