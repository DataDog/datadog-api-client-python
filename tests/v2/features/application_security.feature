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

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Create an Application Security exclusion filter returns "Bad Request" response
    Given new "CreateApplicationSecurityExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Create an Application Security exclusion filter returns "Conflict" response
    Given new "CreateApplicationSecurityExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Create an Application Security exclusion filter returns "OK" response
    Given new "CreateApplicationSecurityExclusionFilter" request
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Delete an Application Security exclusion filter returns "Not Found" response
    Given new "DeleteApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Delete an Application Security exclusion filter returns "OK" response
    Given new "DeleteApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Get an Application Security exclusion filter returns "OK" response
    Given new "GetApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: List all Application Security exclusion filters returns "OK" response
    Given new "ListApplicationSecurityExclusionFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update an Application Security exclusion filter returns "Bad Request" response
    Given new "UpdateApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update an Application Security exclusion filter returns "Concurrent Modification" response
    Given new "UpdateApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update an Application Security exclusion filter returns "Not Found" response
    Given new "UpdateApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update an Application Security exclusion filter returns "OK" response
    Given new "UpdateApplicationSecurityExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Exclude false positives on a path", "enabled": true, "ip_list": ["198.51.100.72"], "on_match": "monitor", "parameters": ["list.search.query"], "path_glob": "/accounts/*", "rules_target": [{"rule_id": "dog-913-009", "tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "www", "service": "prod"}]}, "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 200 OK
