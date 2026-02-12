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

  @skip-validation @team:DataDog/monitor-app
  Scenario: Create a monitor notification rule returns "Bad Request" response
    Given new "CreateMonitorNotificationRule" request
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}", "host:abc"]}, "name": "test rule", "recipients": ["@slack-test-channel", "@jira-test"]}, "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Create a monitor notification rule returns "OK" response
    Given new "CreateMonitorNotificationRule" request
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}"]}, "name": "test rule", "recipients": ["slack-test-channel", "jira-test"]}, "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "test rule"

  @team:DataDog/monitor-app
  Scenario: Create a monitor notification rule with conditional recipients returns "OK" response
    Given new "CreateMonitorNotificationRule" request
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}"]}, "name": "test rule", "conditional_recipients": {"conditions": [{"scope": "transition_type:is_alert", "recipients": ["slack-test-channel", "jira-test"]}]}}, "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "test rule"

  @team:DataDog/monitor-app
  Scenario: Create a monitor notification rule with scope returns "OK" response
    Given new "CreateMonitorNotificationRule" request
    And body with value {"data": {"attributes": {"filter": {"scope": "test:{{ unique_lower }}"}, "name": "test rule", "recipients": ["slack-test-channel", "jira-test"]}, "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "test rule"

  @skip-validation @team:DataDog/monitor-app
  Scenario: Create a monitor user template returns "Bad Request" response
    Given new "CreateMonitorUserTemplate" request
    And operation "CreateMonitorUserTemplate" enabled
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Create a monitor user template returns "OK" response
    Given new "CreateMonitorUserTemplate" request
    And operation "CreateMonitorUserTemplate" enabled
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 200 OK

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
  Scenario: Delete a monitor notification rule returns "Not Found" response
    Given new "DeleteMonitorNotificationRule" request
    And request contains "rule_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Delete a monitor notification rule returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "DeleteMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/monitor-app
  Scenario: Delete a monitor user template returns "Not Found" response
    Given new "DeleteMonitorUserTemplate" request
    And operation "DeleteMonitorUserTemplate" enabled
    And request contains "template_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/monitor-app
  Scenario: Delete a monitor user template returns "OK" response
    Given operation "DeleteMonitorUserTemplate" enabled
    And new "DeleteMonitorUserTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
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
  Scenario: Get a monitor notification rule returns "Not Found" response
    Given new "GetMonitorNotificationRule" request
    And request contains "rule_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Get a monitor notification rule returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "GetMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "test rule"

  @team:DataDog/monitor-app
  Scenario: Get a monitor user template returns "Not Found" response
    Given new "GetMonitorUserTemplate" request
    And operation "GetMonitorUserTemplate" enabled
    And request contains "template_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Get a monitor user template returns "OK" response
    Given there is a valid "monitor_user_template" in the system
    And new "GetMonitorUserTemplate" request
    And operation "GetMonitorUserTemplate" enabled
    And request contains "template_id" parameter from "monitor_user_template.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "monitor-user-template"

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

  @team:DataDog/monitor-app
  Scenario: Get all monitor notification rules returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "GetMonitorNotificationRules" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.name" with value "test rule"

  @team:DataDog/monitor-app
  Scenario: Get all monitor user templates returns "OK" response
    Given there is a valid "monitor_user_template" in the system
    And new "ListMonitorUserTemplates" request
    And operation "ListMonitorUserTemplates" enabled
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "type" with value "monitor-user-template"
    And the response "data" has item with field "id" with value "{{ monitor_user_template.data.id }}"
    And the response "data" has item with field "attributes.description" with value "It's a threshold"
    And the response "data" has item with field "attributes.monitor_definition.message" with value "cats"

  @skip-validation @team:DataDog/monitor-app
  Scenario: Update a monitor notification rule returns "Bad Request" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "UpdateMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}", "host:abc"]}, "name": "updated rule", "recipients": ["@slack-test-channel"]}, "id": "{{ monitor_notification_rule.data.id }}", "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Update a monitor notification rule returns "Not Found" response
    Given new "UpdateMonitorNotificationRule" request
    And request contains "rule_id" parameter with value "00000000-0000-1234-0000-000000000000"
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}", "host:abc"]}, "name": "updated rule", "recipients": ["slack-test-channel", "jira-test"]}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Update a monitor notification rule returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "UpdateMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}", "host:abc"]}, "name": "updated rule", "recipients": ["slack-test-channel"]}, "id": "{{ monitor_notification_rule.data.id }}", "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "updated rule"

  @team:DataDog/monitor-app
  Scenario: Update a monitor notification rule with conditional_recipients returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "UpdateMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    And body with value {"data": {"attributes": {"filter": {"tags": ["test:{{ unique_lower }}", "host:abc"]}, "name": "updated rule", "conditional_recipients": {"conditions": [{"scope": "transition_type:is_alert", "recipients": ["slack-test-channel", "jira-test"]}]}}, "id": "{{ monitor_notification_rule.data.id }}", "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "updated rule"

  @team:DataDog/monitor-app
  Scenario: Update a monitor notification rule with scope returns "OK" response
    Given there is a valid "monitor_notification_rule" in the system
    And new "UpdateMonitorNotificationRule" request
    And request contains "rule_id" parameter from "monitor_notification_rule.data.id"
    And body with value {"data": {"attributes": {"filter": {"scope": "test:{{ unique_lower }}"}, "name": "updated rule", "recipients": ["slack-test-channel"]}, "id": "{{ monitor_notification_rule.data.id }}", "type": "monitor-notification-rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "updated rule"

  @skip-validation @team:DataDog/monitor-app
  Scenario: Update a monitor user template to a new version returns "Bad Request" response
    Given there is a valid "monitor_user_template" in the system
    And operation "UpdateMonitorUserTemplate" enabled
    And new "UpdateMonitorUserTemplate" request
    And request contains "template_id" parameter from "monitor_user_template.data.id"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Update a monitor user template to a new version returns "Not Found" response
    Given new "UpdateMonitorUserTemplate" request
    And operation "UpdateMonitorUserTemplate" enabled
    And request contains "template_id" parameter with value "00000000-0000-1234-0000-000000000000"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Update a monitor user template to a new version returns "OK" response
    Given there is a valid "monitor_user_template" in the system
    And new "UpdateMonitorUserTemplate" request
    And operation "UpdateMonitorUserTemplate" enabled
    And request contains "template_id" parameter from "monitor_user_template.data.id"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/monitor-app
  Scenario: Validate a monitor user template returns "Bad Request" response
    Given new "ValidateMonitorUserTemplate" request
    And operation "ValidateMonitorUserTemplate" enabled
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Validate a monitor user template returns "OK" response
    Given new "ValidateMonitorUserTemplate" request
    And operation "ValidateMonitorUserTemplate" enabled
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 204 OK

  @skip-validation @team:DataDog/monitor-app
  Scenario: Validate an existing monitor user template returns "Bad Request" response
    Given there is a valid "monitor_user_template" in the system
    And new "ValidateExistingMonitorUserTemplate" request
    And operation "ValidateExistingMonitorUserTemplate" enabled
    And request contains "template_id" parameter from "monitor_user_template.data.id"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Validate an existing monitor user template returns "Not Found" response
    Given new "ValidateExistingMonitorUserTemplate" request
    And operation "ValidateExistingMonitorUserTemplate" enabled
    And request contains "template_id" parameter with value "00000000-0000-1234-0000-000000000000"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Validate an existing monitor user template returns "OK" response
    Given there is a valid "monitor_user_template" in the system
    And new "ValidateExistingMonitorUserTemplate" request
    And operation "ValidateExistingMonitorUserTemplate" enabled
    And request contains "template_id" parameter from "monitor_user_template.data.id"
    And body with value {"data": {"attributes": {"description": "A description.", "monitor_definition": {"message": "A msg.", "name": "A name {{ unique_lower }}", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert"}, "tags": ["integration:Azure"], "template_variables": [{"available_values": ["value1", "value2"], "defaults": ["defaultValue"], "name": "regionName", "tag_key": "datacenter"}], "title": "Postgres DB {{ unique_lower }}"}, "id": "00000000-0000-1234-0000-000000000000", "type": "monitor-user-template"}}
    When the request is sent
    Then the response status is 204 OK
