## Tutorial for setting up Django on server:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04

## Files used on FLOM server

### Socket file

```sudo nano /etc/systemd/system/gunicorn.socket```

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

### Systemd service file

```sudo nano /etc/systemd/system/gunicorn.service```

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/FLOM/_software
ExecStart=/home/ubuntu/FLOM/_software/flomenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          flom.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Nginx Configuration

```sudo nano /etc/nginx/sites-available/flom```

```
server {
    listen 80;
    server_name flom.ml;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /home/ubuntu/FLOM/_software/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```