@endpoint(feature-flags) @endpoint(feature-flags-v2)
Feature: Feature Flags
  Manage feature flags and environments.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "FeatureFlags" API

  @skip @team:DataDog/feature-flags
  Scenario: Archive a feature flag returns "Bad Request" response
    Given new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Archive a feature flag returns "Not Found" response
    Given new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/feature-flags
  Scenario: Archive a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "ArchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: Create a feature flag returns "Bad Request" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "control", "description": "This is an example feature flag for demonstration", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "key": "example-feature-flag", "name": "Example Feature Flag", "value_type": "BOOLEAN", "variants": [{"key": "control", "name": "Control Variant", "value": "true"}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Create a feature flag returns "Conflict" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "control", "description": "This is an example feature flag for demonstration", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "key": "example-feature-flag", "name": "Example Feature Flag", "value_type": "BOOLEAN", "variants": [{"key": "control", "name": "Control Variant", "value": "true"}]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/feature-flags
  Scenario: Create a feature flag returns "Created" response
    Given new "CreateFeatureFlag" request
    And body with value {"data": {"type": "feature-flags", "attributes": {"default_variant_key": "variant-{{ unique }}-1", "description": "Test feature flag for BDD scenarios", "key": "test-feature-flag-{{ unique }}", "name": "Test Feature Flag {{ unique }}", "value_type": "BOOLEAN", "variants": [{"key": "variant-{{ unique }}-1", "name": "Variant {{ unique }} A", "value": "true"}, {"key": "variant-{{ unique }}-2", "name": "Variant {{ unique }} B", "value": "false"}]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.key" is equal to "test-feature-flag-{{ unique }}"
    And the response "data.attributes.name" is equal to "Test Feature Flag {{ unique }}"
    And the response "data.attributes.value_type" is equal to "BOOLEAN"

  @skip @team:DataDog/feature-flags
  Scenario: Create an environment returns "Bad Request" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"description": "Staging environment for testing", "key": "staging", "name": "staging"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Create an environment returns "Conflict" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"description": "Staging environment for testing", "key": "staging", "name": "staging"}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/feature-flags
  Scenario: Create an environment returns "Created" response
    Given new "CreateFeatureFlagsEnvironment" request
    And body with value {"data": {"type": "environments", "attributes": {"name": "Test Environment {{ unique }}", "queries": ["test-{{ unique }}", "env-{{ unique }}"]}}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:DataDog/feature-flags
  Scenario: Delete an environment returns "No Content" response
    Given there is a valid "environment" in the system
    And new "DeleteFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:DataDog/feature-flags
  Scenario: Delete an environment returns "Not Found" response
    Given new "DeleteFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Disable a feature flag in an environment returns "Accepted - Approval required for this change" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @skip @team:DataDog/feature-flags
  Scenario: Disable a feature flag in an environment returns "Not Found" response
    Given new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Disable a feature flag in an environment returns "OK" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "DisableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: Enable a feature flag in an environment returns "Accepted - Approval required for this change" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 202 Accepted - Approval required for this change

  @skip @team:DataDog/feature-flags
  Scenario: Enable a feature flag in an environment returns "Not Found" response
    Given new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Enable a feature flag in an environment returns "OK" response
    Given there is a valid "feature_flag" in the system
    And there is a valid "environment" in the system
    And new "EnableFeatureFlagEnvironment" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: Get a feature flag returns "Not Found" response
    Given new "GetFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/feature-flags
  Scenario: Get a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "GetFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.key" has the same value as "feature_flag.data.attributes.key"
    And the response "data.attributes.name" has the same value as "feature_flag.data.attributes.name"
    And the response "data.attributes.value_type" has the same value as "feature_flag.data.attributes.value_type"

  @skip @team:DataDog/feature-flags
  Scenario: Get an environment returns "Not Found" response
    Given new "GetFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Get an environment returns "OK" response
    Given there is a valid "environment" in the system
    And new "GetFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: List environments returns "OK" response
    Given new "ListFeatureFlagsEnvironments" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/feature-flags
  Scenario: List feature flags returns "OK" response
    Given new "ListFeatureFlags" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: Unarchive a feature flag returns "Bad Request" response
    Given new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Unarchive a feature flag returns "Not Found" response
    Given new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Unarchive a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "UnarchiveFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/feature-flags
  Scenario: Update a feature flag returns "Bad Request" response
    Given new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "name": "Updated Feature Flag Name"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Update a feature flag returns "Not Found" response
    Given new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "json_schema": "{\"type\": \"object\", \"properties\": {\"enabled\": {\"type\": \"boolean\"}}}", "name": "Updated Feature Flag Name"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/feature-flags
  Scenario: Update a feature flag returns "OK" response
    Given there is a valid "feature_flag" in the system
    And new "UpdateFeatureFlag" request
    And request contains "feature_flag_id" parameter from "feature_flag.data.id"
    And body with value {"data": {"type": "feature-flags", "attributes": {"description": "Updated description for the feature flag", "name": "Updated Test Feature Flag {{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "Updated Test Feature Flag {{ unique }}"
    And the response "data.attributes.description" is equal to "Updated description for the feature flag"

  @skip @team:DataDog/feature-flags
  Scenario: Update an environment returns "Bad Request" response
    Given new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "environments", "attributes": {"description": "Updated staging environment description", "name": "Updated Staging"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/feature-flags
  Scenario: Update an environment returns "Not Found" response
    Given new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "environments", "attributes": {"description": "Updated staging environment description", "name": "Updated Staging"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/feature-flags
  Scenario: Update an environment returns "OK" response
    Given there is a valid "environment" in the system
    And new "UpdateFeatureFlagsEnvironment" request
    And request contains "environment_id" parameter from "environment.data.id"
    And body with value {"data": {"type": "environments", "attributes": {"name": "Updated Test Environment {{ unique }}", "queries": ["updated-{{ unique }}", "live-{{ unique }}"]}}}
    When the request is sent
    Then the response status is 200 OK
