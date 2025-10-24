@endpoint(static-analysis) @endpoint(static-analysis-v2)
Feature: Static Analysis
  API for static analysis

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "StaticAnalysis" API

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: POST request to resolve vulnerable symbols returns "OK" response
    Given operation "CreateSCAResolveVulnerableSymbols" enabled
    And new "CreateSCAResolveVulnerableSymbols" request
    And body with value {"data": {"attributes": {"purls": []}, "type": "resolve-vulnerable-symbols-request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Post dependencies for analysis returns "OK" response
    Given operation "CreateSCAResult" enabled
    And new "CreateSCAResult" request
    And body with value {"data": {"attributes": {"commit": {}, "dependencies": [{"exclusions": [], "locations": [{"block": {"end": {}, "start": {}}, "name": {"end": {}, "start": {}}, "namespace": {"end": {}, "start": {}}, "version": {"end": {}, "start": {}}}], "reachable_symbol_properties": [{}]}], "files": [{}], "relations": [{"depends_on": []}], "repository": {}, "vulnerabilities": [{"affects": [{}]}]}, "type": "scarequests"}}
    When the request is sent
    Then the response status is 200 OK
