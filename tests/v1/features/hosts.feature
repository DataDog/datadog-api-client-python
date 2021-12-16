@endpoint(hosts) @endpoint(hosts-v1)
Feature: Hosts
  Get information about your live hosts in Datadog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Hosts" API

  @generated @skip @team:DataDog/core-index
  Scenario: Get all hosts for your organization returns "Invalid Parameter Error" response
    Given new "ListHosts" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @integration-only @team:DataDog/core-index
  Scenario: Get all hosts for your organization returns "OK" response
    Given new "ListHosts" request
    And request contains "filter" parameter with value "env:ci"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Get the total number of active hosts returns "Invalid Parameter Error" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Get the total number of active hosts returns "OK" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Mute a host returns "Invalid Parameter Error" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Mute a host returns "OK" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Unmute a host returns "Invalid Parameter Error" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Unmute a host returns "OK" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
