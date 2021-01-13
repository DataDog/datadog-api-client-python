@endpoint(events)
Feature: Events
  The events service allows you to programmatically post events to the event
  stream and fetch events from the event stream. Events are limited to 4000
  characters. If an event is sent out with a message containing more than
  4000 characters only the 4000 first characters are displayed.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Events" API

  @generated @skip
  Scenario: Query the event stream returns "OK" response
    Given new "ListEvents" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an event returns "OK" response
    Given new "GetEvent" request
    And request contains "event_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Query the event stream returns "Bad Request" response
    Given new "ListEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get an event returns "Item Not Found" response
    Given new "GetEvent" request
    And request contains "event_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found
