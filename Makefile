.DEFAULT_GOAL := help

run: ## Run the application using uvicorn with provided arguments or defaults
	poetry run gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker -c gunicorn.conf.py

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'