.PHONY: all
all: .generator
	@rm -rf ./src/datadog_api_client/
	@pre-commit run --all-files --hook-stage=manual openapi-generator || true
	@cp -r v1/datadog_api_client ./src/
	@cp -r v2/datadog_api_client ./src/
	@ls v1/docs/*Api.md | xargs -n1 ./extract-code-blocks.awk -v output="examples/generated/v1"
	@ls v2/docs/*Api.md | xargs -n1 ./extract-code-blocks.awk -v output="examples/generated/v2"
	@rm -rf v1 v2
	@pre-commit run --all-files --hook-stage=manual docs || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual autoflake || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual black || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual api-docs || echo "modified files"
