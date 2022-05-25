.PHONY: all
all: .generator
	@rm -rf ./src/datadog_api_client/v1 ./src/datadog_api_client/v2 src/datadog_api_client/{api_client.py,configuration.py,exceptions.py,model_utils.py,rest.py} examples/*
	@pre-commit run --all-files --hook-stage=manual generator || true
	@pre-commit run --all-files --hook-stage=manual examples || true
	@pre-commit run --all-files --hook-stage=manual docs || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual autoflake || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual black || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual api-docs || echo "modified files"
