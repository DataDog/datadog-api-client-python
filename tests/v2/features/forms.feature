@endpoint(forms) @endpoint(forms-v2)
Feature: Forms
  The Datadog Forms API lets you create and manage forms within the App
  Builder platform. You can configure form settings, manage versions,
  publish forms, and handle sharing configurations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Forms" API

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a form returns "Bad Request" response
    Given operation "CreateForm" enabled
    And new "CreateForm" request
    And body with value {"data": {"attributes": {"anonymous": false, "data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "description": "A form to collect user feedback.", "idp_survey": false, "name": "User Feedback Form", "single_response": false, "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}}, "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Create a form returns "OK" response
    Given operation "CreateForm" enabled
    And new "CreateForm" request
    And body with value {"data": {"attributes": {"anonymous": false, "data_definition": {}, "description": "A form to collect user feedback.", "idp_survey": false, "name": "User Feedback Form", "single_response": false, "ui_definition": {}}, "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create and publish a form returns "Bad Request" response
    Given operation "CreateAndPublishForm" enabled
    And new "CreateAndPublishForm" request
    And body with value {"data": {"attributes": {"anonymous": false, "data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "description": "A form to collect user feedback.", "idp_survey": false, "name": "User Feedback Form", "single_response": false, "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}}, "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Create and publish a form returns "OK" response
    Given operation "CreateAndPublishForm" enabled
    And new "CreateAndPublishForm" request
    And body with value {"data": {"attributes": {"anonymous": false, "data_definition": {}, "description": "A form to collect user feedback.", "idp_survey": false, "name": "User Feedback Form", "single_response": false, "ui_definition": {}}, "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Delete a form returns "Bad Request" response
    Given operation "DeleteForm" enabled
    And new "DeleteForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Delete a form returns "OK" response
    Given operation "DeleteForm" enabled
    And there is a valid "form" in the system
    And new "DeleteForm" request
    And request contains "form_id" parameter from "form.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "form.data.id"
    And the response "data.type" is equal to "forms"

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Get a form returns "Bad Request" response
    Given operation "GetForm" enabled
    And new "GetForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Get a form returns "Not Found" response
    Given operation "GetForm" enabled
    And new "GetForm" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Get a form returns "OK" response
    Given operation "GetForm" enabled
    And there is a valid "form" in the system
    And new "GetForm" request
    And request contains "form_id" parameter from "form.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "form.data.id"
    And the response "data.type" is equal to "forms"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List forms returns "Bad Request" response
    Given operation "ListForms" enabled
    And new "ListForms" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: List forms returns "OK" response
    Given operation "ListForms" enabled
    And there is a valid "form" in the system
    And new "ListForms" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ form.data.id }}"
    And the response "data" has item with field "type" with value "forms"
    And the response "data" has item with field "attributes.name" with value "{{ unique }}"
