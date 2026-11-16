@endpoint(ai-gateway) @endpoint(ai-gateway-v2)
Feature: AI Gateway
  AI Gateway routes your applications' LLM requests to the model providers
  you connect, and applies your organization's routing, access, spending,
  rate limit, and data capture rules.  These endpoints allow you to
  configure:  - Providers: the model providers your organization connects,
  and the models and pricing each offers. - Routing rules: the named routes
  your applications call, and the models that serve each one. - Access:
  inbound routing policies and model groups that decide who can use which
  models. - Budgets and rate limits: spending caps and request limits, and
  their current usage. - Data capture and governance: what request data is
  recorded, and organization-wide controls.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AIGateway" API

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Add a model to an AI Gateway provider returns "Bad Request" response
    Given operation "CreateAiGatewayModel" enabled
    And new "CreateAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Add a model to an AI Gateway provider returns "Created" response
    Given operation "CreateAiGatewayModel" enabled
    And new "CreateAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Add multiple models to an AI Gateway provider returns "Bad Request" response
    Given operation "BulkCreateAiGatewayModels" enabled
    And new "BulkCreateAiGatewayModels" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"models": [{"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}]}, "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Add multiple models to an AI Gateway provider returns "Created" response
    Given operation "BulkCreateAiGatewayModels" enabled
    And new "BulkCreateAiGatewayModels" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"models": [{"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}]}, "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Archive an AI Gateway budget returns "No Content" response
    Given operation "DeleteAiGatewayBudget" enabled
    And new "DeleteAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Archive an AI Gateway budget returns "Not Found" response
    Given operation "DeleteAiGatewayBudget" enabled
    And new "DeleteAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Archive an AI Gateway rate limit returns "No Content" response
    Given operation "DeleteAiGatewayRateLimit" enabled
    And new "DeleteAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Archive an AI Gateway rate limit returns "Not Found" response
    Given operation "DeleteAiGatewayRateLimit" enabled
    And new "DeleteAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway budget returns "Bad Request" response
    Given operation "CreateAiGatewayBudget" enabled
    And new "CreateAiGatewayBudget" request
    And body with value {"data": {"attributes": {"capacity_microcents": 100000000, "enforcement": "BLOCK", "name": "Coding agents", "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "tags": {"model": "gpt-5.2-codex"}, "track_existing": false, "warning_threshold": 0.9, "window_policy": "MONTHLY"}, "type": "budgets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway budget returns "Conflict" response
    Given operation "CreateAiGatewayBudget" enabled
    And new "CreateAiGatewayBudget" request
    And body with value {"data": {"attributes": {"capacity_microcents": 100000000, "enforcement": "BLOCK", "name": "Coding agents", "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "tags": {"model": "gpt-5.2-codex"}, "track_existing": false, "warning_threshold": 0.9, "window_policy": "MONTHLY"}, "type": "budgets"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway budget returns "Created" response
    Given operation "CreateAiGatewayBudget" enabled
    And new "CreateAiGatewayBudget" request
    And body with value {"data": {"attributes": {"capacity_microcents": 100000000, "enforcement": "BLOCK", "name": "Coding agents", "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "tags": {"model": "gpt-5.2-codex"}, "track_existing": false, "warning_threshold": 0.9, "window_policy": "MONTHLY"}, "type": "budgets"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway data capture override returns "Bad Request" response
    Given operation "CreateAiGatewayDataCaptureOverride" enabled
    And new "CreateAiGatewayDataCaptureOverride" request
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway data capture override returns "Conflict" response
    Given operation "CreateAiGatewayDataCaptureOverride" enabled
    And new "CreateAiGatewayDataCaptureOverride" request
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway data capture override returns "Created" response
    Given operation "CreateAiGatewayDataCaptureOverride" enabled
    And new "CreateAiGatewayDataCaptureOverride" request
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway model group returns "Bad Request" response
    Given operation "CreateAiGatewayModelGroup" enabled
    And new "CreateAiGatewayModelGroup" request
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "bindings": [{"principals": ["user:55555555-5555-5555-5555-555555555555"], "relation": "runner"}], "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "type": "model-groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway model group returns "Conflict" response
    Given operation "CreateAiGatewayModelGroup" enabled
    And new "CreateAiGatewayModelGroup" request
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "bindings": [{"principals": ["user:55555555-5555-5555-5555-555555555555"], "relation": "runner"}], "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "type": "model-groups"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway model group returns "Created" response
    Given operation "CreateAiGatewayModelGroup" enabled
    And new "CreateAiGatewayModelGroup" request
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "bindings": [{"principals": ["user:55555555-5555-5555-5555-555555555555"], "relation": "runner"}], "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "type": "model-groups"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway provider returns "Bad Request" response
    Given operation "CreateAiGatewayProvider" enabled
    And new "CreateAiGatewayProvider" request
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "initial_bindings": [{"principals": ["org:11111111-1111-1111-1111-111111111111"], "relation": "viewer"}], "integration_account_id": "account-123", "integration_config": {"bedrock_region": "us-east-1", "foundry_project": "my-project", "foundry_resource_id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/ai/providers/Microsoft.CognitiveServices/accounts/my-foundry", "location": "us-central1", "project_id": "my-gcp-project", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "known_provider": "openai", "models": [{"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}], "name": "production-us", "slug": "prod-us"}, "type": "providers"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway provider returns "Conflict" response
    Given operation "CreateAiGatewayProvider" enabled
    And new "CreateAiGatewayProvider" request
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "initial_bindings": [{"principals": ["org:11111111-1111-1111-1111-111111111111"], "relation": "viewer"}], "integration_account_id": "account-123", "integration_config": {"bedrock_region": "us-east-1", "foundry_project": "my-project", "foundry_resource_id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/ai/providers/Microsoft.CognitiveServices/accounts/my-foundry", "location": "us-central1", "project_id": "my-gcp-project", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "known_provider": "openai", "models": [{"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}], "name": "production-us", "slug": "prod-us"}, "type": "providers"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway provider returns "Created" response
    Given operation "CreateAiGatewayProvider" enabled
    And new "CreateAiGatewayProvider" request
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "initial_bindings": [{"principals": ["org:11111111-1111-1111-1111-111111111111"], "relation": "viewer"}], "integration_account_id": "account-123", "integration_config": {"bedrock_region": "us-east-1", "foundry_project": "my-project", "foundry_resource_id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/ai/providers/Microsoft.CognitiveServices/accounts/my-foundry", "location": "us-central1", "project_id": "my-gcp-project", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "known_provider": "openai", "models": [{"model_id_canonical": "gpt-5.2-codex", "model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}], "name": "production-us", "slug": "prod-us"}, "type": "providers"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway rate limit returns "Bad Request" response
    Given operation "CreateAiGatewayRateLimit" enabled
    And new "CreateAiGatewayRateLimit" request
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": 100000000, "input_tokens_per_minute": null, "mode": "ALERT", "name": "Default rate limit", "output_tokens_per_minute": null, "requests_per_minute": 600, "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "team_id": "00000000-0000-4000-8000-000000000002", "user_id": "00000000-0000-4000-8000-000000000001"}, "type": "rate-limits"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway rate limit returns "Conflict" response
    Given operation "CreateAiGatewayRateLimit" enabled
    And new "CreateAiGatewayRateLimit" request
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": 100000000, "input_tokens_per_minute": null, "mode": "ALERT", "name": "Default rate limit", "output_tokens_per_minute": null, "requests_per_minute": 600, "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "team_id": "00000000-0000-4000-8000-000000000002", "user_id": "00000000-0000-4000-8000-000000000001"}, "type": "rate-limits"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway rate limit returns "Created" response
    Given operation "CreateAiGatewayRateLimit" enabled
    And new "CreateAiGatewayRateLimit" request
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": 100000000, "input_tokens_per_minute": null, "mode": "ALERT", "name": "Default rate limit", "output_tokens_per_minute": null, "requests_per_minute": 600, "selector": [{"dim": "user_id", "per_value": true, "values": ["11111111-1111-1111-1111-111111111111"]}], "team_id": "00000000-0000-4000-8000-000000000002", "user_id": "00000000-0000-4000-8000-000000000001"}, "type": "rate-limits"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway routing rule returns "Bad Request" response
    Given operation "CreateAiGatewayRoutingRule" enabled
    And new "CreateAiGatewayRoutingRule" request
    And body with value {"data": {"attributes": {"slug": "coding", "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "type": "routing-rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway routing rule returns "Conflict" response
    Given operation "CreateAiGatewayRoutingRule" enabled
    And new "CreateAiGatewayRoutingRule" request
    And body with value {"data": {"attributes": {"slug": "coding", "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "type": "routing-rules"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create an AI Gateway routing rule returns "Created" response
    Given operation "CreateAiGatewayRoutingRule" enabled
    And new "CreateAiGatewayRoutingRule" request
    And body with value {"data": {"attributes": {"slug": "coding", "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "type": "routing-rules"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create or replace an AI Gateway routing policy returns "Bad Request" response
    Given operation "UpsertAiGatewayPolicy" enabled
    And new "UpsertAiGatewayPolicy" request
    And body with value {"data": {"attributes": {"inbound": "coding-agent", "priority": 1, "tiers": [{"priority": 1, "targets": [{"id": 901, "model": "gpt-5.2-codex", "provider": "prod-us"}]}]}, "type": "routing-documents"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Create or replace an AI Gateway routing policy returns "OK" response
    Given operation "UpsertAiGatewayPolicy" enabled
    And new "UpsertAiGatewayPolicy" request
    And body with value {"data": {"attributes": {"inbound": "coding-agent", "priority": 1, "tiers": [{"priority": 1, "targets": [{"id": 901, "model": "gpt-5.2-codex", "provider": "prod-us"}]}]}, "type": "routing-documents"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete a model from an AI Gateway provider returns "No Content" response
    Given operation "DeleteAiGatewayModel" enabled
    And new "DeleteAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete a model from an AI Gateway provider returns "Not Found" response
    Given operation "DeleteAiGatewayModel" enabled
    And new "DeleteAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete a model pricing override returns "Bad Request" response
    Given operation "DeleteAiGatewayModelPricing" enabled
    And new "DeleteAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete a model pricing override returns "No Content" response
    Given operation "DeleteAiGatewayModelPricing" enabled
    And new "DeleteAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete a model pricing override returns "Not Found" response
    Given operation "DeleteAiGatewayModelPricing" enabled
    And new "DeleteAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway data capture override returns "Bad Request" response
    Given operation "DeleteAiGatewayDataCaptureOverride" enabled
    And new "DeleteAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway data capture override returns "Conflict" response
    Given operation "DeleteAiGatewayDataCaptureOverride" enabled
    And new "DeleteAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway data capture override returns "No Content" response
    Given operation "DeleteAiGatewayDataCaptureOverride" enabled
    And new "DeleteAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway data capture override returns "Not Found" response
    Given operation "DeleteAiGatewayDataCaptureOverride" enabled
    And new "DeleteAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway model group returns "Bad Request" response
    Given operation "DeleteAiGatewayModelGroup" enabled
    And new "DeleteAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway model group returns "No Content" response
    Given operation "DeleteAiGatewayModelGroup" enabled
    And new "DeleteAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway model group returns "Not Found" response
    Given operation "DeleteAiGatewayModelGroup" enabled
    And new "DeleteAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway provider returns "Bad Request" response
    Given operation "DeleteAiGatewayProvider" enabled
    And new "DeleteAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway provider returns "Conflict" response
    Given operation "DeleteAiGatewayProvider" enabled
    And new "DeleteAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway provider returns "No Content" response
    Given operation "DeleteAiGatewayProvider" enabled
    And new "DeleteAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway provider returns "Not Found" response
    Given operation "DeleteAiGatewayProvider" enabled
    And new "DeleteAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway routing policy returns "No Content" response
    Given operation "DeleteAiGatewayPolicy" enabled
    And new "DeleteAiGatewayPolicy" request
    And request contains "inbound" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway routing policy returns "Not Found" response
    Given operation "DeleteAiGatewayPolicy" enabled
    And new "DeleteAiGatewayPolicy" request
    And request contains "inbound" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway routing rule returns "Conflict" response
    Given operation "DeleteAiGatewayRoutingRule" enabled
    And new "DeleteAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway routing rule returns "No Content" response
    Given operation "DeleteAiGatewayRoutingRule" enabled
    And new "DeleteAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Delete an AI Gateway routing rule returns "Not Found" response
    Given operation "DeleteAiGatewayRoutingRule" enabled
    And new "DeleteAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/frontier-prd-gateway
  Scenario: Get AI Gateway governance controls returns "OK" response
    Given operation "GetAiGatewayGovernance" enabled
    And new "GetAiGatewayGovernance" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get AI Gateway rate limit usage returns "OK" response
    Given operation "GetAiGatewayRateLimitUsage" enabled
    And new "GetAiGatewayRateLimitUsage" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get a model pricing override returns "Bad Request" response
    Given operation "GetAiGatewayModelPricing" enabled
    And new "GetAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get a model pricing override returns "Not Found" response
    Given operation "GetAiGatewayModelPricing" enabled
    And new "GetAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get a model pricing override returns "OK" response
    Given operation "GetAiGatewayModelPricing" enabled
    And new "GetAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget instance summary returns "Bad Request" response
    Given operation "GetAiGatewayBudgetInstancesSummary" enabled
    And new "GetAiGatewayBudgetInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget instance summary returns "Not Found" response
    Given operation "GetAiGatewayBudgetInstancesSummary" enabled
    And new "GetAiGatewayBudgetInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget instance summary returns "OK" response
    Given operation "GetAiGatewayBudgetInstancesSummary" enabled
    And new "GetAiGatewayBudgetInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget returns "Not Found" response
    Given operation "GetAiGatewayBudget" enabled
    And new "GetAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget returns "OK" response
    Given operation "GetAiGatewayBudget" enabled
    And new "GetAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget's current period returns "Not Found" response
    Given operation "GetAiGatewayBudgetCurrentPeriod" enabled
    And new "GetAiGatewayBudgetCurrentPeriod" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway budget's current period returns "OK" response
    Given operation "GetAiGatewayBudgetCurrentPeriod" enabled
    And new "GetAiGatewayBudgetCurrentPeriod" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway model group returns "Bad Request" response
    Given operation "GetAiGatewayModelGroup" enabled
    And new "GetAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway model group returns "Not Found" response
    Given operation "GetAiGatewayModelGroup" enabled
    And new "GetAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway model group returns "OK" response
    Given operation "GetAiGatewayModelGroup" enabled
    And new "GetAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway provider returns "Not Found" response
    Given operation "GetAiGatewayProvider" enabled
    And new "GetAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway provider returns "OK" response
    Given operation "GetAiGatewayProvider" enabled
    And new "GetAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway rate limit counter summary returns "Bad Request" response
    Given operation "GetAiGatewayRateLimitInstancesSummary" enabled
    And new "GetAiGatewayRateLimitInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway rate limit counter summary returns "Not Found" response
    Given operation "GetAiGatewayRateLimitInstancesSummary" enabled
    And new "GetAiGatewayRateLimitInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway rate limit counter summary returns "OK" response
    Given operation "GetAiGatewayRateLimitInstancesSummary" enabled
    And new "GetAiGatewayRateLimitInstancesSummary" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway rate limit returns "Not Found" response
    Given operation "GetAiGatewayRateLimit" enabled
    And new "GetAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway rate limit returns "OK" response
    Given operation "GetAiGatewayRateLimit" enabled
    And new "GetAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway routing policy returns "Not Found" response
    Given operation "GetAiGatewayPolicy" enabled
    And new "GetAiGatewayPolicy" request
    And request contains "inbound" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway routing policy returns "OK" response
    Given operation "GetAiGatewayPolicy" enabled
    And new "GetAiGatewayPolicy" request
    And request contains "inbound" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway routing rule returns "Not Found" response
    Given operation "GetAiGatewayRoutingRule" enabled
    And new "GetAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Get an AI Gateway routing rule returns "OK" response
    Given operation "GetAiGatewayRoutingRule" enabled
    And new "GetAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: Get the AI Gateway data capture configuration returns "OK" response
    Given operation "GetAiGatewayDataCaptureConfiguration" enabled
    And new "GetAiGatewayDataCaptureConfiguration" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instance dimension values returns "Bad Request" response
    Given operation "ListAiGatewayBudgetInstanceDimensions" enabled
    And new "ListAiGatewayBudgetInstanceDimensions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instance dimension values returns "Not Found" response
    Given operation "ListAiGatewayBudgetInstanceDimensions" enabled
    And new "ListAiGatewayBudgetInstanceDimensions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instance dimension values returns "OK" response
    Given operation "ListAiGatewayBudgetInstanceDimensions" enabled
    And new "ListAiGatewayBudgetInstanceDimensions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instances returns "Bad Request" response
    Given operation "ListAiGatewayBudgetInstances" enabled
    And new "ListAiGatewayBudgetInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instances returns "Not Found" response
    Given operation "ListAiGatewayBudgetInstances" enabled
    And new "ListAiGatewayBudgetInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budget instances returns "OK" response
    Given operation "ListAiGatewayBudgetInstances" enabled
    And new "ListAiGatewayBudgetInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway budgets returns "OK" response
    Given operation "ListAiGatewayBudgets" enabled
    And new "ListAiGatewayBudgets" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway model groups returns "OK" response
    Given operation "ListAiGatewayModelGroups" enabled
    And new "ListAiGatewayModelGroups" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway models by canonical ID returns "OK" response
    Given operation "ListAiGatewayModelsByCanonical" enabled
    And new "ListAiGatewayModelsByCanonical" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway providers returns "OK" response
    Given operation "ListAiGatewayProviders" enabled
    And new "ListAiGatewayProviders" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway rate limit counter summaries returns "OK" response
    Given operation "ListAiGatewayRateLimitInstancesSummaries" enabled
    And there is a valid "rate_limit_template" in the system
    And new "ListAiGatewayRateLimitInstancesSummaries" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ rate_limit_template.data.id }}"
    And the response "data" has item with field "attributes.rate_limit_id" with value "{{ rate_limit_template.data.id }}"
    And the response "data[0].type" is equal to "rate-limit-instances-summary"
    And the response "data[0].attributes" has field "instance_count"
    And the response "data[0].attributes" has field "truncated"
    And the response "data[0].attributes" has field "scope_restricted"

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway rate limit counters returns "Bad Request" response
    Given operation "ListAiGatewayRateLimitInstances" enabled
    And new "ListAiGatewayRateLimitInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway rate limit counters returns "Not Found" response
    Given operation "ListAiGatewayRateLimitInstances" enabled
    And new "ListAiGatewayRateLimitInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway rate limit counters returns "OK" response
    Given operation "ListAiGatewayRateLimitInstances" enabled
    And new "ListAiGatewayRateLimitInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway rate limits returns "OK" response
    Given operation "ListAiGatewayRateLimits" enabled
    And new "ListAiGatewayRateLimits" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway routing policies returns "OK" response
    Given operation "ListAiGatewayPolicies" enabled
    And new "ListAiGatewayPolicies" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/frontier-prd-gateway
  Scenario: List AI Gateway routing rules returns "OK" response
    Given operation "ListAiGatewayRoutingRules" enabled
    And new "ListAiGatewayRoutingRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List models available from a provider integration returns "Bad Request" response
    Given operation "ListAiGatewayProviderModels" enabled
    And new "ListAiGatewayProviderModels" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    And request contains "integration_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List models available from a provider integration returns "OK" response
    Given operation "ListAiGatewayProviderModels" enabled
    And new "ListAiGatewayProviderModels" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    And request contains "integration_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: List models for an AI Gateway provider returns "OK" response
    Given operation "ListAiGatewayModels" enabled
    And new "ListAiGatewayModels" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Override a budget instance's capacity returns "Bad Request" response
    Given operation "OverrideAiGatewayBudgetInstanceCapacity" enabled
    And new "OverrideAiGatewayBudgetInstanceCapacity" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"capacity_microcents": 250000000, "instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Temporary increase for a launch week"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Override a budget instance's capacity returns "Not Found" response
    Given operation "OverrideAiGatewayBudgetInstanceCapacity" enabled
    And new "OverrideAiGatewayBudgetInstanceCapacity" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"capacity_microcents": 250000000, "instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Temporary increase for a launch week"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Override a budget instance's capacity returns "OK" response
    Given operation "OverrideAiGatewayBudgetInstanceCapacity" enabled
    And new "OverrideAiGatewayBudgetInstanceCapacity" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"capacity_microcents": 250000000, "instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Temporary increase for a launch week"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace AI Gateway governance controls returns "Bad Request" response
    Given operation "UpdateAiGatewayGovernance" enabled
    And new "UpdateAiGatewayGovernance" request
    And body with value {"data": {"attributes": {"data_capture_mode": "metadata_only", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "zdr_mode": "off"}, "id": "organization", "type": "governance"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace AI Gateway governance controls returns "OK" response
    Given operation "UpdateAiGatewayGovernance" enabled
    And new "UpdateAiGatewayGovernance" request
    And body with value {"data": {"attributes": {"data_capture_mode": "metadata_only", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "zdr_mode": "off"}, "id": "organization", "type": "governance"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace an AI Gateway data capture override returns "Bad Request" response
    Given operation "UpdateAiGatewayDataCaptureOverride" enabled
    And new "UpdateAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace an AI Gateway data capture override returns "Conflict" response
    Given operation "UpdateAiGatewayDataCaptureOverride" enabled
    And new "UpdateAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace an AI Gateway data capture override returns "Not Found" response
    Given operation "UpdateAiGatewayDataCaptureOverride" enabled
    And new "UpdateAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Replace an AI Gateway data capture override returns "OK" response
    Given operation "UpdateAiGatewayDataCaptureOverride" enabled
    And new "UpdateAiGatewayDataCaptureOverride" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"configuration_revision": "capture-revision-1", "metadata_capture": ["tool_usage", "tool_output_size", "tool_names"], "mode": "metadata_only", "name": "Research", "operation": "create", "revision": 1, "scope": {"tags": {"env": "prod"}}}, "id": "11111111-1111-4111-8111-111111111111", "type": "data-capture-overrides"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Reset a budget instance's spend returns "Bad Request" response
    Given operation "ResetAiGatewayBudgetInstanceSpend" enabled
    And new "ResetAiGatewayBudgetInstanceSpend" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Credit approved after incorrect usage attribution"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Reset a budget instance's spend returns "Not Found" response
    Given operation "ResetAiGatewayBudgetInstanceSpend" enabled
    And new "ResetAiGatewayBudgetInstanceSpend" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Credit approved after incorrect usage attribution"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Reset a budget instance's spend returns "OK" response
    Given operation "ResetAiGatewayBudgetInstanceSpend" enabled
    And new "ResetAiGatewayBudgetInstanceSpend" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"instance_key": "v1|7:user_id=36:22222222-2222-2222-2222-222222222222", "reason": "Credit approved after incorrect usage attribution"}, "type": "budget-instances"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Set a model pricing override returns "Bad Request" response
    Given operation "UpdateAiGatewayModelPricing" enabled
    And new "UpdateAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"pricing_config": {"rates": {"cache_read_cost_per_mtok": 0.0, "cache_write_cost_per_mtok": 0.0, "non_cached_input_cost_per_mtok": 0.0, "output_cost_per_mtok": 0.0}, "source": {"type": "custom"}, "version": 1}}, "id": "gpt-4o", "type": "model-pricing"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Set a model pricing override returns "Not Found" response
    Given operation "UpdateAiGatewayModelPricing" enabled
    And new "UpdateAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"pricing_config": {"rates": {"cache_read_cost_per_mtok": 0.0, "cache_write_cost_per_mtok": 0.0, "non_cached_input_cost_per_mtok": 0.0, "output_cost_per_mtok": 0.0}, "source": {"type": "custom"}, "version": 1}}, "id": "gpt-4o", "type": "model-pricing"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Set a model pricing override returns "OK" response
    Given operation "UpdateAiGatewayModelPricing" enabled
    And new "UpdateAiGatewayModelPricing" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"pricing_config": {"rates": {"cache_read_cost_per_mtok": 0.0, "cache_write_cost_per_mtok": 0.0, "non_cached_input_cost_per_mtok": 0.0, "output_cost_per_mtok": 0.0}, "source": {"type": "custom"}, "version": 1}}, "id": "gpt-4o", "type": "model-pricing"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update a model for an AI Gateway provider returns "Bad Request" response
    Given operation "UpdateAiGatewayModel" enabled
    And new "UpdateAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "id": "101", "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update a model for an AI Gateway provider returns "Not Found" response
    Given operation "UpdateAiGatewayModel" enabled
    And new "UpdateAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "id": "101", "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update a model for an AI Gateway provider returns "OK" response
    Given operation "UpdateAiGatewayModel" enabled
    And new "UpdateAiGatewayModel" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    And request contains "canonical" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"model_id_wire": "gpt-5.2-codex-20260801", "supported_operations": ["OPENAI_CHAT_COMPLETIONS"]}, "id": "101", "type": "model-catalog-entries"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway budget returns "Bad Request" response
    Given operation "UpdateAiGatewayBudget" enabled
    And new "UpdateAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"apply_to_current_period": false, "capacity_microcents": 120000000, "enabled": true, "enforcement": "BLOCK", "name": "Coding agents", "reason": "Temporary capacity increase approved for an incident", "track_existing": false, "warning_threshold": 0.8}, "id": "11111111-1111-1111-1111-111111111111", "type": "budgets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway budget returns "Not Found" response
    Given operation "UpdateAiGatewayBudget" enabled
    And new "UpdateAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"apply_to_current_period": false, "capacity_microcents": 120000000, "enabled": true, "enforcement": "BLOCK", "name": "Coding agents", "reason": "Temporary capacity increase approved for an incident", "track_existing": false, "warning_threshold": 0.8}, "id": "11111111-1111-1111-1111-111111111111", "type": "budgets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway budget returns "OK" response
    Given operation "UpdateAiGatewayBudget" enabled
    And new "UpdateAiGatewayBudget" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"apply_to_current_period": false, "capacity_microcents": 120000000, "enabled": true, "enforcement": "BLOCK", "name": "Coding agents", "reason": "Temporary capacity increase approved for an incident", "track_existing": false, "warning_threshold": 0.8}, "id": "11111111-1111-1111-1111-111111111111", "type": "budgets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway model group returns "Bad Request" response
    Given operation "UpdateAiGatewayModelGroup" enabled
    And new "UpdateAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "id": "7", "type": "model-groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway model group returns "Conflict" response
    Given operation "UpdateAiGatewayModelGroup" enabled
    And new "UpdateAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "id": "7", "type": "model-groups"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway model group returns "Not Found" response
    Given operation "UpdateAiGatewayModelGroup" enabled
    And new "UpdateAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "id": "7", "type": "model-groups"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway model group returns "OK" response
    Given operation "UpdateAiGatewayModelGroup" enabled
    And new "UpdateAiGatewayModelGroup" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"allow_fast_mode": true, "max_reasoning_level": "high", "model_ids": [101], "name": "Coding models", "provider_ids": [], "routing_rule_slugs": ["coding-route"]}, "id": "7", "type": "model-groups"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway provider returns "Bad Request" response
    Given operation "UpdateAiGatewayProvider" enabled
    And new "UpdateAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "name": "production-us-v2"}, "id": "42", "type": "providers"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway provider returns "Conflict" response
    Given operation "UpdateAiGatewayProvider" enabled
    And new "UpdateAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "name": "production-us-v2"}, "id": "42", "type": "providers"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway provider returns "Not Found" response
    Given operation "UpdateAiGatewayProvider" enabled
    And new "UpdateAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "name": "production-us-v2"}, "id": "42", "type": "providers"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway provider returns "OK" response
    Given operation "UpdateAiGatewayProvider" enabled
    And new "UpdateAiGatewayProvider" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_multiplier": 1.0, "name": "production-us-v2"}, "id": "42", "type": "providers"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway rate limit returns "Bad Request" response
    Given operation "UpdateAiGatewayRateLimit" enabled
    And new "UpdateAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": null, "input_tokens_per_minute": null, "mode": "ALERT", "output_tokens_per_minute": null, "requests_per_minute": null, "tags": null, "team_id": null, "user_id": null}, "id": "11111111-1111-1111-1111-111111111111", "type": "rate-limits"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway rate limit returns "Conflict" response
    Given operation "UpdateAiGatewayRateLimit" enabled
    And new "UpdateAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": null, "input_tokens_per_minute": null, "mode": "ALERT", "output_tokens_per_minute": null, "requests_per_minute": null, "tags": null, "team_id": null, "user_id": null}, "id": "11111111-1111-1111-1111-111111111111", "type": "rate-limits"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway rate limit returns "Not Found" response
    Given operation "UpdateAiGatewayRateLimit" enabled
    And new "UpdateAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": null, "input_tokens_per_minute": null, "mode": "ALERT", "output_tokens_per_minute": null, "requests_per_minute": null, "tags": null, "team_id": null, "user_id": null}, "id": "11111111-1111-1111-1111-111111111111", "type": "rate-limits"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway rate limit returns "OK" response
    Given operation "UpdateAiGatewayRateLimit" enabled
    And new "UpdateAiGatewayRateLimit" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cost_microcents_per_minute": null, "input_tokens_per_minute": null, "mode": "ALERT", "output_tokens_per_minute": null, "requests_per_minute": null, "tags": null, "team_id": null, "user_id": null}, "id": "11111111-1111-1111-1111-111111111111", "type": "rate-limits"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway routing rule returns "Bad Request" response
    Given operation "UpdateAiGatewayRoutingRule" enabled
    And new "UpdateAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"expected_updated_at": "2026-08-24T12:00:00Z", "removed_target_ids": [901], "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "id": "coding", "type": "routing-rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway routing rule returns "Conflict" response
    Given operation "UpdateAiGatewayRoutingRule" enabled
    And new "UpdateAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"expected_updated_at": "2026-08-24T12:00:00Z", "removed_target_ids": [901], "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "id": "coding", "type": "routing-rules"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway routing rule returns "Not Found" response
    Given operation "UpdateAiGatewayRoutingRule" enabled
    And new "UpdateAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"expected_updated_at": "2026-08-24T12:00:00Z", "removed_target_ids": [901], "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "id": "coding", "type": "routing-rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/frontier-prd-gateway
  Scenario: Update an AI Gateway routing rule returns "OK" response
    Given operation "UpdateAiGatewayRoutingRule" enabled
    And new "UpdateAiGatewayRoutingRule" request
    And request contains "slug" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"expected_updated_at": "2026-08-24T12:00:00Z", "removed_target_ids": [901], "tiers": [{"classifier": {"confidence_threshold": 0.5, "context": "Requests come from engineers.", "model": "gpt-6-luna", "provider": "openai"}, "ordering": "configured", "targets": [{"default": false, "id": 901, "model": "gpt-5.2-codex", "model_id": 101, "provider": "prod-us", "reasoning_level": "medium", "rubric": "Short factual questions.", "slug": "coding-fallback", "type": "model", "weight": 70}]}]}, "id": "coding", "type": "routing-rules"}}
    When the request is sent
    Then the response status is 200 OK
