install:
	pip install poetry && poetry install
	
start:
	cd src/fastapi_pres && \
		uvicorn app:app --host 0.0.0.0 --port 9000

start-gunicorn:
	cd src/fastapi_pres && \
		gunicorn app:app --bind 0.0.0.0:9000 -w 4 -k uvicorn.workers.UvicornWorker

build-docker-image:
	docker build . --network host -t fastapi_pres

start-docker:
	docker run -d -p 9000:9000 fastapi_pres:latest

stop-docker:
	docker ps -q --filter ancestor=fastapi_pres | xargs docker stop

show-docker-logs:
	docker ps -q --filter ancestor=fastapi_pres | xargs docker logs -f

terminate-docker:
	docker ps -q --filter ancestor=fastapi_pres | xargs docker rm -f

unit-test:
	pytest tests/unit -v

unit-test-docker:
	docker container run fastapi_pres:latest pytest tests/unit -v

unit-test-docker-locally:
	docker container run -v ${PWD}:/app/ fastapi_pres:latest pytest tests/unit -v

api-test:
	pytest tests/api -v

api-test-docker:
	docker container run fastapi_pres:latest pytest tests/api -v

api-test-docker-locally:
	docker container run -v ${PWD}:/app/ fastapi_pres:latest pytest tests/api -v
