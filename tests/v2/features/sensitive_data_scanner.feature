@endpoint(sensitive-data-scanner) @endpoint(sensitive-data-scanner-v2) @endpoint(sensitivedatascanner) @endpoint(sensitivedatascanner-v2)
Feature: Sensitive Data Scanner
  Create, update, delete, and retrieve sensitive data scanner groups and
  rules. See the [Sensitive Data Scanner
  page](https://docs.datadoghq.com/sensitive_data_scanner/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SensitiveDataScanner" API

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Create Scanning Group returns "Bad Request" response
    Given new "CreateScanningGroup" request
    And body with value {"data": {"attributes": {"filter": {}, "product_list": ["logs"], "samplings": [{"product": "logs", "rate": 100.0}]}, "relationships": {"configuration": {"data": {"type": "sensitive_data_scanner_configuration"}}, "rules": {"data": [{"type": "sensitive_data_scanner_rule"}]}}, "type": "sensitive_data_scanner_group"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/sensitive-data-scanner
  Scenario: Create Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And new "CreateScanningGroup" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_group","attributes":{"name":"{{ unique }}","is_enabled":false,"product_list":["logs"],"filter":{"query":"*"}},"relationships":{"configuration":{"data":{"type":"sensitive_data_scanner_configuration","id":"{{ configuration.data.id }}"}},"rules":{"data":[]}}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "sensitive_data_scanner_group"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @team:DataDog/sensitive-data-scanner
  Scenario: Create Scanning Rule returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "CreateScanningRule" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/sensitive-data-scanner
  Scenario: Create Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "CreateScanningRule" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern", "namespaces": ["admin"], "excluded_namespaces": ["admin.name"], "text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true,"priority":1,"included_keyword_configuration":{"keywords":["credit card"],"character_count":35}},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "sensitive_data_scanner_rule"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.pattern" is equal to "pattern"
    And the response "data.attributes.included_keyword_configuration.character_count" is equal to 35
    And the response "data.attributes.included_keyword_configuration.keywords[0]" is equal to "credit card"

  @team:DataDog/sensitive-data-scanner
  Scenario: Create Scanning Rule with should_save_match returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "CreateScanningRule" request
    And body with value {"meta":{},"data":{"type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"replacement_string","replacement_string":"REDACTED","should_save_match":true},"tags":["sensitive_data:true"],"is_enabled":true,"priority":1},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "sensitive_data_scanner_rule"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Group returns "Bad Request" response
    Given new "DeleteScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Group returns "Not Found" response
    Given new "DeleteScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "DeleteScanningGroup" request
    And request contains "group_id" parameter from "group.data.id"
    And body with value {"meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Rule returns "Bad Request" response
    Given new "DeleteScanningRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Rule returns "Not Found" response
    Given new "DeleteScanningRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"meta": {"version": 0}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/sensitive-data-scanner
  Scenario: Delete Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "DeleteScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: List Scanning Groups returns "Bad Request" response
    Given new "ListScanningGroups" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/sensitive-data-scanner
  Scenario: List Scanning Groups returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "ListScanningGroups" request
    When the request is sent
    Then the response status is 200 OK
    And the response "included" has item with field "id" with value "{{ group.data.id }}"

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: List standard patterns returns "Bad Request" response
    Given new "ListStandardPatterns" request
    When the request is sent
    Then the response status is 400 Bad Request

  @integration-only @team:DataDog/sensitive-data-scanner
  Scenario: List standard patterns returns "OK" response
    Given new "ListStandardPatterns" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/sensitive-data-scanner
  Scenario: Reorder Groups returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "ReorderScanningGroups" request
    And body with value {"data": {"relationships": {"groups": {"data": [{"type": "sensitive_data_scanner_group", "id": "{{ unique }}"}]}}, "type": "sensitive_data_scanner_configuration", "id": "{{ configuration.data.id }}"}, "meta": {}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/sensitive-data-scanner
  Scenario: Reorder Groups returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And a valid "configuration" in the system
    And new "ReorderScanningGroups" request
    And body with value {"data": {"relationships": {"groups": {"data": [{"type": "sensitive_data_scanner_group", "id": "{{ group.data.id }}"}]}}, "type": "sensitive_data_scanner_configuration", "id": "{{ configuration.data.id }}"}, "meta": {}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Group returns "Bad Request" response
    Given new "UpdateScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": {}, "product_list": ["logs"], "samplings": [{"product": "logs", "rate": 100.0}]}, "relationships": {"configuration": {"data": {"type": "sensitive_data_scanner_configuration"}}, "rules": {"data": [{"type": "sensitive_data_scanner_rule"}]}}, "type": "sensitive_data_scanner_group"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Group returns "Not Found" response
    Given new "UpdateScanningGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": {}, "product_list": ["logs"], "samplings": [{"product": "logs", "rate": 100.0}]}, "relationships": {"configuration": {"data": {"type": "sensitive_data_scanner_configuration"}}, "rules": {"data": [{"type": "sensitive_data_scanner_rule"}]}}, "type": "sensitive_data_scanner_group"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Group returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And new "UpdateScanningGroup" request
    And request contains "group_id" parameter from "group.data.id"
    And body with value {"meta": {},"data":{"id": "{{ group.data.id }}", "type":"sensitive_data_scanner_group","attributes":{"name":"{{ unique }}","is_enabled":false,"product_list":["logs"],"filter":{"query":"*"}},"relationships":{"configuration":{"data":{"type":"sensitive_data_scanner_configuration","id":"{{ configuration.data.id }}"}},"rules":{"data":[]}}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Rule returns "Bad Request" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "UpdateScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta":{},"data":{"attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true},"relationships":{"group":{"data":{"type":"{{ group.data.type }}","id":"{{ group.data.id }}"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Rule returns "Not Found" response
    Given new "UpdateScanningRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"excluded_namespaces": ["admin.name"], "included_keyword_configuration": {"character_count": 30, "keywords": ["email", "address", "login"]}, "namespaces": ["admin"], "suppressions": {"ends_with": ["@example.com", "another.example.com"], "exact_match": ["admin@example.com", "user@example.com"], "starts_with": ["admin", "user"]}, "tags": [], "text_replacement": {"type": "none"}}, "relationships": {"group": {"data": {"type": "sensitive_data_scanner_group"}}, "standard_pattern": {"data": {"type": "sensitive_data_scanner_standard_pattern"}}}, "type": "sensitive_data_scanner_rule"}, "meta": {"version": 0}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/sensitive-data-scanner
  Scenario: Update Scanning Rule returns "OK" response
    Given a valid "configuration" in the system
    And there is a valid "scanning_group" in the system
    And the "scanning_group" has a "scanning_rule"
    And new "UpdateScanningRule" request
    And request contains "rule_id" parameter from "rule.data.id"
    And body with value {"meta":{},"data":{"id": "{{ rule.data.id }}", "type":"sensitive_data_scanner_rule","attributes":{"name":"{{ unique }}","pattern":"pattern","text_replacement":{"type":"none"},"tags":["sensitive_data:true"],"is_enabled":true,"priority":5,"included_keyword_configuration": {"keywords": ["credit card", "cc"], "character_count":35}}}}
    When the request is sent
    Then the response status is 200 OK
