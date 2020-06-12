Feature: Monitors allow you to watch a metric or check that you care about, notifying your team when some defined threshold is exceeded.

    Background:
        Given a valid API key
        And a valid Application key

    Scenario: List Monitors
        Given an instance of "Monitors" API
        When I call "ListMonitors" endpoint
        Then I should get a list of "Monitor" objects
