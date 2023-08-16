# cisco_ping


## Brief description
A simple application with 2 endpoints on it's behalf.
1. **GET** -> `/health` : An endpoint for a base healthcheck
2. **GET** -> `/info` : An endpoint printing a message
3. **POST** -> `/ping` : An endpoint taking body `{"url": url}`, pinging it (**GET** request) and returnig the original body.
4. **GET** -> `/docs` : A Swagger based endpoints documentation
5. **GET** -> `/redoc` : A ReDoc based endpoints documentation


## Usage
All necessary commands can be ran using make.
* `make install` - install app and it's dependencies
* `make start` - start application using uvicorn. Use `ctrl+c` to stop
* `make start-gunicorn` - start application using guvicorn, using 4 workers. Use `ctrl+c` to stop
* `make build-docker-image` - build an image for a dockerized execution. This one is a pre-requisite for all other docker based commands
* `make start-docker` - start a dockerized instance. User `make stop-docker` to stop
* `make stop-docker` - stop a dockerized instance
* `make show-docker-logs` - scroll logs for a running instance. Eg. for debugging. Use `ctrl+c` to stop
* `make terminate-docker` - a hard wat to stop a dockerized instance 


## Testing
All tests can be ran using make.

Unit tests:
* `unit-test`: unit tests using pytest with local changes
* `unit-test-docker`: unit tests on built docker image
* `unit-test-docker-locally`: unit tests on built docker image with local code changes

Api tests:
* `api-test`: api tests usin pytest pytest with local changes
* `api-test-docker`: api tests on built docker image
* `api-test-docker-locally`: api tests on built docker image with local code changes


## Docs
Swagger based docs are exposed via `/docs` or `/redoc` endpoint