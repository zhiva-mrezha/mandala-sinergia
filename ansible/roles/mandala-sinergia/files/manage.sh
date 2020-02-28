export SECRET_KEY='{{secret_key}}'
export DB_HOST='localhost'
export DB_PASSWORD='{{db_password}}'
export DB_NAME='{{db_name}}'
export DB_USER='{{db_user}}'
export OIDC_RP_CLIENT_ID='{{ oidc_client_id }}'
export OIDC_RP_CLIENT_SECRET='{{ oidc_client_secret }}'


venv/bin/python manage.py $@
