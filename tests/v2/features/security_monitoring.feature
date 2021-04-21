@endpoint(security-monitoring)
Feature: Security Monitoring
  Detection rules for generating signals and listing of generated signals.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Delete a non existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "ThisRuleIdProbablyDoesntExist"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Delete an existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: Delete an existing rule returns "OK" response
    Given there is a valid "security_rule" in the system
    And new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get a list of security signals returns "Bad Request" response
    Given operation "SearchSecurityMonitoringSignals" enabled
    And new "SearchSecurityMonitoringSignals" request
    And body {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a list of security signals returns "OK" response
    Given operation "SearchSecurityMonitoringSignals" enabled
    And new "SearchSecurityMonitoringSignals" request
    And body {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a quick list of security signals returns "Bad Request" response
    Given operation "ListSecurityMonitoringSignals" enabled
    And new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a quick list of security signals returns "OK" response
    Given operation "ListSecurityMonitoringSignals" enabled
    And new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a rule's details returns "Not Found" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get a rule's details returns "OK" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List rules returns "Bad Request" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: List rules returns "OK" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "info"}], "filters": [{"action": "require", "query": null}], "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "info"}], "filters": [{"action": "require", "query": null}], "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "info"}], "filters": [{"action": "require", "query": null}], "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null]}
    When the request is sent
    Then the response status is 200 OK
