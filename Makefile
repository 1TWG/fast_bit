start:
	uvicorn main:api --reload

freezevenv:
	pip freeze > requirements.txt


install:
	python3 -m pip install -r requirements.txt
