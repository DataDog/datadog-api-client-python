@endpoint(asm-exclusion-filters) @endpoint(asm-exclusion-filters-v2)
Feature: ASM Exclusion Filters
  Exclusion filters in ASM libraries are used to circumvent false positives
  in protection.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ASMExclusionFilters" API

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Create a ASM WAF Exclusion filter returns "Bad Request" response
    Given new "CreateASMExclusionFilter" request
    And body with value {"data": {"type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Create a ASM WAF Exclusion filter returns "Conflict" response
    Given new "CreateASMExclusionFilter" request
    And body with value {"data": {"type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip @team:DataDog/asm-respond-backend
  Scenario: Create a ASM WAF Exclusion filter returns "OK" response
    Given new "CreateASMExclusionFilter" request
    And body with value {"data": {"type": "exclusion_filter","attributes":{"description":"my description","enabled":true,"path_glob":"*","rules_target":[{"tags":{"category":"attack_attempt","type":"sql_injection"}}],"scope":[{"env":"staging","service":"container-resolver"}]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Delete a ASM Exclusion Filter returns "Not Found" response
    Given new "DeleteASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Delete a ASM Exclusion Filter returns "OK" response
    Given new "DeleteASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Get a specific ASM Exclusion Filter returns "OK" response
    Given new "GetASMExclusionFilters" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: List ASM Exclusion Filters returns "OK" response
    Given new "ListASMExclusionFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update a ASM Exclusion filter returns "Bad Request" response
    Given new "UpdateASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "My Exclusion filter", "enabled": true, "ip_list": ["127.0.0.1"], "path_glob": "/lfi_include/*", "rules_target": [{"tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "dd-appsec-php-support", "service": "anil-php-weblog"}]}, "id": "3dd-0uc-h1s", "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update a ASM Exclusion filter returns "Concurrent Modification" response
    Given new "UpdateASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "My Exclusion filter", "enabled": true, "ip_list": ["127.0.0.1"], "path_glob": "/lfi_include/*", "rules_target": [{"tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "dd-appsec-php-support", "service": "anil-php-weblog"}]}, "id": "3dd-0uc-h1s", "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update a ASM Exclusion filter returns "Not Found" response
    Given new "UpdateASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "My Exclusion filter", "enabled": true, "ip_list": ["127.0.0.1"], "path_glob": "/lfi_include/*", "rules_target": [{"tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "dd-appsec-php-support", "service": "anil-php-weblog"}]}, "id": "3dd-0uc-h1s", "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/asm-respond-backend
  Scenario: Update a ASM Exclusion filter returns "OK" response
    Given new "UpdateASMExclusionFilter" request
    And request contains "exclusion_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "My Exclusion filter", "enabled": true, "ip_list": ["127.0.0.1"], "path_glob": "/lfi_include/*", "rules_target": [{"tags": {"category": "attack_attempt", "type": "lfi"}}], "scope": [{"env": "dd-appsec-php-support", "service": "anil-php-weblog"}]}, "id": "3dd-0uc-h1s", "type": "exclusion_filter"}}
    When the request is sent
    Then the response status is 200 OK
