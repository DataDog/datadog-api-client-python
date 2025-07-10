@endpoint(security-monitoring) @endpoint(security-monitoring-v2)
Feature: Security Monitoring
  Create and manage your security rules, signals, filters, and more. See the
  [Datadog Security page](https://docs.datadoghq.com/security/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  @team:DataDog/k9-cloud-security-platform
  Scenario: Cancel a historical job returns "Bad Request" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Cancel a historical job returns "Conflict" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform
  Scenario: Cancel a historical job returns "Not Found" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Cancel a historical job returns "OK" response
    Given operation "CancelHistoricalJob" enabled
    And operation "RunHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And there is a valid "historical_job" in the system
    And request contains "job_id" parameter from "historical_job.data.id"
    When the request is sent
    Then the response status is 204 No Content

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

  @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a job result to a signal returns "Bad Request" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a job result to a signal returns "Not Found" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a job result to a signal returns "OK" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 204 OK

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a rule from JSON to Terraform returns "Bad Request" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a rule from JSON to Terraform returns "Not Found" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Convert a rule from JSON to Terraform returns "OK" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 200 OK
    And the response "terraformContent" is equal to "resource \"datadog_security_monitoring_rule\" \"{{ unique_lower }}\" {\n\tname = \"{{ unique }}\"\n\tenabled = true\n\tquery {\n\t\tquery = \"@test:true\"\n\t\tgroup_by_fields = []\n\t\tdistinct_fields = []\n\t\taggregation = \"count\"\n\t\tname = \"\"\n\t\tdata_source = \"logs\"\n\t}\n\toptions {\n\t\tkeep_alive = 3600\n\t\tmax_signal_duration = 86400\n\t\tdetection_method = \"threshold\"\n\t\tevaluation_window = 900\n\t}\n\tcase {\n\t\tname = \"\"\n\t\tstatus = \"info\"\n\t\tnotifications = []\n\t\tcondition = \"a > 0\"\n\t}\n\tmessage = \"Test rule\"\n\ttags = []\n\thas_extended_title = false\n\ttype = \"log_detection\"\n}\n"

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert an existing rule from JSON to Terraform returns "Bad Request" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Convert an existing rule from JSON to Terraform returns "Not Found" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Convert an existing rule from JSON to Terraform returns "OK" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "terraformContent" is equal to "resource \"datadog_security_monitoring_rule\" \"{{ unique_lower }}\" {\n\tname = \"{{ unique }}\"\n\tenabled = true\n\tquery {\n\t\tquery = \"@test:true\"\n\t\tgroup_by_fields = []\n\t\tdistinct_fields = []\n\t\taggregation = \"count\"\n\t\tname = \"\"\n\t\tdata_source = \"logs\"\n\t}\n\toptions {\n\t\tkeep_alive = 3600\n\t\tmax_signal_duration = 86400\n\t\tdetection_method = \"threshold\"\n\t\tevaluation_window = 900\n\t}\n\tcase {\n\t\tname = \"\"\n\t\tstatus = \"info\"\n\t\tnotifications = []\n\t\tcondition = \"a > 0\"\n\t}\n\tmessage = \"Test rule\"\n\ttags = []\n\thas_extended_title = false\n\ttype = \"log_detection\"\n}\n"

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
  Scenario: Create a custom framework returns "Bad Request" response
    Given new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:DataDog/k9-cloud-security-platform
  Scenario: Create a custom framework returns "Conflict" response
    Given there is a valid "custom_framework" in the system
    And new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @replay-only @skip-terraform-config @team:DataDog/k9-cloud-security-platform
  Scenario: Create a custom framework returns "OK" response
    Given new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection", "referenceTables":[{"tableName": "synthetics_test_reference_table_dont_delete", "columnName": "value", "logFieldPath":"testtag", "checkPresence":true, "ruleQueryName":"a"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "Test rule"
    And the response "referenceTables" is equal to [{"tableName": "synthetics_test_reference_table_dont_delete", "columnName": "value", "logFieldPath":"testtag", "checkPresence":true, "ruleQueryName":"a"}]

  @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with detection method 'third_party' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"thirdPartyCases":[{"query":"status:error","name":"high","status":"high"},{"query":"status:info","name":"low","status":"low"}],"queries":[],"cases":[],"message":"This is a third party rule","options":{"detectionMethod":"third_party","keepAlive":0,"maxSignalDuration":600,"thirdPartyRuleOptions":{"defaultStatus":"info","rootQueries":[{"query":"source:guardduty @details.alertType:*EC2*", "groupByFields":["instance-id"]},{"query":"source:guardduty", "groupByFields":[]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "third_party"
    And the response "thirdPartyCases[0].query" is equal to "status:error"

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a detection rule with type 'application_security 'returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"type":"application_security","name":"{{unique}}_appsec_rule","queries":[{"query":"@appsec.security_activity:business_logic.users.login.failure","aggregation":"count","groupByFields":["service","@http.client_ip"],"distinctFields":[]}],"filters":[],"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 100000","actions":[{"type":"block_ip","options":{"duration":900}}, {"type":"user_behavior","options":{"userBehaviorName":"behavior"}}]}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900,"detectionMethod":"threshold"},"isEnabled":true,"message":"Test rule","tags":[],"groupSignalsBy":["service"]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_appsec_rule"
    And the response "type" is equal to "application_security"
    And the response "message" is equal to "Test rule"

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

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Create a new signal-based notification rule returns "Bad Request" response
    Given new "CreateSignalNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Create a new signal-based notification rule returns "Successfully created the notification rule." response
    Given new "CreateSignalNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the notification rule.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Create a new vulnerability-based notification rule returns "Bad Request" response
    Given new "CreateVulnerabilityNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Create a new vulnerability-based notification rule returns "Successfully created the notification rule." response
    Given new "CreateVulnerabilityNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the notification rule.

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

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Create a suppression rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Create a suppression rule returns "Conflict" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a suppression rule returns "OK" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "start_date": {{ timestamp('now + 10d') }}000, "expiration_date": {{ timestamp('now + 21d') }}000, "name": "{{ unique }}", "rule_query": "type:log_detection source:cloudtrail", "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.rule_query" is equal to "type:log_detection source:cloudtrail"

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Create a suppression rule with an exclusion query returns "OK" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "start_date": {{ timestamp('now + 10d') }}000, "expiration_date": {{ timestamp('now + 21d') }}000, "name": "{{ unique }}", "rule_query": "type:log_detection source:cloudtrail", "data_exclusion_query": "account_id:12345"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.rule_query" is equal to "type:log_detection source:cloudtrail"
    And the response "data.attributes.data_exclusion_query" is equal to "account_id:12345"

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a custom framework returns "Bad Request" response
    Given new "DeleteCustomFramework" request
    And request contains "handle" parameter with value "handle-does-not-exist"
    And request contains "version" parameter with value "version-does-not-exist"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "DeleteCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a non existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "ThisRuleIdProbablyDoesntExist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
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

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a signal-based notification rule returns "Not Found" response
    Given new "DeleteSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a signal-based notification rule returns "Rule successfully deleted." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "DeleteSignalNotificationRule" request
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a suppression rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter with value "does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a suppression rule returns "OK" response
    Given there is a valid "suppression" in the system
    And new "DeleteSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a vulnerability-based notification rule returns "Not Found" response
    Given new "DeleteVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a vulnerability-based notification rule returns "Rule successfully deleted." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "DeleteVulnerabilityNotificationRule" request
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing job returns "Bad Request" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing job returns "Conflict" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing job returns "Not Found" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete an existing job returns "OK" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
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

  @generated @skip @team:DataDog/asm-vm
  Scenario: Get SBOM returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "GetSBOM" enabled
    And new "GetSBOM" request
    And request contains "asset_type" parameter from "REPLACE.ME"
    And request contains "filter[asset_name]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @team:DataDog/asm-vm
  Scenario: Get SBOM returns "Not found: asset not found" response
    Given operation "GetSBOM" enabled
    And new "GetSBOM" request
    And request contains "asset_type" parameter with value "Host"
    And request contains "filter[asset_name]" parameter with value "unknown-host"
    When the request is sent
    Then the response status is 404 Not found: asset not found

  @skip @team:DataDog/asm-vm
  Scenario: Get SBOM returns "OK" response
    Given operation "GetSBOM" enabled
    And new "GetSBOM" request
    And request contains "asset_type" parameter with value "Repository"
    And request contains "filter[asset_name]" parameter with value "github.com/datadog/datadog-agent"
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Get a cloud configuration rule's details returns "OK" response
    Given there is a valid "cloud_configuration_rule" in the system
    And new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "cloud_configuration_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud"
    And the response "id" has the same value as "cloud_configuration_rule.id"

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a custom framework returns "Bad Request" response
    Given new "GetCustomFramework" request
    And request contains "handle" parameter with value "frame-does-not-exist"
    And request contains "version" parameter with value "frame-does-not-exist"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Get a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "GetCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    When the request is sent
    Then the response status is 200 OK

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

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a job's details returns "Bad Request" response
    Given operation "GetHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a job's details returns "Not Found" response
    Given operation "GetHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get a job's details returns "OK" response
    Given operation "GetHistoricalJob" enabled
    And operation "RunHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And there is a valid "historical_job" in the system
    And request contains "job_id" parameter from "historical_job.data.id"
    When the request is sent
    Then the response status is 200 OK

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
  Scenario: Get a rule's version history returns "Bad Request" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's version history returns "Not Found" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get a rule's version history returns "OK" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
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

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Get a suppression rule returns "Not Found" response
    Given new "GetSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter with value "this-does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Get a suppression rule returns "OK" response
    Given new "GetSecurityMonitoringSuppression" request
    And there is a valid "suppression" in the system
    And request contains "suppression_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.rule_query" has the same value as "suppression.data.attributes.rule_query"
    And the response "data.attributes.suppression_query" is equal to "env:test"

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get all security filters returns "OK" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.filtered_data_type" with value "logs"
    And the response "data" has item with field "attributes.is_builtin" with value true

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Get all suppression rules returns "OK" response
    Given new "ListSecurityMonitoringSuppressions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Bad Request" response
    Given new "GetSignalNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Not Found" response
    Given new "GetSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Notification rule details." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "GetSignalNotificationRule" request
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 Notification rule details.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Bad Request" response
    Given new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Not Found" response
    Given new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Notification rule details." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 Notification rule details.

  @skip-go @skip-java @skip-ruby @team:DataDog/k9-cloud-security-platform
  Scenario: Get rule version history returns "OK" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "security_rule.id"
    And the response "data.type" is equal to "GetRuleVersionHistoryResponse"
    And the response "data.attributes.count" is equal to 1
    And the response "data.attributes.data[1].rule.name" has the same value as "security_rule.name"

  @team:DataDog/cloud-security-posture-management
  Scenario: Get the list of signal-based notification rules returns "The list of notification rules." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "GetSignalNotificationRules" request
    When the request is sent
    Then the response status is 200 The list of notification rules.

  @team:DataDog/cloud-security-posture-management
  Scenario: Get the list of vulnerability notification rules returns "The list of notification rules." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "GetVulnerabilityNotificationRules" request
    When the request is sent
    Then the response status is 200 The list of notification rules.

  @generated @skip @team:DataDog/asm-vm
  Scenario: List assets SBOMs returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListAssetsSBOMs" enabled
    And new "ListAssetsSBOMs" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @team:DataDog/asm-vm
  Scenario: List assets SBOMs returns "Not found: There is no request associated with the provided token." response
    Given operation "ListAssetsSBOMs" enabled
    And new "ListAssetsSBOMs" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 404 Not found: There is no request associated with the provided token.

  @generated @skip @team:DataDog/asm-vm
  Scenario: List assets SBOMs returns "Not found: asset not found" response
    Given operation "ListAssetsSBOMs" enabled
    And new "ListAssetsSBOMs" request
    When the request is sent
    Then the response status is 404 Not found: asset not found

  @team:DataDog/asm-vm
  Scenario: List assets SBOMs returns "OK" response
    Given operation "ListAssetsSBOMs" enabled
    And new "ListAssetsSBOMs" request
    And request contains "filter[package_name]" parameter with value "pandas"
    And request contains "filter[asset_type]" parameter with value "Service"
    When the request is sent
    Then the response status is 200 OK

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

  @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "OK" response with details
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    And request contains "detailed_findings" parameter with value true
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management @with-pagination
  Scenario: List findings returns "OK" response with pagination
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/cloud-security-posture-management
  Scenario: List findings with detection_type query param returns "OK" response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    And request contains "filter[vulnerability_type]" parameter with value ["misconfiguration", "attack_path"]
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: List historical jobs returns "Bad Request" response
    Given operation "ListHistoricalJobs" enabled
    And new "ListHistoricalJobs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: List historical jobs returns "OK" response
    Given operation "ListHistoricalJobs" enabled
    And operation "RunHistoricalJob" enabled
    And new "ListHistoricalJobs" request
    And there is a valid "historical_job" in the system
    And request contains "filter[query]" parameter with value "id:{{historical_job.data.id}}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: List resource filters returns "Bad Request" response
    Given new "GetResourceEvaluationFilters" request
    And request contains "account_id" parameter with value "123456789"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: List resource filters returns "OK" response
    Given new "GetResourceEvaluationFilters" request
    And request contains "cloud_provider" parameter with value "aws"
    And request contains "account_id" parameter with value "123456789"
    When the request is sent
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

  @generated @skip @team:DataDog/asm-vm
  Scenario: List vulnerabilities returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @team:DataDog/asm-vm
  Scenario: List vulnerabilities returns "Not found: There is no request associated with the provided token." response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 404 Not found: There is no request associated with the provided token.

  @team:DataDog/asm-vm
  Scenario: List vulnerabilities returns "OK" response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    And request contains "filter[cvss.base.severity]" parameter with value "High"
    And request contains "filter[asset.type]" parameter with value "Service"
    And request contains "filter[tool]" parameter with value "Infra"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/asm-vm
  Scenario: List vulnerable assets returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @team:DataDog/asm-vm
  Scenario: List vulnerable assets returns "Not found: There is no request associated with the provided token." response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 404 Not found: There is no request associated with the provided token.

  @team:DataDog/asm-vm
  Scenario: List vulnerable assets returns "OK" response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    And request contains "filter[type]" parameter with value "Host"
    And request contains "filter[repository_url]" parameter with value "github.com/datadog/dd-go"
    And request contains "filter[risks.in_production]" parameter with value true
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

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Bad Request" response
    Given new "PatchSignalNotificationRule" request
    And there is a valid "valid_signal_notification_rule" in the system
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Not Found" response
    Given new "PatchSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Notification rule successfully patched." response
    Given new "PatchSignalNotificationRule" request
    And there is a valid "valid_signal_notification_rule" in the system
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 200 Notification rule successfully patched.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "The server cannot process the request because it contains invalid data." response
    Given new "PatchSignalNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Bad Request" response
    Given new "PatchVulnerabilityNotificationRule" request
    And there is a valid "valid_vulnerability_notification_rule" in the system
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Not Found" response
    Given new "PatchVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Notification rule successfully patched." response
    Given new "PatchVulnerabilityNotificationRule" request
    And there is a valid "valid_vulnerability_notification_rule" in the system
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 200 Notification rule successfully patched.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "The server cannot process the request because it contains invalid data." response
    Given new "PatchVulnerabilityNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @team:DataDog/k9-cloud-security-platform
  Scenario: Run a historical job returns "Bad Request" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data":{"type":"historicalDetectionsJobCreate","attributes":{"jobDefinition":{"type":"log_detection","name":"Excessive number of failed attempts.","queries":[{"query":"source:non_existing_src_weekend","aggregation":"count","groupByFields":[],"distinctFields":[]}],"cases":[{"name":"Condition 1","status":"info","notifications":[],"condition":"a > 1"}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900},"message":"A large number of failed login attempts.","tags":[],"from":1730387522611,"to":1730391122611,"index":"non_existing_index"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Run a historical job returns "Not Found" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data": { "type": "historicalDetectionsJobCreate", "attributes": {"fromRule": {"from": 1730201035064, "id": "non-existng", "index": "main", "notifications": [], "to": 1730204635115}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Run a historical job returns "Status created" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data":{"type":"historicalDetectionsJobCreate","attributes":{"jobDefinition":{"type":"log_detection","name":"Excessive number of failed attempts.","queries":[{"query":"source:non_existing_src_weekend","aggregation":"count","groupByFields":[],"distinctFields":[]}],"cases":[{"name":"Condition 1","status":"info","notifications":[],"condition":"a > 1"}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900},"message":"A large number of failed login attempts.","tags":[],"from":1730387522611,"to":1730387532611,"index":"main"}}}}
    When the request is sent
    Then the response status is 201 Status created

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Test a rule returns "Bad Request" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [], "filters": [{"action": "require"}], "hasExtendedTitle": true, "isEnabled": true, "message": "", "name": "My security monitoring rule.", "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}, "thirdPartyRuleOptions": {"defaultNotifications": [], "defaultStatus": "critical", "rootQueries": [{"groupByFields": [], "query": "source:cloudtrail"}]}}, "queries": [], "tags": ["env:prod", "team:security"], "thirdPartyCases": [], "type": "application_security"}, "ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Test a rule returns "Not Found" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [], "filters": [{"action": "require"}], "hasExtendedTitle": true, "isEnabled": true, "message": "", "name": "My security monitoring rule.", "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}, "thirdPartyRuleOptions": {"defaultNotifications": [], "defaultStatus": "critical", "rootQueries": [{"groupByFields": [], "query": "source:cloudtrail"}]}}, "queries": [], "tags": ["env:prod", "team:security"], "thirdPartyCases": [], "type": "application_security"}, "ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-go @skip-java @skip-ruby @skip-typescript @team:DataDog/k9-cloud-security-platform
  Scenario: Test a rule returns "OK" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [{"name": "","status": "info","notifications": [],"condition": "a > 0"}],"hasExtendedTitle": true,"isEnabled": true,"message": "My security monitoring rule message.","name": "My security monitoring rule.","options": {"decreaseCriticalityBasedOnEnv": false,"detectionMethod": "threshold","evaluationWindow": 0,"keepAlive": 0,"maxSignalDuration": 0},"queries": [{"query": "source:source_here","groupByFields": ["@userIdentity.assumed_role"],"distinctFields": [],"aggregation": "count","name": ""}],"tags": ["env:prod", "team:security"],"type": "log_detection"}, "ruleQueryPayloads": [{"expectedResult": true,"index": 0,"payload": {"ddsource": "source_here","ddtags": "env:staging,version:5.1","hostname": "i-012345678","message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World","service": "payment","userIdentity": {"assumed_role" : "fake assumed_role"}}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "results[0]" is equal to true

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Test an existing rule returns "Bad Request" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Test an existing rule returns "Not Found" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Test an existing rule returns "OK" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
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

  @team:DataDog/k9-cloud-security-platform
  Scenario: Update a custom framework returns "Bad Request" response
    Given new "UpdateCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    And body with value {"data": {"attributes": {"handle": "", "name": "", "requirements": [{"controls": [{"name": "", "rules_id": [""]}], "name": ""}], "version": ""}, "type": "custom_framework"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/k9-cloud-security-platform
  Scenario: Update a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "UpdateCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
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
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.filtered_data_type" is equal to "logs"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a suppression rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a suppression rule returns "Concurrent Modification" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Update a suppression rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Update a suppression rule returns "OK" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And there is a valid "suppression" in the system
    And request contains "suppression_id" parameter from "suppression.data.id"
    And body with value {"data": {"attributes": {"suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.suppression_query" is equal to "env:staging status:low"
    And the response "data.attributes.version" is equal to 2

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

  @team:DataDog/k9-cloud-security-platform
  Scenario: Update resource filters returns "Bad Request" response
    Given new "UpdateResourceEvaluationFilters" request
    And body with value {"data": {"attributes": {"cloud_provider": {"invalid": {"aws_account_id": ["tag1:v1"]}}}, "id": "csm_resource_filter", "type": "csm_resource_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Update resource filters returns "OK" response
    Given new "UpdateResourceEvaluationFilters" request
    And body with value {"data": {"attributes": {"cloud_provider": {"aws": {"aws_account_id": ["tag1:v1"]}}}, "id": "csm_resource_filter", "type": "csm_resource_filter"}}
    When the request is sent
    Then the response status is 201 OK

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-typescript @skip-validation @team:DataDog/k9-cloud-security-platform
  Scenario: Validate a detection rule returns "Bad Request" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0"}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":1800,"keepAlive":999999,"maxSignalDuration":1800,"detectionMethod":"threshold"},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"aggregation":"count","name":""}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Validate a detection rule returns "OK" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0"}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":1800,"keepAlive":1800,"maxSignalDuration":1800,"detectionMethod":"threshold"},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"aggregation":"count","name":""}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 204 OK
