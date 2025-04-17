@endpoint(monitors) @endpoint(monitors-v2)
Feature: Monitors
  [Monitors](https://docs.datadoghq.com/monitors) allow you to watch a
  metric or check that you care about and notifies your team when a defined
  threshold has exceeded.  For more information, see [Creating
  Monitors](https://docs.datadoghq.com/monitors/create/types/) and [Tag
  Policies](https://docs.datadoghq.com/monitors/settings/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Monitors" API

  @skip-validation @team:DataDog/monitor-app
  Scenario: Create a monitor configuration policy returns "Bad Request" response
    Given new "CreateMonitorConfigPolicy" request
    And body with value {"data": {"attributes": {"policy_type": "INVALID", "policy": {"tag_key": "datacenter", "tag_key_required": true, "valid_tag_values": ["prod", "staging"]}}, "type": "monitor-config-policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Create a monitor configuration policy returns "OK" response
    Given new "CreateMonitorConfigPolicy" request
    And body with value {"data": {"attributes": {"policy_type": "tag", "policy": {"tag_key": "{{ unique_lower_alnum }}", "tag_key_required": false, "valid_tag_values": ["prod", "staging"]}}, "type": "monitor-config-policy"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "monitor-config-policy"
    And the response "data.attributes.policy_type" is equal to "tag"
    And the response "data.attributes.policy.tag_key" is equal to "{{ unique_lower_alnum }}"
    And the response "data.attributes.policy.valid_tag_values" is equal to ["prod", "staging"]

  @team:DataDog/monitor-app
  Scenario: Delete a monitor configuration policy returns "Bad Request" response
    Given new "DeleteMonitorConfigPolicy" request
    And request contains "policy_id" parameter with value "INVALID_UUID"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Delete a monitor configuration policy returns "Not Found" response
    Given new "DeleteMonitorConfigPolicy" request
    And request contains "policy_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Delete a monitor configuration policy returns "OK" response
    Given there is a valid "monitor_configuration_policy" in the system
    And new "DeleteMonitorConfigPolicy" request
    And request contains "policy_id" parameter from "monitor_configuration_policy.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/monitor-app
  Scenario: Edit a monitor configuration policy returns "Not Found" response
    Given new "UpdateMonitorConfigPolicy" request
    And request contains "policy_id" parameter with value "00000000-0000-1234-0000-000000000000"
    And body with value {"data": {"attributes": {"policy": {"tag_key": "datacenter", "tag_key_required": false, "valid_tag_values": ["prod", "staging"]}, "policy_type": "tag"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-config-policy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Edit a monitor configuration policy returns "OK" response
    Given there is a valid "monitor_configuration_policy" in the system
    And new "UpdateMonitorConfigPolicy" request
    And request contains "policy_id" parameter from "monitor_configuration_policy.data.id"
    And body with value {"data": {"attributes": {"policy": {"tag_key": "{{ unique_lower_alnum }}", "tag_key_required": false, "valid_tag_values": ["prod", "staging"]}, "policy_type": "tag"}, "id": "{{ monitor_configuration_policy.data.id }}", "type": "monitor-config-policy"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "monitor-config-policy"
    And the response "data.id" is equal to "{{ monitor_configuration_policy.data.id }}"
    And the response "data.attributes.policy_type" is equal to "tag"
    And the response "data.attributes.policy.tag_key" is equal to "{{ unique_lower_alnum }}"
    And the response "data.attributes.policy.valid_tag_values" is equal to ["prod", "staging"]

  @team:DataDog/monitor-app
  Scenario: Edit a monitor configuration policy returns "Unprocessable Entity" response
    Given there is a valid "monitor_configuration_policy" in the system
    And new "UpdateMonitorConfigPolicy" request
    And request contains "policy_id" parameter from "monitor_configuration_policy.data.id"
    And body with value {"data": {"attributes": {"policy": {"tag_key": "{{ unique_lower_alnum }}", "tag_key_required": false, "valid_tag_values": ["prod", "staging"]}, "policy_type": "tag"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-config-policy"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/monitor-app
  Scenario: Get a monitor configuration policy returns "Not Found" response
    Given new "GetMonitorConfigPolicy" request
    And request contains "policy_id" parameter with value "12340000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Get a monitor configuration policy returns "OK" response
    Given there is a valid "monitor_configuration_policy" in the system
    And new "GetMonitorConfigPolicy" request
    And request contains "policy_id" parameter from "monitor_configuration_policy.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "monitor-config-policy"
    And the response "data.id" is equal to "{{ monitor_configuration_policy.data.id }}"
    And the response "data.attributes.policy_type" is equal to "tag"
    And the response "data.attributes.policy.tag_key" is equal to "{{ unique_lower_alnum }}"
    And the response "data.attributes.policy.valid_tag_values" is equal to ["prod", "staging"]

  @team:DataDog/monitor-app
  Scenario: Get all monitor configuration policies returns "OK" response
    Given there is a valid "monitor_configuration_policy" in the system
    And new "ListMonitorConfigPolicies" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "type" with value "monitor-config-policy"
    And the response "data" has item with field "id" with value "{{ monitor_configuration_policy.data.id }}"
    And the response "data" has item with field "attributes.policy_type" with value "tag"
    And the response "data" has item with field "attributes.policy.tag_key" with value "{{ unique_lower_alnum }}"
    And the response "data" has item with field "attributes.policy.valid_tag_values" with value ["prod", "staging"]
