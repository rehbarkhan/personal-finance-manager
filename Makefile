.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8080

.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate