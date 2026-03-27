@endpoint(widgets) @endpoint(widgets-v2)
Feature: Widgets
  Create, read, update, and delete saved widgets. Widgets are reusable
  visualization components stored independently from any dashboard or
  notebook, partitioned by experience type and identified by a UUID.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Widgets" API

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a widget returns "Bad Request" response
    Given new "CreateWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"title": "My Widget", "type": "bar_chart"}, "tags": []}, "type": "widgets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a widget returns "OK" response
    Given new "CreateWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"title": "My Widget", "type": "bar_chart"}, "tags": []}, "type": "widgets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a widget returns "Bad Request" response
    Given new "DeleteWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a widget returns "No Content" response
    Given new "DeleteWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a widget returns "Not Found" response
    Given new "DeleteWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a widget returns "Bad Request" response
    Given new "GetWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a widget returns "Not Found" response
    Given new "GetWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a widget returns "OK" response
    Given new "GetWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Search widgets returns "Bad Request" response
    Given new "SearchWidgets" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Search widgets returns "OK" response
    Given new "SearchWidgets" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a widget returns "Bad Request" response
    Given new "UpdateWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"title": "My Widget", "type": "bar_chart"}, "tags": []}, "type": "widgets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a widget returns "Not Found" response
    Given new "UpdateWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"title": "My Widget", "type": "bar_chart"}, "tags": []}, "type": "widgets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a widget returns "OK" response
    Given new "UpdateWidget" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And request contains "uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"title": "My Widget", "type": "bar_chart"}, "tags": []}, "type": "widgets"}}
    When the request is sent
    Then the response status is 200 OK
