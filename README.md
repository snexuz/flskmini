
## Minimal Flask Instance

### Requirements
- Flask==1.0.2
- Flask-Admin==1.5.2
- Flask-Bootstrap==3.3.7.1
- Flask-Migrate==2.3.0
- Flask-SQLAlchemy==2.3.2
- [intergrated with Bootswatch theme](https://bootswatch.com/)
    - change theme from `templates\base.html`::`{% set theme = 'cosmo' %}`

### run app
python -m flask run

### app init & migration
python -m flask db init
python -m flask db migrate
python -m flask db upgrade

### flask shell
python -m flask shell

