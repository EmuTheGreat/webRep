local_up:
	docker-compose build --parallel
	docker-compose up

local_down:
	docker-compose down

local_shell:
	docker-compose exec web bash

local_migrate:
	docker-compose exec web python manage.py migrate

local_make_migration:
	docker-compose exec web python manage.py makemigrations

local_create_superuser:
	docker-compose exec web python manage.py createsuperuser

local_django_shell:
	docker-compose exec web python manage.py shell

format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120

lint:
	flake8 . --count --show-source --statistics --max-line-length 120
	isort --check .
	black --check .
