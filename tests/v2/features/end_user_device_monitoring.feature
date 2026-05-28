@endpoint(end-user-device-monitoring) @endpoint(end-user-device-monitoring-v2)
Feature: End User Device Monitoring
  Inspect devices reported by the Datadog Agent on end-user laptops,
  desktops, and mobile devices, including their health, hardware, and
  connectivity attributes.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EndUserDeviceMonitoring" API

  @generated @skip @team:DataDog/windows-products
  Scenario: Get a device returns "Not Found" response
    Given new "GetEUDMDevice" request
    And request contains "device_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/windows-products
  Scenario: Get a device returns "OK" response
    Given new "GetEUDMDevice" request
    And request contains "device_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/windows-products
  Scenario: Get all device issue definitions returns "OK" response
    Given new "GetEUDMIssues" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/windows-products
  Scenario: Get all devices returns "OK" response
    Given new "GetEUDMDevices" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/windows-products
  Scenario: Get device counts grouped by attribute returns "OK" response
    Given new "GetEUDMGraph" request
    And request contains "by" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/windows-products
  Scenario: Get overview tiles returns "OK" response
    Given new "GetEUDMOverview" request
    When the request is sent
    Then the response status is 200 OK
