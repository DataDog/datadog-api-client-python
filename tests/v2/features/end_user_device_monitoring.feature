@endpoint(end-user-device-monitoring) @endpoint(end-user-device-monitoring-v2)
Feature: End User Device Monitoring
  Inspect devices reported by the Datadog Agent on end-user laptops,
  desktops, and mobile devices, including their health, hardware, and
  connectivity attributes.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EndUserDeviceMonitoring" API

  @generated @skip @team:ddoghq/eudm-experiences
  Scenario: Get a device returns "Bad Request" response
    Given operation "GetEUDMDevice" enabled
    And new "GetEUDMDevice" request
    And request contains "device_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/eudm-experiences
  Scenario: Get a device returns "Not Found" response
    Given operation "GetEUDMDevice" enabled
    And new "GetEUDMDevice" request
    And request contains "device_id" parameter with value "not_found"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/eudm-experiences
  Scenario: Get a device returns "OK" response
    Given operation "GetEUDMDevice" enabled
    And new "GetEUDMDevice" request
    And request contains "device_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/eudm-experiences
  Scenario: Get all devices returns "Bad Request" response
    Given operation "GetEUDMDevices" enabled
    And new "GetEUDMDevices" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/eudm-experiences
  Scenario: Get all devices returns "OK" response
    Given operation "GetEUDMDevices" enabled
    And new "GetEUDMDevices" request
    When the request is sent
    Then the response status is 200 OK
