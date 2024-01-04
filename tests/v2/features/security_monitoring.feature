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
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Change the triage state of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Change the triage state of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}}}
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a cloud_configuration rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"type":"cloud_configuration","name":"{{ unique }}_cloud","isEnabled":false,"cases":[{"status":"info","notifications":["channel"]}],"options":{"complianceRuleOptions":{"resourceType":"gcp_compute_disk","complexRule": false,"regoRule":{"policy":"package datadog\n\nimport data.datadog.output as dd_output\n\nimport future.keywords.contains\nimport future.keywords.if\nimport future.keywords.in\n\nmilliseconds_in_a_day := ((1000 * 60) * 60) * 24\n\neval(iam_service_account_key) = \"skip\" if {\n\tiam_service_account_key.disabled\n} else = \"pass\" if {\n\t(iam_service_account_key.resource_seen_at / milliseconds_in_a_day) - (iam_service_account_key.valid_after_time / milliseconds_in_a_day) <= 90\n} else = \"fail\"\n\n# This part remains unchanged for all rules\nresults contains result if {\n\tsome resource in input.resources[input.main_resource_type]\n\tresult := dd_output.format(resource, eval(resource))\n}\n","resourceTypes":["gcp_compute_disk"]}}},"message":"ddd","tags":["my:tag"],"complianceSignalOptions":{"userActivationStatus":true,"userGroupByFields":["@account_id"]},"filters":[{"action":"require","query":"resource_id:helo*"},{"action":"suppress","query":"control:helo*"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud"
    And the response "type" is equal to "cloud_configuration"
    And the response "message" is equal to "ddd"
    And the response "options.complianceRuleOptions.resourceType" is equal to "gcp_compute_disk"

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "Test rule"

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with detection method 'third_party' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"thirdPartyCases":[{"query":"status:error","name":"high","status":"high"},{"query":"status:info","name":"low","status":"low"}],"queries":[],"cases":[],"message":"This is a third party rule","options":{"detectionMethod":"third_party","keepAlive":0,"maxSignalDuration":0,"thirdPartyRuleOptions":{"defaultStatus":"info","rootQueries":[{"query":"source:guardduty @details.alertType:*EC2*", "groupByFields":["instance-id"]},{"query":"source:guardduty", "groupByFields":[]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "third_party"
    And the response "thirdPartyCases[0].query" is equal to "status:error"

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'impossible_travel' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"queries":[{"aggregation":"geo_data","groupByFields":["@usr.id"],"distinctFields":[],"metric":"@network.client.geoip","query":"*"}],"cases":[{"name":"","status":"info","notifications":[]}],"hasExtendedTitle":true,"message":"test","isEnabled":true,"options":{"maxSignalDuration":86400,"evaluationWindow":900,"keepAlive":3600,"detectionMethod":"impossible_travel","impossibleTravelOptions":{"baselineUserLocations":false}},"name":"{{ unique }}","type":"log_detection","tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "test"
    And the response "options.detectionMethod" is equal to "impossible_travel"

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'signal_correlation' returns "OK" response
    Given there is a valid "security_rule" in the system
    And there is a valid "security_rule_bis" in the system
    And new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}_signal_rule", "queries":[{"ruleId":"{{ security_rule.id }}","aggregation":"event_count","correlatedByFields":["host"],"correlatedQueryIndex":1}, {"ruleId":"{{ security_rule_bis.id }}","aggregation":"event_count","correlatedByFields":["host"]}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0 && b > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test signal correlation rule","tags":[],"isEnabled":true, "type": "signal_correlation"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_signal_rule"
    And the response "type" is equal to "signal_correlation"
    And the response "message" is equal to "Test signal correlation rule"
    And the response "isEnabled" is equal to true

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'workload_security' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type": "workload_security"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "workload_security"
    And the response "message" is equal to "Test rule"
    And the response "isEnabled" is equal to true

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
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.is_enabled" is equal to true
    And the response "data.attributes.exclusion_filters[0].name" is equal to "Exclude staging"
    And the response "data.attributes.exclusion_filters[0].query" is equal to "source:staging"

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

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing rule returns "OK" response
    Given there is a valid "security_rule" in the system
    And new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 204 OK

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Get a cloud configuration rule's details returns "OK" response
    Given there is a valid "cloud_configuration_rule" in the system
    And new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "cloud_configuration_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud"
    And the response "id" has the same value as "cloud_configuration_rule.id"

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "Bad Request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "Not Found: The requested finding cannot be found." response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The requested finding cannot be found.

  @replay-only @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "OK" response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter with value "AgAAAYd59gjghzF52gAAAAAAAAAYAAAAAEFZZDU5Z2pnQUFCRTRvV1lFeEo4SlFBQQAAACQAAAAAMDE4NzdhMDEtMDRiYS00NTZlLWFmMzMtNTIxNmNkNjVlNDMz"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.evaluation" is equal to "pass"

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

  @replay-only @skip-validation @team:DataDog/k9-cloud-security-platform @with-pagination
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

  @replay-only @skip-validation @team:DataDog/k9-cloud-security-platform @with-pagination
  Scenario: Get a quick list of security signals returns "OK" response with pagination
    Given new "ListSecurityMonitoringSignals" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's details returns "Not Found" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "abcde-12345"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's details returns "OK" response
    Given new "GetSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "id" has the same value as "security_rule.id"

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
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.is_enabled" is equal to true
    And the response "data.attributes.exclusion_filters[0].name" is equal to "Exclude logs from staging"
    And the response "data.attributes.exclusion_filters[0].query" is equal to "source:staging"

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Get a signal's details returns "Not Found" response
    Given new "GetSecurityMonitoringSignal" request
    And request contains "signal_id" parameter with value "AQAAAYNqUBVU4-rffwAAAABBWU5xVUJWVUFBQjJBd3ptCL3QUEm3nt2"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Get a signal's details returns "OK" response
    Given new "GetSecurityMonitoringSignal" request
    And request contains "signal_id" parameter with value "AQAAAYNqUBVU4-rffwAAAABBWU5xVUJWVUFBQjJBd3ptMDdQUnF3QUE"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get all security filters returns "OK" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.filtered_data_type" with value "logs"
    And the response "data" has item with field "attributes.is_builtin" with value true

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "Bad Request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 400 Bad Request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "Not Found: The requested finding cannot be found." response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 404 Not Found: The requested finding cannot be found.

  @replay-only @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "OK" response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "finding"

  @generated @skip @team:DataDog/cloud-security-posture-management @with-pagination
  Scenario: List findings returns "OK" response with pagination
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: List rules returns "Bad Request" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: List rules returns "OK" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"name": null, "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"name": null, "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Modify the triage assignee of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"assignee": {"uuid": ""}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Mute or unmute a batch of findings returns "Bad Request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "MuteFindings" enabled
    And new "MuteFindings" request
    And body with value {"data": {"attributes": {"mute": {"expiration_date": 1778721573794, "muted": true, "reason": "ACCEPTED_RISK"}}, "id": "dbe5f567-192b-4404-b908-29b70e1c9f76", "meta": {"findings": [{"finding_id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw=="}]}, "type": "finding"}}
    When the request is sent
    Then the response status is 400 Bad Request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Mute or unmute a batch of findings returns "Invalid Request: The server understands the request syntax but cannot process it due to invalid data." response
    Given operation "MuteFindings" enabled
    And new "MuteFindings" request
    And body with value {"data": {"attributes": {"mute": {"expiration_date": 1778721573794, "muted": true, "reason": "ACCEPTED_RISK"}}, "id": "dbe5f567-192b-4404-b908-29b70e1c9f76", "meta": {"findings": [{"finding_id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw=="}]}, "type": "finding"}}
    When the request is sent
    Then the response status is 422 Invalid Request: The server understands the request syntax but cannot process it due to invalid data.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Mute or unmute a batch of findings returns "Not Found: The requested finding cannot be found." response
    Given operation "MuteFindings" enabled
    And new "MuteFindings" request
    And body with value {"data": {"attributes": {"mute": {"expiration_date": 1778721573794, "muted": true, "reason": "ACCEPTED_RISK"}}, "id": "dbe5f567-192b-4404-b908-29b70e1c9f76", "meta": {"findings": [{"finding_id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw=="}]}, "type": "finding"}}
    When the request is sent
    Then the response status is 404 Not Found: The requested finding cannot be found.

  @replay-only @team:DataDog/cloud-security-posture-management
  Scenario: Mute or unmute a batch of findings returns "OK" response
    Given operation "MuteFindings" enabled
    And new "MuteFindings" request
    And body with value {"data": {"attributes": {"mute": {"expiration_date": 1778721573794, "muted": true, "reason": "ACCEPTED_RISK"}}, "id": "dbe5f567-192b-4404-b908-29b70e1c9f76", "meta": {"findings":[{"finding_id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw=="}]}, "type": "finding"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Update a cloud configuration rule's details returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "cloud_configuration_rule" in the system
    And request contains "rule_id" parameter from "cloud_configuration_rule.id"
    And body with value {"name":"{{ unique }}_cloud_updated","isEnabled":false,"cases":[{"status":"info","notifications":[]}],"options":{"complianceRuleOptions":{"resourceType":"gcp_compute_disk", "regoRule":{"policy":"package datadog\n\nimport data.datadog.output as dd_output\n\nimport future.keywords.contains\nimport future.keywords.if\nimport future.keywords.in\n\nmilliseconds_in_a_day := ((1000 * 60) * 60) * 24\n\neval(iam_service_account_key) = \"skip\" if {\n\tiam_service_account_key.disabled\n} else = \"pass\" if {\n\t(iam_service_account_key.resource_seen_at / milliseconds_in_a_day) - (iam_service_account_key.valid_after_time / milliseconds_in_a_day) <= 90\n} else = \"fail\"\n\n# This part remains unchanged for all rules\nresults contains result if {\n\tsome resource in input.resources[input.main_resource_type]\n\tresult := dd_output.format(resource, eval(resource))\n}\n","resourceTypes":["gcp_compute_disk"]}}},"message":"ddd","tags":[],"complianceSignalOptions":{"userActivationStatus":false,"userGroupByFields":[]}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud_updated"
    And the response "id" has the same value as "cloud_configuration_rule.id"

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
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.filtered_data_type" is equal to "logs"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule Bad","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "abcde-12345"
    And body with value {"name": "{{ unique }}-NotFound","queries": [{"query": "@test:true","aggregation": "count","groupByFields": [],"distinctFields": [],"metrics": []}],"filters": [],"cases": [{"name": "", "status": "info", "condition": "a > 0", "notifications": []}], "options": {"evaluationWindow": 900, "keepAlive": 3600, "maxSignalDuration": 86400}, "message": "Test rule", "tags": [], "isEnabled": true}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    And body with value {"name": "{{ unique }}-Updated","queries": [{"query": "@test:true","aggregation": "count","groupByFields": [],"distinctFields": [],"metrics": []}],"filters": [],"cases": [{"name": "", "status": "info", "condition": "a > 0", "notifications": []}], "options": {"evaluationWindow": 900, "keepAlive": 3600, "maxSignalDuration": 86400}, "message": "Test rule", "tags": [], "isEnabled": true}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}-Updated"
    And the response "id" has the same value as "security_rule.id"
