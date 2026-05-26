.PHONY: up upa down build rebuild up-api build-api index logs reset help

help: ## Mostra esta ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

up: ## Sobe todos os serviços em background
	docker compose up -d

upa: ## Sobe apenas a API (com logs)
	docker compose up api

down: ## Para e remove todos os serviços
	docker compose down

rebuild: ## Reconstrói todas as imagens do zero
	docker compose build --no-cache

up-api: ## Reconstrói e sobe tudo
	docker compose build --no-cache api
	docker compose up

build-api: ## Reconstrói a imagem da API em background
	docker compose build --no-cache api -d

index: ## Indexa documentos no ChromaDB (apaga índice anterior)
	docker compose run --rm api python rag/rag.py --reset

logs: ## Acompanha logs da API em tempo real
	docker compose logs -f api

reset: ## Recria volumes do banco (apaga dados!)
	docker compose down -v
	docker compose up -d
