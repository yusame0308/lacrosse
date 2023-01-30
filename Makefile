run:
	python manage.py runserver

migrate:
	python manage.py migrate

secretkey:
	python lacrosse/generate_secretkey_setting.py > lacrosse/settings_local.py

init:
	make secretkey
	make migrate
	make run