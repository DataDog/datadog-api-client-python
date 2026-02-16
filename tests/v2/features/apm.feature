@endpoint(apm) @endpoint(apm-v2)
Feature: APM
  Observe, troubleshoot, and improve cloud-scale applications with all
  telemetry in context

  @generated @skip @team:DataDog/apm-aoe
  Scenario: Get service list returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "APM" API
    And new "GetServiceList" request
    And request contains "filter[env]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
