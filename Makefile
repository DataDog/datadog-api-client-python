.PHONY: all
all: .generator .env
	@rm -rf ./src/datadog_api_client/v1 ./src/datadog_api_client/v2
	@pre-commit run --all-files --hook-stage=manual generator-v1 || true
	@pre-commit run --all-files --hook-stage=manual generator-v2 || true
	@pre-commit run --all-files --hook-stage=manual docs || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual autoflake || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual black || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual api-docs || echo "modified files"

.PHONY: .env
.env:
	@echo "export UID=$(shell id -u)\nexport GID=$(shell id -g)" > $@
