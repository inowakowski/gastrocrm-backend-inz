bind        =   "0.0.0.0:8080"
workers     =   2
accesslog   =   "-"
proc_name   =   "gastrocrm-gunicorn-app"
chdir       =   "/app"
# raw_env     =   [ "ENVIRONMENT=production" ]
user        =   "www-data"
group       =   "www-data"
