@endpoint(rum-replay-sessions) @endpoint(rum-replay-sessions-v2)
Feature: Rum Replay Sessions
  Retrieve segments for RUM replay sessions. Access session replay data
  stored in event platform or blob storage.

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Get segments returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplaySessions" API
    And new "GetSegments" request
    And request contains "view_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
