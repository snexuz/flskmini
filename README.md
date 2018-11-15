
## Minimal Flask Instance

### requirements
- Flask==1.0.2
- Flask-Admin==1.5.2
- Flask-Bootstrap==3.3.7.1
    - [intergrated with Bootswatch theme](https://bootswatch.com/)
        - change theme from `templates\base.html`::`{% set theme = 'cosmo' %}`
- Flask-SQLAlchemy==2.3.2
- Flask-Migrate==2.3.0 
- gunicorn==19.9.0

### virtualenv
```
virtualenv env
source env/bin/activate
python36 -m pip install -r requirements.txt
```

### DB init & migration
```
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

### run app
```
python -m flask run
```

### flask shell
```
python -m flask shell
```

## Depolyeement
- [Install Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7)
- [Serve Flask Applications](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)

### gunicorn
- `sudo systemctl start flskmini.service`

```
#/etc/systemd/system/flskmini.service

[Unit]
Description=Gunicorn instance to serve flskmini
After=network.target

[Service]
WorkingDirectory=/home/usr/flskmini
Environment="PATH=/home/usr/flskmini/env/bin"
ExecStart=/home/usr/flskmini/env/bin/gunicorn --workers 3 --bind unix:flskmini.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target

```

### Nginx
- `sudo nginx -s reload`
```
#/etc/nginx/nginx.conf

location / {
    proxy_http_version 1.1;
    client_max_body_size 8m;    
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
	proxy_pass http://unix:/home/usr/flskmini/flskmini.sock;
}
```