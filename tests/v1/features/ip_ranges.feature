Feature: IP Ranges
  Get a list of IP prefixes belonging to Datadog.

  Background:
    Given an instance of "IPRanges" API

  Scenario: List IP Ranges
    Given new "GetIPRanges" request
    When I execute the request
    Then the status is 200 List of IP ranges.
