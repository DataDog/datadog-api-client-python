@endpoint(forms) @endpoint(forms-v2)
Feature: Forms
  Create and manage forms for collecting data from users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Forms" API

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a form version returns "Bad Request" response
    Given operation "UpsertFormVersion" enabled
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a form version returns "Conflict" response
    Given operation "UpsertFormVersion" enabled
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a form version returns "OK" response
    Given operation "UpsertFormVersion" enabled
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a new form returns "Bad Request" response
    Given operation "CreateForm" enabled
    And new "CreateForm" request
    And body with value {"data": {"attributes": {"data_definition": {}, "description": "test description", "name": "test form happy path", "ui_definition": {}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create a new form returns "OK" response
    Given operation "CreateForm" enabled
    And new "CreateForm" request
    And body with value {"data": {"attributes": {"data_definition": {}, "description": "test description", "name": "test form happy path", "ui_definition": {}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create and publish a form returns "Bad Request" response
    Given operation "CreateAndPublishForm" enabled
    And new "CreateAndPublishForm" request
    And body with value {"data": {"attributes": {"data_definition": {}, "description": "test description", "name": "test form happy path", "ui_definition": {}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Create and publish a form returns "OK" response
    Given operation "CreateAndPublishForm" enabled
    And new "CreateAndPublishForm" request
    And body with value {"data": {"attributes": {"data_definition": {}, "description": "test description", "name": "test form happy path", "ui_definition": {}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Delete a form returns "Bad Request" response
    Given operation "DeleteForm" enabled
    And new "DeleteForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Delete a form returns "OK" response
    Given operation "DeleteForm" enabled
    And new "DeleteForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Get a form returns "Bad Request" response
    Given operation "GetForm" enabled
    And new "GetForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Get a form returns "Not Found" response
    Given operation "GetForm" enabled
    And new "GetForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Get a form returns "OK" response
    Given operation "GetForm" enabled
    And new "GetForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List all forms returns "Bad Request" response
    Given operation "ListForms" enabled
    And new "ListForms" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List all forms returns "OK" response
    Given operation "ListForms" enabled
    And new "ListForms" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Publish a form returns "Bad Request" response
    Given operation "PublishForm" enabled
    And new "PublishForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Publish a form returns "Not Found" response
    Given operation "PublishForm" enabled
    And new "PublishForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Publish a form returns "OK" response
    Given operation "PublishForm" enabled
    And new "PublishForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Submit a form returns "Bad Request" response
    Given operation "SubmitForm" enabled
    And new "SubmitForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"submission_data": {}}, "type": "form_submissions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Submit a form returns "Not Found" response
    Given operation "SubmitForm" enabled
    And new "SubmitForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"submission_data": {}}, "type": "form_submissions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Submit a form returns "OK" response
    Given operation "SubmitForm" enabled
    And new "SubmitForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"submission_data": {}}, "type": "form_submissions"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Update a form returns "Bad Request" response
    Given operation "UpdateForm" enabled
    And new "UpdateForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"form_update": {"description": "Updated description", "name": "New Form Name"}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Update a form returns "Not Found" response
    Given operation "UpdateForm" enabled
    And new "UpdateForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"form_update": {"description": "Updated description", "name": "New Form Name"}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Update a form returns "OK" response
    Given operation "UpdateForm" enabled
    And new "UpdateForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"form_update": {"description": "Updated description", "name": "New Form Name"}}, "id": "00000000-0000-0000-0000-000000000000", "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "Bad Request" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "Conflict" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "OK" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"updated": "true"}, "state": "draft", "ui_definition": {}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 200 OK
