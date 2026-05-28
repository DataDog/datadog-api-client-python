@endpoint(eudm) @endpoint(eudm-v2)
Feature: End User Device Monitoring
  Inspect devices reported by the Datadog Agent on end-user laptops, desktops,
  and mobile devices, including their health, hardware, and connectivity
  attributes.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EndUserDeviceMonitoring" API

  @team:DataDog/windows-products
  Scenario: Get a device returns "Not Found" response
    Given new "GetEUDMDevice" request
    And request contains "device_id" parameter with value "not_found"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/windows-products
  Scenario: Get all devices returns "OK" response
    Given new "GetEUDMDevices" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/windows-products
  Scenario: Get device counts grouped by attribute returns "OK" response
    Given new "GetEUDMGraph" request
    And request contains "by" parameter with value "os"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/windows-products
  Scenario: Get all device issue definitions returns "OK" response
    Given new "GetEUDMIssues" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/windows-products
  Scenario: Get overview tiles returns "OK" response
    Given new "GetEUDMOverview" request
    When the request is sent
    Then the response status is 200 OK
