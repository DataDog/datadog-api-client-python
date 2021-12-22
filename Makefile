.PHONY: all
all: .generator .env
	@./generate.sh
	@mkdir -p docs/v1 docs/v2
	@cp -r v1/datadog_api_client ./src/
	@cp -r v2/datadog_api_client ./src/
	@cp -r v1/docs/* ./docs/v1/
	@cp -r v2/docs/* ./docs/v2/
	@cp v1/README.md ./docs/v1/
	@cp v2/README.md ./docs/v2/
	@rm -rf v1 v2
	@pre-commit run --all-files --hook-stage=manual docs || echo "modified files"
	@pre-commit run --all-files --hook-stage=manual black || echo "modified files"

.PHONY: .env
.env:
	@echo "export UID=$(shell id -u)\nexport GID=$(shell id -g)" > $@
