@endpoint(events) @endpoint(events-v1)
Feature: Events
  The events service allows you to programmatically post events to the event
  stream and fetch events from the event stream. Events are limited to 4000
  characters. If an event is sent out with a message containing more than
  4000 characters, only the first 4000 characters are displayed.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Events" API

  @generated @skip @team:DataDog/monitors-evaluation
  Scenario: Get a list of events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListEvents" request
    And request contains "start" parameter from "REPLACE.ME"
    And request contains "end" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/monitors-evaluation
  Scenario: Get a list of events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListEvents" request
    And request contains "start" parameter from "REPLACE.ME"
    And request contains "end" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/monitors-evaluation
  Scenario: Get an event returns "Item Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "GetEvent" request
    And request contains "event_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip @team:DataDog/monitors-evaluation
  Scenario: Get an event returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetEvent" request
    And request contains "event_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitors-evaluation
  Scenario: Post an event in the past returns "Bad Request" response
    Given new "CreateEvent" request
    And body with value {"title": "{{ unique }}", "text": "A text message.", "date_happened": 1, "tags": ["test:{{ unique_alnum }}"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/monitors-evaluation
  Scenario: Post an event returns "Bad Request" response
    Given new "CreateEvent" request
    And body with value {"alert_type": "info", "priority": "normal", "tags": ["environment:test"], "text": "Oh boy!", "title": "Did you hear the news today?"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitors-evaluation
  Scenario: Post an event returns "OK" response
    Given new "CreateEvent" request
    And body with value {"title": "{{ unique }}", "text": "A text message.", "tags": ["test:{{ unique_alnum }}"]}
    When the request is sent
    Then the response status is 202 OK
    And the response "event.text" is equal to "A text message."

  @team:DataDog/monitors-evaluation
  Scenario: Post an event with a long title returns "OK" response
    Given new "CreateEvent" request
    And body with value {"title": "{{ unique }} very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters", "text": "A text message.", "tags": ["test:{{ unique_alnum }}"]}
    When the request is sent
    Then the response status is 202 OK
