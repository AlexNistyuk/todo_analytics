up-aws:
	docker-compose up -d localstack_app
up-build:
	docker-compose up -d --build $(c)
down:
	docker-compose down $(c)
restart:
	docker-compose stop $(c)
	docker-compose up -d --build $(c)
