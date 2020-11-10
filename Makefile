##
# Scout
#
# @file
# @version 0.1

.DEFAULT_GOAL := help
.PHONY: build run init prune help up down bash-scout

build:    ## Build new images
	docker-compose build
init:    ## Initialize scout database
	docker-compose up --detach
	docker-compose exec scout-cli scout --host db setup database --yes
	docker-compose exec scout-cli scout --host db load panel scout/demo/panel_1.txt
	docker-compose exec scout-cli scout --host db case scout/demo/643594.config.yaml
	echo "Setup scout demo database"
	docker-compose down
up:    ## Run Scout software
	docker-compose up --detach
down:    ## Take down Scout software
	docker-compose down --volumes
bash-scout:    ## Remove dangling images, volumes and used data
	docker-compose exec scout-cli /bin/bash
prune:    ## Remove orphans and dangling images
	docker-compose down --remove-orphans
	docker images prune
help:    ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# end
