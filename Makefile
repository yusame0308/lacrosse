run:
	python manage.py runserver

migrate:
	python manage.py migrate

secretkey:
	python lacrosse/generate_secretkey_setting.py > lacrosse/settings_local.py

create-admin-user:
	python manage.py createsuperuser

build-railway:
	make secretkey
	make migrate
	