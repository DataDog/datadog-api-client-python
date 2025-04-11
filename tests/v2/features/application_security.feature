@endpoint(application-security) @endpoint(application-security-v2)
Feature: Application Security
  [Datadog Application
  Security](https://docs.datadoghq.com/security/application_security/)
  provides protection against application-level attacks that aim to exploit
  code-level vulnerabilities, such as Server-Side-Request-Forgery (SSRF),
  SQL injection, Log4Shell, and Reflected Cross-Site-Scripting (XSS). You
  can monitor and protect apps hosted directly on a server, Docker,
  Kubernetes, Amazon ECS, and (for supported languages) AWS Fargate.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ApplicationSecurity" API

  @generated @skip @team:DataDog/asm-backend
  Scenario: Create a WAF custom rule returns "Bad Request" response
    Given new "CreateApplicationSecurityWafCustomRule" request
    And body with value {"data": {"attributes": {"action": {"action": "block_request", "parameters": {"location": "/blocking", "status_code": 403}}, "blocking": false, "conditions": [{"operator": "match_regex", "parameters": {"data": "blocked_users", "inputs": [{"address": "server.db.statement", "key_path": []}], "list": [], "options": {"case_sensitive": false, "min_length": 0}, "regex": "path.*", "value": "custom_tag"}}], "enabled": false, "name": "Block request from a bad useragent", "path_glob": "/api/search/*", "scope": [{"env": "prod", "service": "billing-service"}], "tags": {"category": "business_logic", "type": "users.login.success"}}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-backend
  Scenario: Create a WAF custom rule returns "Concurrent Modification" response
    Given new "CreateApplicationSecurityWafCustomRule" request
    And body with value {"data": {"attributes": {"action": {"action": "block_request", "parameters": {"location": "/blocking", "status_code": 403}}, "blocking": false, "conditions": [{"operator": "match_regex", "parameters": {"data": "blocked_users", "inputs": [{"address": "server.db.statement", "key_path": []}], "list": [], "options": {"case_sensitive": false, "min_length": 0}, "regex": "path.*", "value": "custom_tag"}}], "enabled": false, "name": "Block request from a bad useragent", "path_glob": "/api/search/*", "scope": [{"env": "prod", "service": "billing-service"}], "tags": {"category": "business_logic", "type": "users.login.success"}}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/asm-backend
  Scenario: Create a WAF custom rule returns "Created" response
    Given new "CreateApplicationSecurityWafCustomRule" request
    And body with value {"data": {"attributes": {"action": {"action": "block_request", "parameters": {"location": "/blocking", "status_code": 403}}, "blocking": false, "conditions": [{"operator": "match_regex", "parameters": {"data": "blocked_users", "inputs": [{"address": "server.db.statement", "key_path": []}], "list": [], "options": {"case_sensitive": false, "min_length": 0}, "regex": "path.*", "value": "custom_tag"}}], "enabled": false, "name": "Block request from a bad useragent", "path_glob": "/api/search/*", "scope": [{"env": "prod", "service": "billing-service"}], "tags": {"category": "business_logic", "type": "users.login.success"}}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/asm-backend
  Scenario: Create a WAF exclusion filter returns "Bad Request" response
    Given new "CreateApplicationSecurityWafExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-backend
  Scenario: Create a WAF exclusion filter returns "Concurrent Modification" response
    Given new "CreateApplicationSecurityWafExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/asm-backend
  Scenario: Create a WAF exclusion filter returns "OK" response
    Given new "CreateApplicationSecurityWafExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.enabled" is equal to true

  @team:DataDog/asm-backend
  Scenario: Create a legacy WAF exclusion filter returns "Bad Request" response
    Given new "CreateApplicationSecurityWafExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "event_query": "test:1"}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-backend
  Scenario: Delete a WAF Custom Rule returns "Concurrent Modification" response
    Given new "DeleteApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/asm-backend
  Scenario: Delete a WAF Custom Rule returns "No Content" response
    Given new "DeleteApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/asm-backend
  Scenario: Delete a WAF Custom Rule returns "Not Found" response
    Given new "DeleteApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/asm-backend
  Scenario: Delete a WAF exclusion filter returns "Concurrent Modification" response
    Given new "DeleteApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/asm-backend
  Scenario: Delete a WAF exclusion filter returns "Not Found" response
    Given new "DeleteApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter with value "unknown"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/asm-backend
  Scenario: Delete a WAF exclusion filter returns "OK" response
    Given there is a valid "exclusion_filter" in the system
    And new "DeleteApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "exclusion_filter.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/asm-backend
  Scenario: Get a WAF custom rule returns "OK" response
    Given new "GetApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-backend
  Scenario: Get a WAF exclusion filter returns "Not Found" response
    Given new "GetApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/asm-backend
  Scenario: Get a WAF exclusion filter returns "OK" response
    Given there is a valid "exclusion_filter" in the system
    And new "GetApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "exclusion_filter.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/asm-backend
  Scenario: List all WAF custom rules returns "OK" response
    Given new "ListApplicationSecurityWAFCustomRules" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/asm-backend
  Scenario: List all WAF exclusion filters returns "OK" response
    Given new "ListApplicationSecurityWafExclusionFilters" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/asm-backend
  Scenario: Update a WAF Custom Rule returns "Bad Request" response
    Given there is a valid "custom_rule" in the system
    And new "UpdateApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "custom_rule.data.id"
    And body with value {"data": {"type": "custom_rule", "attributes": {"blocking": false, "conditions": [{"operator": "match_regex", "parameters": { "inputs": [ { "address": "server.request.query", "key_path": [ "id" ] } ], "regex": "\\" } } ], "enabled": false, "name": "test", "path_glob": "/test", "scope": [ { "env": "test", "service": "test" } ], "tags": { "category": "attack_attempt", "type": "test"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-backend
  Scenario: Update a WAF Custom Rule returns "Concurrent Modification" response
    Given new "UpdateApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"action": "block_request", "parameters": {"location": "/blocking", "status_code": 403}}, "blocking": false, "conditions": [{"operator": "match_regex", "parameters": {"data": "blocked_users", "inputs": [{"address": "server.db.statement", "key_path": []}], "list": [], "options": {"case_sensitive": false, "min_length": 0}, "regex": "path.*", "value": "custom_tag"}}], "enabled": false, "name": "Block request from bad useragent", "path_glob": "/api/search/*", "scope": [{"env": "prod", "service": "billing-service"}], "tags": {"category": "business_logic", "type": "users.login.success"}}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/asm-backend
  Scenario: Update a WAF Custom Rule returns "Not Found" response
    Given new "UpdateApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"action": "block_request", "parameters": {"location": "/blocking", "status_code": 403}}, "blocking": false, "conditions": [{"operator": "match_regex", "parameters": {"data": "blocked_users", "inputs": [{"address": "server.db.statement", "key_path": []}], "list": [], "options": {"case_sensitive": false, "min_length": 0}, "regex": "path.*", "value": "custom_tag"}}], "enabled": false, "name": "Block request from bad useragent", "path_glob": "/api/search/*", "scope": [{"env": "prod", "service": "billing-service"}], "tags": {"category": "business_logic", "type": "users.login.success"}}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/asm-backend
  Scenario: Update a WAF Custom Rule returns "OK" response
    Given there is a valid "custom_rule" in the system
    And new "UpdateApplicationSecurityWafCustomRule" request
    And request contains "custom_rule_id" parameter from "custom_rule.data.id"
    And body with value {"data": {"type": "custom_rule", "attributes": {"blocking": false, "conditions": [{"operator": "match_regex", "parameters": { "inputs": [ { "address": "server.request.query", "key_path": [ "id" ] } ], "regex": "badactor" } } ], "enabled": false, "name": "test", "path_glob": "/test", "scope": [ { "env": "test", "service": "test" } ], "tags": { "category": "attack_attempt", "type": "test"}}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/asm-backend
  Scenario: Update a WAF exclusion filter returns "Bad Request" response
    Given there is a valid "custom_rule" in the system
    And new "UpdateApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "custom_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": false, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-backend
  Scenario: Update a WAF exclusion filter returns "Concurrent Modification" response
    Given new "UpdateApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/asm-backend
  Scenario: Update a WAF exclusion filter returns "Not Found" response
    Given new "UpdateApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter with value "unknown"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/asm-backend
  Scenario: Update a WAF exclusion filter returns "OK" response
    Given there is a valid "exclusion_filter" in the system
    And new "UpdateApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "exclusion_filter.data.id"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": false, "ip_list": ["198.51.100.72"], "on_match": "monitor"}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/asm-backend
  Scenario: Update a legacy WAF exclusion filter returns "Bad Request" response
    Given there is a valid "exclusion_filter" in the system
    And new "UpdateApplicationSecurityWafExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "exclusion_filter.data.id"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "event_query": "test:1"}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request
