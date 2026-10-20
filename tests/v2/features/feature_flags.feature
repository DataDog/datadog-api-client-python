@endpoint(feature-flags) @endpoint(feature-flags-v2)
Feature: Feature Flags
  Manage feature flags and environments.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "FeatureFlags" API

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Add a variant to a feature flag returns "Bad Request" response
    Given new "CreateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And body with value {"key": "variant-abc123", "name": "Variant ABC123", "value": "true"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Add a variant to a feature flag returns "Conflict - A variant with this key already exists on the flag." response
    Given new "CreateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And body with value {"key": "variant-abc123", "name": "Variant ABC123", "value": "true"}
    When the request is sent
    Then the response status is 409 Conflict - A variant with this key already exists on the flag.

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Add a variant to a feature flag returns "Created" response
    Given new "CreateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And body with value {"key": "variant-abc123", "name": "Variant ABC123", "value": "true"}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Add a variant to a feature flag returns "Not Found" response
    Given new "CreateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And body with value {"key": "variant-abc123", "name": "Variant ABC123", "value": "true"}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Archive a feature flag returns "Bad Request" response
    Given new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Archive a feature flag returns "Not Found" response
    Given new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/feature-flags
  Scenario: Archive a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Create a feature flag returns "Bad Request" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "control", "description": "This is an example feature flag for demonstration", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "key": "example-feature-flag", "name": "Example Feature Flag", "value_type": "BOOLEAN", "variants": [{"key": "control", "name": "Control Variant", "value": "true"}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Create a feature flag returns "Conflict" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "control", "description": "This is an example feature flag for demonstration", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "key": "example-feature-flag", "name": "Example Feature Flag", "value_type": "BOOLEAN", "variants": [{"key": "control", "name": "Control Variant", "value": "true"}]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/feature-flags
  Scenario: Create a feature flag returns "Created" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "variant-{{ unique }}-1", "distribution_channel": "SERVER", "key": "test-feature-flag-{{ unique }}", "name": "Test Feature Flag {{ unique }}", "require_approval": false, "staleness_status": "PERMANENT", "tags": ["env:api-client-test"], "value_type": "BOOLEAN", "variants": [{"key": "variant-{{ unique }}-1", "name": "Variant {{ unique }} A", "value": "true"}, {"key": "variant-{{ unique }}-2", "name": "Variant {{ unique }} B", "value": "false"}]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.distribution_channel" is equal to "SERVER"
    And the response "data.attributes.key" is equal to "test-feature-flag-{{ unique }}"
    And the response "data.attributes.name" is equal to "Test Feature Flag {{ unique }}"
    And the response "data.attributes.require_approval" is equal to false
    And the response "data.attributes.staleness_status_override" is equal to "PERMANENT"
    And the response "data.attributes.tags" is equal to ["env:api-client-test"]
    And the response "data.attributes.value_type" is equal to "BOOLEAN"

  @team:ddoghq/feature-flags
  Scenario: Create allocation for a flag in an environment returns "Created" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    And body with value {"data":{"type":"allocations","attributes":{"name":"New targeting rule {{ unique }}","key":"new-targeting-rule-{{ unique_lower }}","targeting_rules":[],"variant_weights":[{"variant_id":"{{ feature_flag.data.attributes.variants[0].id }}","value":100}],"guardrail_metrics":[],"type":"CANARY"}}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:ddoghq/feature-flags
  Scenario: Create an environment returns "Bad Request" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"description": "Staging environment for testing", "key": "staging", "name": "staging"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Create an environment returns "Conflict" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"description": "Staging environment for testing", "key": "staging", "name": "staging"}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/feature-flags
  Scenario: Create an environment returns "Created" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"name": "Test Environment {{ unique }}", "queries": ["test-{{ unique }}", "env-{{ unique }}"]}}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Create targeting rules for a flag env returns "Accepted - Approval required for this change" response
    Given new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}}
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Create targeting rules for a flag env returns "Bad Request" response
    Given new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Create targeting rules for a flag env returns "Conflict" response
    Given new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Create targeting rules for a flag env returns "Created" response
    Given new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Create targeting rules for a flag env returns "Not Found" response
    Given new "CreateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Delete a variant returns "Bad Request" response
    Given new "DeleteVariantFromFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Delete a variant returns "Conflict - A pending suggestion already exists for this property." response
    Given new "DeleteVariantFromFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict - A pending suggestion already exists for this property.

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Delete a variant returns "No Content" response
    Given new "DeleteVariantFromFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Delete a variant returns "Not Found" response
    Given new "DeleteVariantFromFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Delete an environment returns "No Content" response
    Given there is a valid "environment" in the system
    And new "DeleteFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:ddoghq/feature-flags
  Scenario: Delete an environment returns "Not Found" response
    Given new "DeleteFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Disable a feature flag in an environment returns "Accepted - Approval required for this change" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @skip @team:ddoghq/feature-flags
  Scenario: Disable a feature flag in an environment returns "Not Found" response
    Given new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Disable a feature flag in an environment returns "OK" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Enable a feature flag in an environment returns "Accepted - Approval required for this change" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @skip @team:ddoghq/feature-flags
  Scenario: Enable a feature flag in an environment returns "Not Found" response
    Given new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Enable a feature flag in an environment returns "OK" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Get a feature flag returns "Not Found" response
    Given new "GetFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/feature-flags
  Scenario: Get a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "GetFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.key" has the same value as "feature_flag.data.attributes.key"
    And the response "data.attributes.name" has the same value as "feature_flag.data.attributes.name"
    And the response "data.attributes.value_type" has the same value as "feature_flag.data.attributes.value_type"

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Get a saved filter returns "Bad Request" response
    Given new "GetSavedFilter" request
    And request contains "saved_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/feature-flags
  Scenario: Get a saved filter returns "Not Found" response
    Given new "GetSavedFilter" request
    And request contains "saved_filter_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:ddoghq/feature-flags
  Scenario: Get a saved filter returns "OK" response
    Given new "GetSavedFilter" request
    And request contains "saved_filter_id" parameter with value "8c051ac8-df7a-496e-b5c0-de691a411100"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "8c051ac8-df7a-496e-b5c0-de691a411100"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.name" is equal to "getSavedFilterTest-Rule"
    And the response "data.attributes.description" is equal to "Synthetic fixture for OpenAPI tests"
    And the response "data.attributes.targeting_rules" has length 2
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "email"
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test@example.com"]
    And the response "data.attributes.targeting_rules[1].conditions" has length 1
    And the response "data.attributes.targeting_rules[1].conditions[0].attribute" is equal to "org_id"
    And the response "data.attributes.targeting_rules[1].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[1].conditions[0].value" is equal to ["test-org-1"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Get a saved filter returns a saved list
    Given new "GetSavedFilter" request
    And request contains "saved_filter_id" parameter with value "fb44ff15-fe17-4bab-afe8-9a8eb0cf586c"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "fb44ff15-fe17-4bab-afe8-9a8eb0cf586c"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.creation_type" is equal to "LIST"
    And the response "data.attributes.name" is equal to "getSavedFilterTest-list"
    And the response "data.attributes.description" is equal to "Synthetic fixture for OpenAPI tests"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-1", "test-user-2"]

  @skip @team:ddoghq/feature-flags
  Scenario: Get an environment returns "Not Found" response
    Given new "GetFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Get an environment returns "OK" response
    Given there is a valid "environment" in the system
    And new "GetFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: List environments returns "OK" response
    Given new "ListFeatureFlagsEnvironments" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/feature-flags
  Scenario: List feature flags applies default pagination
    Given new "ListFeatureFlags" request
    And request contains "key" parameter with value "missing-{{ unique_lower }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta.page.total" is equal to 0
    And the response "meta.page.limit" is equal to 25
    And the response "meta.page.offset" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags combines exact keys tags search types creators and IDs
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "key" parameter with value "list-a-{{ unique_lower }}"
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}", "color:blue"]
    And request contains "search" parameter with value "LIST-A-{{ unique_lower }}"
    And request contains "value_type" parameter with value ["BOOLEAN", "STRING"]
    And request contains "created_by" parameter with value ["{{ feature_flag_list_a.data.attributes.created_by }}"]
    And request contains "flag_ids" parameter with value ["{{ feature_flag_list_a.data.id }}", "{{ feature_flag_list_b.data.id }}"]
    And request contains "is_archived" parameter with value false
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "meta.page.total" is equal to 1
    And the response "data[0].id" has the same value as "feature_flag_list_a.data.id"

  @team:ddoghq/feature-flags
  Scenario: List feature flags combines teams with legacy team tags
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}", "team:api-client-test-b"]
    And request contains "teams" parameter with value ["api-client-test-a", "api-client-test-a"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2
    And the response "meta.page.total" is equal to 2

  @team:ddoghq/feature-flags
  Scenario: List feature flags combines teams with ordinary tags
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}", "color:blue"]
    And request contains "teams" parameter with value ["api-client-test-a", "api-client-test-b"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "meta.page.total" is equal to 1

  @team:ddoghq/feature-flags
  Scenario: List feature flags does not partially match keys
    Given there is a valid "feature_flag_list_a" in the system
    And new "ListFeatureFlags" request
    And request contains "key" parameter with value "list-a-"
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta.page.total" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags excludes unknown saved filters
    Given there is a valid "feature_flag_list_a" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "saved_filter_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta.page.total" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags excludes unknown teams
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "teams" parameter with value ["missing-{{ unique_lower }}"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta.page.total" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags filters SDK availability for ALL
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And there is a valid "feature_flag_list_c" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "distribution_channel" parameter with value "ALL"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 3
    And the response "meta.page.total" is equal to 3

  @team:ddoghq/feature-flags
  Scenario: List feature flags filters SDK availability for CLIENT
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And there is a valid "feature_flag_list_c" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "distribution_channel" parameter with value "CLIENT"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2
    And the response "meta.page.total" is equal to 2

  @team:ddoghq/feature-flags
  Scenario: List feature flags filters SDK availability for SERVER
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And there is a valid "feature_flag_list_c" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "distribution_channel" parameter with value "SERVER"
    And request contains "sort" parameter with value "name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2
    And the response "meta.page.total" is equal to 2
    And the response "data[0].attributes.key" is equal to "list-b-{{ unique_lower }}"

  @team:ddoghq/feature-flags
  Scenario: List feature flags filters disabled production status
    Given there is a valid "production_environment" in the system
    And there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "flag_ids" parameter with value ["{{ feature_flag_list_a.data.id }}", "{{ feature_flag_list_b.data.id }}"]
    And request contains "production_status" parameter with value ["DISABLED"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2
    And the response "meta.page.total" is equal to 2

  @team:ddoghq/feature-flags
  Scenario: List feature flags filters permanent staleness using computed details
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "staleness_status" parameter with value "PERMANENT"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "meta.page.total" is equal to 1
    And the response "data[0].attributes.staleness_details.staleness_status" is equal to "PERMANENT"
    And the response "data[0].attributes.staleness_status" is equal to "ACTIVE"

  @team:ddoghq/feature-flags
  Scenario: List feature flags gives page parameters precedence over aliases
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "limit" parameter with value 2
    And request contains "offset" parameter with value 1
    And request contains "page[limit]" parameter with value 1
    And request contains "page[offset]" parameter with value 0
    And request contains "sort" parameter with value "name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.key" is equal to "list-a-{{ unique_lower }}"
    And the response "meta.page.limit" is equal to 1
    And the response "meta.page.offset" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags matches any selected team
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "teams" parameter with value ["api-client-test-a", "api-client-test-b"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2
    And the response "meta.page.total" is equal to 2

  @team:ddoghq/feature-flags
  Scenario: List feature flags rejects empty team handles
    Given new "ListFeatureFlags" request
    And request contains "teams" parameter with value [""]
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/feature-flags
  Scenario: List feature flags rejects unknown sort fields
    Given new "ListFeatureFlags" request
    And request contains "sort" parameter with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/feature-flags
  Scenario: List feature flags requires every ordinary tag
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}", "color:blue", "color:red"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta.page.total" is equal to 0

  @team:ddoghq/feature-flags
  Scenario: List feature flags returns "Bad Request" response
    Given new "ListFeatureFlags" request
    And request contains "teams" parameter with value ["team:checkout"]
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/feature-flags
  Scenario: List feature flags returns "OK" response
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "page[limit]" parameter with value 1
    And request contains "page[offset]" parameter with value 0
    And request contains "sort" parameter with value "name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.key" is equal to "list-a-{{ unique_lower }}"
    And the response "meta.page.type" is equal to "offset_limit"
    And the response "meta.page.limit" is equal to 1
    And the response "meta.page.offset" is equal to 0
    And the response "meta.page.total" is equal to 2
    And the response "meta.page.next_offset" is equal to 1
    And the response "links" has field "next"

  @team:ddoghq/feature-flags
  Scenario: List feature flags returns the second filtered page
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "page[limit]" parameter with value 1
    And request contains "page[offset]" parameter with value 1
    And request contains "sort" parameter with value "name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.key" is equal to "list-b-{{ unique_lower }}"
    And the response "meta.page.offset" is equal to 1
    And the response "meta.page.total" is equal to 2
    And the response "meta.page.next_offset" is equal to null
    And the response "links" has field "prev"

  @team:ddoghq/feature-flags
  Scenario: List feature flags supports legacy pagination aliases
    Given there is a valid "feature_flag_list_a" in the system
    And there is a valid "feature_flag_list_b" in the system
    And new "ListFeatureFlags" request
    And request contains "tags" parameter with value ["list-test:{{ unique_lower }}"]
    And request contains "limit" parameter with value 1
    And request contains "offset" parameter with value 1
    And request contains "sort" parameter with value "name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.key" is equal to "list-b-{{ unique_lower }}"
    And the response "meta.page.limit" is equal to 1
    And the response "meta.page.offset" is equal to 1
    And the response "meta.page.total" is equal to 2

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter accepts the current timestamp for metadata
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And body with value {"data":{"attributes":{"description":"Metadata with current timestamp.","last_updated_at":"2026-10-16T20:20:29Z"},"type":"saved-filters"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-concurrency-437ebfe7"
    And the response "data.attributes.description" is equal to "Metadata with current timestamp."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-1"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter accepts the current timestamp for rules
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And body with value {"data":{"attributes":{"last_updated_at":"2026-10-16T20:20:30Z","targeting_rules":[{"conditions":[{"attribute":"user_id","operator":"ONE_OF","value":["test-user-2"]}]}]},"type":"saved-filters"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-concurrency-437ebfe7"
    And the response "data.attributes.description" is equal to "Metadata with current timestamp."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-2"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter clears the description with an empty string
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":""}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-null-157e7ff3"
    And the response "data.attributes.description" is equal to ""
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "org_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-org-1"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter preserves a null description
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":null,"name":"patchSavedFilterTest-null-157e7ff3"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-null-157e7ff3"
    And the response "data.attributes.description" is equal to "Combined synthetic test update."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "org_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-org-1"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects a duplicate name
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"name":"patchSavedFilterTest-LIST-157e7ff3"}}}
    When the request is sent
    Then the response status is 409 Conflict
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "409"
    And the response "errors[0].title" is equal to "Conflict"
    And the response "errors[0].detail" is equal to "a saved filter with this name already exists: conflict occurred"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects a null-only update
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":null}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "at least one field must be provided"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects a timestamp-only update
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And body with value {"data":{"attributes":{"last_updated_at":"2026-10-16T20:20:30Z"},"type":"saved-filters"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "at least one field must be provided"

  @replay-only @skip-python @skip-ruby @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects an empty name
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"name":""}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "name must not be empty"

  @replay-only @skip-java @skip-python @skip-ruby @skip-typescript @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects an invalid timestamp
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":"Not applied.","last_updated_at":"invalid"}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "last_updated_at must be a valid RFC3339 timestamp"

  @replay-only @skip-python @skip-ruby @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects empty targeting rules
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"targeting_rules":[]}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "attribute \"targeting_rules\" failed min validation"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects nested saved filters
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"targeting_rules":[{"conditions":[{"operator":"ONE_OF","attribute":"user_id","value":["test-user-1"],"saved_filter_id":"d8e3a81b-1505-4600-99c6-c563d01d46b1"}]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "targeting rule 0 condition 0: saved filters cannot reference other saved filters"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter rejects stale rule updates
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"
    And body with value {"data":{"attributes":{"last_updated_at":"2020-01-01T00:00:00Z","targeting_rules":[{"conditions":[{"attribute":"user_id","operator":"ONE_OF","value":["not-applied"]}]}]},"type":"saved-filters"}}
    When the request is sent
    Then the response status is 409 Conflict
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "409"
    And the response "errors[0].title" is equal to "Conflict"
    And the response "errors[0].detail" is equal to "saved filter has been modified since you last fetched it; please refresh and retry: conflict occurred"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter replaces rules and preserves metadata
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"targeting_rules":[{"conditions":[{"operator":"ONE_OF","attribute":"email","value":["test@example.com"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-renamed-157e7ff3"
    And the response "data.attributes.description" is equal to "Original synthetic test description."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "email"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test@example.com"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter replaces the rules of a saved list
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "d8e3a81b-1505-4600-99c6-c563d01d46b1"
    And body with value {"data":{"type":"saved-filters","attributes":{"targeting_rules":[{"conditions":[{"operator":"ONE_OF","attribute":"user_id","value":["test-user-3"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "d8e3a81b-1505-4600-99c6-c563d01d46b1"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-LIST-157e7ff3"
    And the response "data.attributes.description" is equal to "Updated synthetic test description."
    And the response "data.attributes.creation_type" is equal to "LIST"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-3"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter returns "Bad Request" response
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "400"
    And the response "errors[0].title" is equal to "Bad Request"
    And the response "errors[0].detail" is equal to "at least one field must be provided"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter returns "Conflict" response
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":"Not applied.","last_updated_at":"2020-01-01T00:00:00Z"}}}
    When the request is sent
    Then the response status is 409 Conflict
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "409"
    And the response "errors[0].title" is equal to "Conflict"
    And the response "errors[0].detail" is equal to "saved filter has been modified since you last fetched it; please refresh and retry: conflict occurred"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter returns "Not Found" response
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":"Not applied."}}}
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].status" is equal to "404"
    And the response "errors[0].title" is equal to "Not Found"
    And the response "errors[0].detail" is equal to "saved filter not found or already deleted: record not found"

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter returns "OK" response
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"name":"patchSavedFilterTest-renamed-157e7ff3"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-renamed-157e7ff3"
    And the response "data.attributes.description" is equal to "Original synthetic test description."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-1","test-user-2"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter updates metadata and rules together
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And body with value {"data":{"type":"saved-filters","attributes":{"name":"patchSavedFilterTest-combined-157e7ff3","description":"Combined synthetic test update.","targeting_rules":[{"conditions":[{"operator":"ONE_OF","attribute":"org_id","value":["test-org-1"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-combined-157e7ff3"
    And the response "data.attributes.description" is equal to "Combined synthetic test update."
    And the response "data.attributes.creation_type" is equal to "RULES"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "org_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-org-1"]

  @replay-only @team:ddoghq/feature-flags
  Scenario: Patch a saved filter updates only the description of a saved list
    Given new "UpdateSavedFilterAttributes" request
    And request contains "saved_filter_id" parameter with value "d8e3a81b-1505-4600-99c6-c563d01d46b1"
    And body with value {"data":{"type":"saved-filters","attributes":{"description":"Updated synthetic test description."}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "d8e3a81b-1505-4600-99c6-c563d01d46b1"
    And the response "data.type" is equal to "saved-filters"
    And the response "data.attributes.name" is equal to "patchSavedFilterTest-LIST-157e7ff3"
    And the response "data.attributes.description" is equal to "Updated synthetic test description."
    And the response "data.attributes.creation_type" is equal to "LIST"
    And the response "data.attributes.targeting_rules" has length 1
    And the response "data.attributes.targeting_rules[0].conditions" has length 1
    And the response "data.attributes.targeting_rules[0].conditions[0].operator" is equal to "ONE_OF"
    And the response "data.attributes.targeting_rules[0].conditions[0].attribute" is equal to "user_id"
    And the response "data.attributes.targeting_rules[0].conditions[0].value" is equal to ["test-user-1","test-user-2"]

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Pause a progressive rollout returns "Bad Request" response
    Given new "PauseExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Pause a progressive rollout returns "Conflict" response
    Given new "PauseExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Pause a progressive rollout returns "Not Found" response
    Given new "PauseExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Pause a progressive rollout returns "OK" response
    Given new "PauseExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Resume a progressive rollout returns "Bad Request" response
    Given new "ResumeExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Resume a progressive rollout returns "Conflict" response
    Given new "ResumeExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Resume a progressive rollout returns "Not Found" response
    Given new "ResumeExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Resume a progressive rollout returns "OK" response
    Given new "ResumeExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Start a progressive rollout returns "Bad Request" response
    Given new "StartExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Start a progressive rollout returns "Conflict" response
    Given new "StartExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Start a progressive rollout returns "Not Found" response
    Given new "StartExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Start a progressive rollout returns "OK" response
    Given new "StartExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Stop a progressive rollout returns "Bad Request" response
    Given new "StopExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Stop a progressive rollout returns "Conflict" response
    Given new "StopExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Stop a progressive rollout returns "Not Found" response
    Given new "StopExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Stop a progressive rollout returns "OK" response
    Given new "StopExposureSchedule" request
    And request contains "exposure_schedule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Unarchive a feature flag returns "Bad Request" response
    Given new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Unarchive a feature flag returns "Not Found" response
    Given new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Unarchive a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Update a feature flag returns "Bad Request" response
    Given new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "name": "Updated Feature Flag Name"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Update a feature flag returns "Not Found" response
    Given new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "name": "Updated Feature Flag Name"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/feature-flags
  Scenario: Update a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "name": "Updated Test Feature Flag {{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "Updated Test Feature Flag {{ unique }}"
    And the response "data.attributes.description" is equal to "Updated description for the feature flag"

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update a variant returns "Bad Request" response
    Given new "UpdateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"name": "Variant ABC123 Updated", "value": "new_value"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update a variant returns "Conflict - A pending suggestion already exists for this property." response
    Given new "UpdateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"name": "Variant ABC123 Updated", "value": "new_value"}
    When the request is sent
    Then the response status is 409 Conflict - A pending suggestion already exists for this property.

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update a variant returns "Not Found" response
    Given new "UpdateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"name": "Variant ABC123 Updated", "value": "new_value"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update a variant returns "OK" response
    Given new "UpdateVariantForFeatureFlag" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"name": "Variant ABC123 Updated", "value": "new_value"}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/feature-flags
  Scenario: Update an environment returns "Bad Request" response
    Given new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "environments", "attributes": {"description": "Updated staging environment description", "name": "Updated Staging"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/feature-flags
  Scenario: Update an environment returns "Not Found" response
    Given new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "environments", "attributes": {"description": "Updated staging environment description", "name": "Updated Staging"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/feature-flags
  Scenario: Update an environment returns "OK" response
    Given there is a valid "environment" in the system
    And new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    And body with value {"data": {"type": "environments", "attributes": {"name": "Updated Test Environment {{ unique }}", "queries": ["updated-{{ unique }}", "live-{{ unique }}"]}}}
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag in an environment returns "OK" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    And body with value {"data":[{"type":"allocations","attributes":{"key":"overwrite-allocation-{{ unique_lower }}","name":"New targeting rule {{ unique }}","targeting_rules":[],"variant_weights":[{"variant_id":"{{ feature_flag.data.attributes.variants[0].id }}","value":100}],"exposure_schedule":{"rollout_options":{"strategy":"UNIFORM_INTERVALS","autostart":false,"selection_interval_ms":86400000},"rollout_steps":[{"exposure_ratio":0.05,"interval_ms":null,"is_pause_record":false,"grouped_step_index":0},{"exposure_ratio":0.25,"interval_ms":null,"is_pause_record":false,"grouped_step_index":1},{"exposure_ratio":1,"interval_ms":null,"is_pause_record":false,"grouped_step_index":2}]},"guardrail_metrics":[],"type":"CANARY"}}]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag returns "Accepted - Approval required for this change" response
    Given new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}]}
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag returns "Bad Request" response
    Given new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag returns "Conflict" response
    Given new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}]}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag returns "Not Found" response
    Given new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/feature-flags
  Scenario: Update targeting rules for a flag returns "OK" response
    Given new "UpdateAllocationsForFeatureFlagInEnvironment" request
    And request contains "feature_flag_id" parameter from "REPLACE.ME"
    And request contains "environment_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"experiment_id": "550e8400-e29b-41d4-a716-446655440030", "exposure_schedule": {"absolute_start_time": "2025-06-13T12:00:00Z", "control_variant_id": "550e8400-e29b-41d4-a716-446655440012", "control_variant_key": "control", "id": "550e8400-e29b-41d4-a716-446655440010", "rollout_options": {"autostart": false, "selection_interval_ms": 3600000, "strategy": "UNIFORM_INTERVALS"}, "rollout_steps": [{"exposure_ratio": 0.5, "grouped_step_index": 1, "id": "550e8400-e29b-41d4-a716-446655440040", "interval_ms": 3600000, "is_pause_record": false}]}, "guardrail_metrics": [{"metric_id": "metric-error-rate", "trigger_action": "PAUSE"}], "id": "550e8400-e29b-41d4-a716-446655440020", "key": "prod-rollout", "name": "Production Rollout", "targeting_rules": [{"conditions": [{"attribute": "user_tier", "operator": "ONE_OF", "saved_filter_id": "550e8400-e29b-41d4-a716-446655440090", "value": ["premium", "enterprise"]}]}], "type": "FEATURE_GATE", "variant_weights": [{"value": 50, "variant_id": "550e8400-e29b-41d4-a716-446655440001", "variant_key": "control"}]}, "type": "allocations"}]}
    When the request is sent
    Then the response status is 200 OK
