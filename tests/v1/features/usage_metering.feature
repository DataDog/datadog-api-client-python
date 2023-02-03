@endpoint(usage-metering) @endpoint(usage-metering-v1)
Feature: Usage Metering
  The usage metering API allows you to get hourly, daily, and monthly usage
  across multiple facets of Datadog. This API is available to all Pro and
  Enterprise customers. Usage is only accessible for [parent-level organizat
  ions](https://docs.datadoghq.com/account_management/multi_organization/).
  **Note**: Usage data is delayed by up to 72 hours from when it was
  incurred. It is retained for 15 months.  You can retrieve up to 24 hours
  of hourly usage data for multiple organizations, and up to two months of
  hourly usage data for a single organization in one request.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "UsageMetering" API

  @team:DataDog/red-zone-revenue-query
  Scenario: Get all custom metrics by hourly average returns "Bad Request" response
    Given new "GetUsageTopAvgMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get all custom metrics by hourly average returns "OK" response
    Given new "GetUsageTopAvgMetrics" request
    And request contains "day" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get billable usage across your account returns "Bad Request" response
    Given new "GetUsageBillableSummary" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get billable usage across your account returns "OK" response
    Given new "GetUsageBillableSummary" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly logs usage by retention returns "Bad Request" response
    Given new "GetUsageLogsByRetention" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly logs usage by retention returns "OK" response
    Given new "GetUsageLogsByRetention" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage attribution returns "Bad Request" response
    Given new "GetHourlyUsageAttribution" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "usage_type" parameter with value "not_a_product"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage attribution returns "OK" response
    Given new "GetHourlyUsageAttribution" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "usage_type" parameter with value "infra_host_usage"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CI Visibility returns "Bad Request" response
    Given new "GetUsageCIApp" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CI Visibility returns "OK" response
    Given new "GetUsageCIApp" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CI visibility returns "Bad Request" response
    Given new "GetUsageCIApp" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CI visibility returns "OK" response
    Given new "GetUsageCIApp" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CSPM returns "Bad Request" response
    Given new "GetUsageCloudSecurityPostureManagement" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for CSPM returns "OK" response
    Given new "GetUsageCloudSecurityPostureManagement" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Cloud Workload Security returns "OK" response
    Given new "GetUsageCWS" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Database Monitoring returns "OK" response
    Given new "GetUsageDBM" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Fargate returns "Bad Request" response
    Given new "GetUsageFargate" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Fargate returns "OK" response
    Given new "GetUsageFargate" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for IoT returns "Bad Request" response
    Given new "GetUsageInternetOfThings" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for IoT returns "OK" response
    Given new "GetUsageInternetOfThings" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Lambda returns "Bad Request" response
    Given new "GetUsageLambda" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Lambda returns "OK" response
    Given new "GetUsageLambda" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Logs by Index returns "Bad Request" response
    Given new "GetUsageLogsByIndex" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Logs by Index returns "OK" response
    Given new "GetUsageLogsByIndex" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Logs returns "Bad Request" response
    Given new "GetUsageLogs" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Logs returns "OK" response
    Given new "GetUsageLogs" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Network Flows returns "Bad Request" response
    Given new "GetUsageNetworkFlows" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Network Flows returns "OK" response
    Given new "GetUsageNetworkFlows" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Network Hosts returns "Bad Request" response
    Given new "GetUsageNetworkHosts" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Network Hosts returns "OK" response
    Given new "GetUsageNetworkHosts" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Online Archive returns "Bad Request" response
    Given new "GetUsageOnlineArchive" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Online Archive returns "OK" response
    Given new "GetUsageOnlineArchive" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM Sessions returns "Bad Request" response
    Given new "GetUsageRumSessions" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM Sessions returns "OK" response
    Given new "GetUsageRumSessions" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM Units returns "OK" response
    Given new "GetUsageRumUnits" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM sessions returns "Bad Request" response
    Given new "GetUsageRumSessions" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM sessions returns "OK" response
    Given new "GetUsageRumSessions" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM units returns "Bad Request" response
    Given new "GetUsageRumUnits" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for RUM units returns "OK" response
    Given new "GetUsageRumUnits" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for SNMP devices returns "Bad Request" response
    Given new "GetUsageSNMP" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for SNMP devices returns "OK" response
    Given new "GetUsageSNMP" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Sensitive Data Scanner returns "OK" response
    Given new "GetUsageSDS" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Synthetics API Checks returns "Bad Request" response
    Given new "GetUsageSyntheticsAPI" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Synthetics API Checks returns "OK" response
    Given new "GetUsageSyntheticsAPI" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Synthetics Browser Checks returns "Bad Request" response
    Given new "GetUsageSyntheticsBrowser" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Synthetics Browser Checks returns "OK" response
    Given new "GetUsageSyntheticsBrowser" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for analyzed logs returns "Bad Request" response
    Given new "GetUsageAnalyzedLogs" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for analyzed logs returns "OK" response
    Given new "GetUsageAnalyzedLogs" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for audit logs returns "Bad Request" response
    Given new "GetUsageAuditLogs" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for audit logs returns "OK" response
    Given new "GetUsageAuditLogs" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for cloud workload security returns "Bad Request" response
    Given new "GetUsageCWS" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for cloud workload security returns "OK" response
    Given new "GetUsageCWS" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for custom metrics returns "Bad Request" response
    Given new "GetUsageTimeseries" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for custom metrics returns "OK" response
    Given new "GetUsageTimeseries" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for database monitoring returns "Bad Request" response
    Given new "GetUsageDBM" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for database monitoring returns "OK" response
    Given new "GetUsageDBM" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for hosts and containers returns "Bad Request" response
    Given new "GetUsageHosts" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for hosts and containers returns "OK" response
    Given new "GetUsageHosts" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for incident management returns "Bad Request" response
    Given new "GetIncidentManagement" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for incident management returns "OK" response
    Given new "GetIncidentManagement" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for indexed spans returns "Bad Request" response
    Given new "GetUsageIndexedSpans" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for indexed spans returns "OK" response
    Given new "GetUsageIndexedSpans" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for ingested spans returns "Bad Request" response
    Given new "GetIngestedSpans" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for ingested spans returns "OK" response
    Given new "GetIngestedSpans" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for lambda returns "Bad Request" response
    Given new "GetUsageLambda" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for lambda returns "OK" response
    Given new "GetUsageLambda" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for logs by index returns "Bad Request" response
    Given new "GetUsageLogsByIndex" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for logs by index returns "OK" response
    Given new "GetUsageLogsByIndex" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for logs returns "Bad Request" response
    Given new "GetUsageLogs" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for logs returns "OK" response
    Given new "GetUsageLogs" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for network hosts returns "Bad Request" response
    Given new "GetUsageNetworkHosts" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for network hosts returns "OK" response
    Given new "GetUsageNetworkHosts" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for online archive returns "Bad Request" response
    Given new "GetUsageOnlineArchive" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for online archive returns "OK" response
    Given new "GetUsageOnlineArchive" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for profiled hosts returns "Bad Request" response
    Given new "GetUsageProfiling" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for profiled hosts returns "OK" response
    Given new "GetUsageProfiling" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for sensitive data scanner returns "Bad Request" response
    Given new "GetUsageSDS" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for sensitive data scanner returns "OK" response
    Given new "GetUsageSDS" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics API checks returns "Bad Request" response
    Given new "GetUsageSyntheticsAPI" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics API checks returns "OK" response
    Given new "GetUsageSyntheticsAPI" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics browser checks returns "Bad Request" response
    Given new "GetUsageSyntheticsBrowser" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics browser checks returns "OK" response
    Given new "GetUsageSyntheticsBrowser" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics checks returns "Bad Request" response
    Given new "GetUsageSynthetics" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for synthetics checks returns "OK" response
    Given new "GetUsageSynthetics" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get mobile hourly usage for RUM Sessions returns "OK" response
    Given new "GetUsageRumSessions" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "type" parameter with value "mobile"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get monthly usage attribution returns "Bad Request" response
    Given new "GetMonthlyUsageAttribution" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "not_a_product"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get monthly usage attribution returns "OK" response
    Given new "GetMonthlyUsageAttribution" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "infra_host_usage"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get specified daily custom reports returns "Not Found" response
    Given new "GetSpecifiedDailyCustomReports" request
    And request contains "report_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get specified daily custom reports returns "OK" response
    Given new "GetSpecifiedDailyCustomReports" request
    And request contains "report_id" parameter with value "2022-03-20"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get specified monthly custom reports returns "Bad Request" response
    Given new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get specified monthly custom reports returns "Not Found" response
    Given new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get specified monthly custom reports returns "OK" response
    Given new "GetSpecifiedMonthlyCustomReports" request
    And request contains "report_id" parameter with value "2021-05-01"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get the list of available daily custom reports returns "OK" response
    Given new "GetDailyCustomReports" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get the list of available monthly custom reports returns "OK" response
    Given new "GetMonthlyCustomReports" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get usage across your account returns "Bad Request" response
    Given new "GetUsageSummary" request
    And request contains "start_month" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get usage across your account returns "OK" response
    Given new "GetUsageSummary" request
    And request contains "start_month" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get usage attribution returns "OK" response
    Given new "GetUsageAttribution" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "*"
    And request contains "offset" parameter with value 0
    And request contains "limit" parameter with value 1
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/red-zone-revenue-query
  Scenario: Paginate monthly usage attribution
    Given there is a valid "monthly_usage_attribution" response
    And new "GetMonthlyUsageAttribution" request
    And request contains "next_record_id" parameter from "monthly_usage_attribution.metadata.pagination.next_record_id"
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "infra_host_usage"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: get hourly usage for network flows returns "Bad Request" response
    Given new "GetUsageNetworkFlows" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: get hourly usage for network flows returns "OK" response
    Given new "GetUsageNetworkFlows" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
