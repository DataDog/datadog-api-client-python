@endpoint(sensitive-data-scanner) @endpoint(sensitive-data-scanner-v2) @endpoint(sensitivedatascanner) @endpoint(sensitivedatascanner-v2)
Feature: Sensitive Data Scanner
  Create, update, delete, and retrieve sensitive data scanner groups and
  rules.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SensitiveDataScanner" API

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Create Scanning Group returns "Bad Request" response
    Given new "CreateScanningGroup" request
    And body with value {"data": {"attributes": {"filter": {}, "product_list": ["logs"]}, "relationships": {"configuration": {"data": {"type": "sensitive_data_scanner_configuration"}}, "rules": {"data": [{"type": "sensitive_data_scanner_rule"}]}}, "type": "sensitive_data_scanner_group"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Create Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And new "CreateScanningGroup" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_group","attributes":{"name":"{{ unique }}","is_enabled":false,"product_list":["logs"],"filter":{"query":"*"}},"relationships":{"configuration":{"data":{"type":"sensitive_data_scanner_configuration","id":"{{ configuration.data.id }}"}},"rules":{"data":[]}}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Create Scanning Rule returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "CreateScanningRule" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Create Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "CreateScanningRule" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Delete Scanning Group returns "Bad Request" response
    Given new "DeleteScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Delete Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "DeleteScanningGroup" request
    And request contains "group_id" parameter from "group.data.id"
    And body with value {"meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Delete Scanning Rule returns "Bad Request" response
    Given new "DeleteScanningRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Delete Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "DeleteScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: List Scanning Groups returns "Bad Request" response
    Given new "ListScanningGroups" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: List Scanning Groups returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "ListScanningGroups" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: List standard patterns returns "Bad Request" response
    Given new "ListStandardPatterns" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: List standard patterns returns "OK" response
    Given new "ListStandardPatterns" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Reorder Groups returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "ReorderScanningGroups" request
    And body with value {"data": {"relationships": {"groups": {"data": [{"type": "sensitive_data_scanner_group", "id": "{{ unique }}"}]}}, "type": "sensitive_data_scanner_configuration", "id": "{{ configuration.data.id }}"}, "meta": {}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Reorder Groups returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "ReorderScanningGroups" request
    And body with value {"data": {"relationships": {"groups": {"data": [{"type": "sensitive_data_scanner_group", "id": "{{ group.data.id }}"}]}}, "type": "sensitive_data_scanner_configuration", "id": "{{ configuration.data.id }}"}, "meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Update Scanning Group returns "Bad Request" response
    Given new "UpdateScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": {}, "product_list": ["logs"]}, "relationships": {"configuration": {"data": {"type": "sensitive_data_scanner_configuration"}}, "rules": {"data": [{"type": "sensitive_data_scanner_rule"}]}}, "type": "sensitive_data_scanner_group"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Update Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "UpdateScanningGroup" request
    And request contains "group_id" parameter from "group.data.id"
    And body with value {"meta": {},"data":{"id": "{{ group.data.id }}", "type":"sensitive_data_scanner_group","attributes":{"name":"{{ unique }}","is_enabled":false,"product_list":["logs"],"filter":{"query":"*"}},"relationships":{"configuration":{"data":{"type":"sensitive_data_scanner_configuration","id":"{{ configuration.data.id }}"}},"rules":{"data":[]}}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Update Scanning Rule returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "UpdateScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app @team:DataDog/logs-core
  Scenario: Update Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "UpdateScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta":{},"data":{"id": "{{ rule.data.id }}", "type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 200 OK
