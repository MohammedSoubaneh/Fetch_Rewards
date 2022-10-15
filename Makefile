test:
	python rewards/manage.py test rewards/

runserver:
	python rewards/manage.py runserver

install:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
