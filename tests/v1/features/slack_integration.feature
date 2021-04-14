@endpoint(slack-integration)
Feature: Slack Integration
  Configure your [Datadog-Slack
  integration](https://docs.datadoghq.com/integrations/slack) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SlackIntegration" API
    And request contains "account_name" parameter from "<PATH>"

  @generated @skip
  Scenario: Create a Slack integration channel returns "Bad Request" response
    Given new "CreateSlackIntegrationChannel" request
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a Slack integration channel returns "Item Not Found" response
    Given new "CreateSlackIntegrationChannel" request
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Create a Slack integration channel returns "OK" response
    Given new "CreateSlackIntegrationChannel" request
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a Slack integration channel returns "Bad Request" response
    Given new "GetSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a Slack integration channel returns "Item Not Found" response
    Given new "GetSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get a Slack integration channel returns "OK" response
    Given new "GetSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all channels in a Slack integration returns "Bad Request" response
    Given new "GetSlackIntegrationChannels" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get all channels in a Slack integration returns "Item Not Found" response
    Given new "GetSlackIntegrationChannels" request
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get all channels in a Slack integration returns "OK" response
    Given new "GetSlackIntegrationChannels" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Remove a Slack integration channel returns "Bad Request" response
    Given new "RemoveSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Remove a Slack integration channel returns "Item Not Found" response
    Given new "RemoveSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Remove a Slack integration channel returns "The channel was removed successfully." response
    Given new "RemoveSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 The channel was removed successfully.

  @generated @skip
  Scenario: Update a Slack integration channel returns "Bad Request" response
    Given new "UpdateSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a Slack integration channel returns "Item Not Found" response
    Given new "UpdateSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Update a Slack integration channel returns "OK" response
    Given new "UpdateSlackIntegrationChannel" request
    And request contains "channel_name" parameter from "<PATH>"
    And body {"display": {"message": true, "notified": true, "snapshot": true, "tags": true}, "name": "#general"}
    When the request is sent
    Then the response status is 200 OK
