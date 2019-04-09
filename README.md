# FLOM

### Folsom Library Occupancy Manager

http://www.flom.ml

Develop an embedded system that allows students to sign into a website with their RCS ID to check what study rooms in the library are occupied and which are not. This will increase students' efficiency when studying. 

## Build Instructions

Clone the URI and run the `manage.py` file located in the \_software directory.

`python manage.py runserver`

Your local build will require access to a database. Our implementation uses [Postgres](https://www.postgresql.org/) and you can create a `config.ini` file with data to your local database. Alternatively, we can set you up with access to our AWS database if you reach out.

You may need to download these python libraries (if you don't already have them).

```pip install Django``` \
```pip install psycopg2``` \
```pip install memcache``` 
