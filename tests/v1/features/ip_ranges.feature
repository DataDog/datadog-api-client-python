@v1 @endpoint(ip-ranges)
Feature: IP Ranges
  Get a list of IP prefixes belonging to Datadog.

  Background:
    Given an instance of "IPRanges" API

  Scenario: List IP Ranges
    Given new "GetIPRanges" request
    When the request is sent
    Then the response status is 200 List of IP ranges.
