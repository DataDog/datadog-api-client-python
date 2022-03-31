@endpoint(ip-ranges) @endpoint(ip-ranges-v1)
Feature: IP Ranges
  Get a list of IP prefixes belonging to Datadog.

  @team:DataDog/network-edge
  Scenario: List IP Ranges returns "OK" response
    Given an instance of "IPRanges" API
    And new "GetIPRanges" request
    When the request is sent
    Then the response status is 200 OK
