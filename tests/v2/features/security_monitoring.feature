@endpoint(security-monitoring) @endpoint(security-monitoring-v2)
Feature: Security Monitoring
  Detection rules for generating signals and listing of generated signals.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Change the related incidents of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Change the related incidents of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Change the related incidents of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Change the triage state of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Change the triage state of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Change the triage state of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'impossible_travel' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"queries":[{"aggregation":"geo_data","groupByFields":["@usr.id"],"distinctFields":[],"metric":"@network.client.geoip","query":"*"}],"cases":[{"name":"","status":"info","notifications":[]}],"hasExtendedTitle":true,"message":"test","isEnabled":true,"options":{"maxSignalDuration":86400,"evaluationWindow":900,"keepAlive":3600,"detectionMethod":"impossible_travel","impossibleTravelOptions":{"baselineUserLocations":false}},"name":"{{ unique }}","type":"log_detection","tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'workload_security' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type": "workload_security"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Create a security filter returns "Bad Request" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Create a security filter returns "Conflict" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a security filter returns "OK" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a non existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "ThisRuleIdProbablyDoesntExist"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a security filter returns "No Content" response
    Given there is a valid "security_filter" in the system
    And new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a security filter returns "Not Found" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a security filter returns "OK" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing rule returns "OK" response
    Given there is a valid "security_rule" in the system
    And new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a list of security signals returns "Bad Request" response
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a list of security signals returns "OK" response
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/k9-cloud-security-platform @with-pagination
  Scenario: Get a list of security signals returns "OK" response with pagination
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "{{ timeISO("now-15m") }}", "query": "security:attack status:high", "to": "{{ timeISO("now") }}"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a quick list of security signals returns "Bad Request" response
    Given new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a quick list of security signals returns "OK" response
    Given new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/k9-cloud-security-platform @with-pagination
  Scenario: Get a quick list of security signals returns "OK" response with pagination
    Given new "ListSecurityMonitoringSignals" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's details returns "Not Found" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's details returns "OK" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a security filter returns "Not Found" response
    Given new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a security filter returns "OK" response
    Given there is a valid "security_filter" in the system
    And new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get all security filters returns "OK" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: List rules returns "Bad Request" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: List rules returns "OK" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"assignee": {"uuid": ""}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a security filter returns "Bad Request" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a security filter returns "Concurrent Modification" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a security filter returns "Not Found" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Update a security filter returns "OK" response
    Given new "UpdateSecurityFilter" request
    And there is a valid "security_filter" in the system
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"cases": [{"notifications": [], "status": "critical"}], "filters": [{"action": "require"}], "hasExtendedTitle": true, "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}}, "queries": [{"aggregation": "count", "distinctFields": [], "groupByFields": []}], "tags": [], "version": 1}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"cases": [{"notifications": [], "status": "critical"}], "filters": [{"action": "require"}], "hasExtendedTitle": true, "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}}, "queries": [{"aggregation": "count", "distinctFields": [], "groupByFields": []}], "tags": [], "version": 1}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"cases": [{"notifications": [], "status": "critical"}], "filters": [{"action": "require"}], "hasExtendedTitle": true, "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}}, "queries": [{"aggregation": "count", "distinctFields": [], "groupByFields": []}], "tags": [], "version": 1}
    When the request is sent
    Then the response status is 200 OK
