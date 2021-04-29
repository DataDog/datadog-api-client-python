@endpoint(events)
Feature: Events
  The events service allows you to programmatically post events to the event
  stream and fetch events from the event stream. Events are limited to 4000
  characters. If an event is sent out with a message containing more than
  4000 characters only the 4000 first characters are displayed.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Events" API

  @generated @skip
  Scenario: Get an event returns "Item Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "GetEvent" request
    And request contains "event_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get an event returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetEvent" request
    And request contains "event_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Post an event returns "Bad Request" response
    Given new "CreateEvent" request
    And body with value {"aggregation_key": null, "alert_type": "info", "date_happened": null, "device_name": null, "host": null, "priority": "normal", "related_event_id": null, "source_type_name": null, "tags": ["environment:test"], "text": "Oh boy!", "title": "Did you hear the news today?"}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Post an event returns "OK" response
    Given new "CreateEvent" request
    And body with value {"title": "{{ unique }}", "text": "A text message.", "tags": ["test:{{ unique_alnum }}"]}
    When the request is sent
    Then the response status is 202 OK

  @generated @skip
  Scenario: Query the event stream returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Query the event stream returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListEvents" request
    When the request is sent
    Then the response status is 200 OK
