@endpoint(processes)
Feature: Processes
  The processes API allows you to query processes data for your
  organization.

  Scenario: Get all processes returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Processes" API
    And new "ListProcesses" request
    And request contains "search" parameter with value "process-agent"
    And request contains "tags" parameter with value "testing:true"
    And request contains "page[limit]" parameter with value 2
    When the request is sent
    Then the response status is 200 OK
