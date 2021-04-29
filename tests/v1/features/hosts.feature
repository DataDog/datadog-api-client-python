@endpoint(hosts)
Feature: Hosts
  Get information about your live hosts in Datadog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Hosts" API

  @generated @skip
  Scenario: Get all hosts for your organization returns "Invalid Parameter Error" response
    Given new "ListHosts" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip
  Scenario: Get all hosts for your organization returns "OK" response
    Given new "ListHosts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the total number of active hosts returns "Invalid Parameter Error" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip
  Scenario: Get the total number of active hosts returns "OK" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Mute a host returns "Invalid Parameter Error" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "<PATH>"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip
  Scenario: Mute a host returns "OK" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "<PATH>"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Unmute a host returns "Invalid Parameter Error" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip
  Scenario: Unmute a host returns "OK" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK
