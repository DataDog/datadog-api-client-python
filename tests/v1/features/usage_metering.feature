@endpoint(usage-metering)
Feature: Usage Metering
  The usage metering API allows you to get hourly, daily, and monthly usage
  across multiple facets of Datadog. This API is available to all Pro and
  Enterprise customers. Usage is only accessible for [parent-level organizat
  ions](https://docs.datadoghq.com/account_management/multi_organization/).
  **Note**: Usage data is delayed by up to 72 hours from when it was
  incurred. It is retained for the past 15 months.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "UsageMetering" API

  @generated @skip
  Scenario: Get hourly usage for analyzed logs returns "OK" response
    Given new "GetUsageAnalyzedLogs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Lambda returns "OK" response
    Given new "GetUsageLambda" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Fargate returns "OK" response
    Given new "GetUsageFargate" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for hosts and containers returns "OK" response
    Given new "GetUsageHosts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Logs returns "OK" response
    Given new "GetUsageLogs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Logs by Index returns "OK" response
    Given new "GetUsageLogsByIndex" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Network Flows returns "OK" response
    Given new "GetUsageNetworkFlows" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Network Hosts returns "OK" response
    Given new "GetUsageNetworkHosts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for RUM Sessions returns "OK" response
    Given new "GetUsageRumSessions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for SNMP devices returns "OK" response
    Given new "GetUsageSNMP" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get usage across your multi-org account returns "OK" response
    Given new "GetUsageSummary" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Synthetics Checks returns "OK" response
    Given new "GetUsageSynthetics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Synthetics API Checks returns "OK" response
    Given new "GetUsageSyntheticsAPI" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Synthetics Browser Checks returns "OK" response
    Given new "GetUsageSyntheticsBrowser" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for custom metrics returns "OK" response
    Given new "GetUsageTimeseries" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the list of available daily custom reports returns "OK" response
    Given operation "GetDailyCustomReports" enabled
    And new "GetDailyCustomReports" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get specified daily custom reports returns "OK" response
    Given operation "GetSpecifiedDailyCustomReports" enabled
    And new "GetSpecifiedDailyCustomReports" request
    And request contains "report_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the list of available monthly custom reports returns "OK" response
    Given operation "GetMonthlyCustomReports" enabled
    And new "GetMonthlyCustomReports" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get specified monthly custom reports returns "OK" response
    Given operation "GetSpecifiedMonthlyCustomReports" enabled
    And new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for profiled hosts returns "OK" response
    Given new "GetUsageProfiling" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for Trace Search returns "OK" response
    Given new "GetUsageTrace" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for tracing without limits returns "OK" response
    Given new "GetTracingWithoutLimits" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get Usage Attribution returns "OK" response
    Given operation "GetUsageAttribution" enabled
    And new "GetUsageAttribution" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get billable usage across your account returns "OK" response
    Given new "GetUsageBillableSummary" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for incident management returns "OK" response
    Given new "GetIncidentManagement" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for indexed spans returns "OK" response
    Given new "GetUsageIndexedSpans" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get hourly usage for ingested spans returns "OK" response
    Given new "GetIngestedSpans" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get top custom metrics by hourly average returns "OK" response
    Given new "GetUsageTopAvgMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get specified daily custom reports returns "Not Found" response
    Given operation "GetSpecifiedDailyCustomReports" enabled
    And new "GetSpecifiedDailyCustomReports" request
    And request contains "report_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get specified monthly custom reports returns "Bad Request" response
    Given operation "GetSpecifiedMonthlyCustomReports" enabled
    And new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get specified monthly custom reports returns "Not Found" response
    Given operation "GetSpecifiedMonthlyCustomReports" enabled
    And new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get hourly usage for analyzed logs returns "Bad Request" response
    Given new "GetUsageAnalyzedLogs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Lambda returns "Bad Request" response
    Given new "GetUsageLambda" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get billable usage across your account returns "Bad Request" response
    Given new "GetUsageBillableSummary" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Fargate returns "Bad Request" response
    Given new "GetUsageFargate" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for hosts and containers returns "Bad Request" response
    Given new "GetUsageHosts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for incident management returns "Bad Request" response
    Given new "GetIncidentManagement" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for indexed spans returns "Bad Request" response
    Given new "GetUsageIndexedSpans" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for ingested spans returns "Bad Request" response
    Given new "GetIngestedSpans" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Logs returns "Bad Request" response
    Given new "GetUsageLogs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Logs by Index returns "Bad Request" response
    Given new "GetUsageLogsByIndex" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Network Flows returns "Bad Request" response
    Given new "GetUsageNetworkFlows" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Network Hosts returns "Bad Request" response
    Given new "GetUsageNetworkHosts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for profiled hosts returns "Bad Request" response
    Given new "GetUsageProfiling" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for RUM Sessions returns "Bad Request" response
    Given new "GetUsageRumSessions" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for SNMP devices returns "Bad Request" response
    Given new "GetUsageSNMP" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get usage across your multi-org account returns "Bad Request" response
    Given new "GetUsageSummary" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Synthetics Checks returns "Bad Request" response
    Given new "GetUsageSynthetics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Synthetics API Checks returns "Bad Request" response
    Given new "GetUsageSyntheticsAPI" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Synthetics Browser Checks returns "Bad Request" response
    Given new "GetUsageSyntheticsBrowser" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for custom metrics returns "Bad Request" response
    Given new "GetUsageTimeseries" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get top custom metrics by hourly average returns "Bad Request" response
    Given new "GetUsageTopAvgMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for Trace Search returns "Bad Request" response
    Given new "GetUsageTrace" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get hourly usage for tracing without limits returns "Bad Request" response
    Given new "GetTracingWithoutLimits" request
    When the request is sent
    Then the response status is 400 Bad Request
