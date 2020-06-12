Feature: Get a list of IP prefixes belonging to Datadog.

    Scenario: List IP Ranges
        Given an instance of "IPRanges" API
        When I call "GetIPRanges" endpoint
        Then I should get an instance of "IPRanges"
