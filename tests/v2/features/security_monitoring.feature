@endpoint(security-monitoring) @endpoint(security-monitoring-v2)
Feature: Security Monitoring
  Detection rules for generating signals and listing of generated signals.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a detection rule with type 'workload_security' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":"", "agentRule":{"agentRuleId": "kernel_module_unlink_2", "expression": "(open.flags & ((O_CREAT|O_RDWR|O_WRONLY|O_TRUNC)) > 0)"}}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type": "workload_security"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a security filter returns "Bad Request" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a security filter returns "Conflict" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Conflict

  Scenario: Create a security filter returns "OK" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a security filter returns "Too many requests" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 429 Too many requests

  @skip
  Scenario: Delete a non existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "ThisRuleIdProbablyDoesntExist"
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: Delete a security filter returns "No Content" response
    Given there is a valid "security_filter" in the system
    And new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip
  Scenario: Delete a security filter returns "Not Found" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @skip
  Scenario: Delete a security filter returns "OK" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a security filter returns "Too many requests" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 429 Too many requests

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
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a list of security signals returns "OK" response
    Given operation "SearchSecurityMonitoringSignals" enabled
    And new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
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
  Scenario: Get a security filter returns "Not Found" response
    Given new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: Get a security filter returns "OK" response
    Given there is a valid "security_filter" in the system
    And new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a security filter returns "Too many requests" response
    Given new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 429 Too many requests

  Scenario: Get all security filters returns "OK" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all security filters returns "Too many requests" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 429 Too many requests

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
  Scenario: Update a security filter returns "Bad Request" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a security filter returns "Concurrent Modification" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip
  Scenario: Update a security filter returns "Not Found" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: Update a security filter returns "OK" response
    Given new "UpdateSecurityFilter" request
    And there is a valid "security_filter" in the system
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a security filter returns "Too many requests" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "<PATH>"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 429 Too many requests

  @generated @skip
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body with value {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "critical"}], "filters": [{"action": "require", "query": null}], "hasExtendedTitle": true, "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null], "version": 1}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body with value {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "critical"}], "filters": [{"action": "require", "query": null}], "hasExtendedTitle": true, "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null], "version": 1}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body with value {"cases": [{"condition": null, "name": null, "notifications": [null], "status": "critical"}], "filters": [{"action": "require", "query": null}], "hasExtendedTitle": true, "isEnabled": null, "message": null, "name": null, "options": {"detectionMethod": "threshold", "evaluationWindow": 0, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0}}, "queries": [{"agentRule": {"agentRuleId": "etc_shadow", "expression": null}, "aggregation": "count", "distinctFields": [null], "groupByFields": [null], "metric": null, "name": null, "query": null}], "tags": [null], "version": 1}
    When the request is sent
    Then the response status is 200 OK
