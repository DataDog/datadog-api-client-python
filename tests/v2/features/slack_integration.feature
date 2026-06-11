@endpoint(slack-integration) @endpoint(slack-integration-v2)
Feature: Slack Integration
  Configure your [Datadog Slack
  integration](https://docs.datadoghq.com/integrations/slack/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SlackIntegration" API
    And new "ListSlackUserBindings" request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: List Slack user bindings returns "Bad Request" response
    Given request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: List Slack user bindings returns "OK" response
    Given request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
