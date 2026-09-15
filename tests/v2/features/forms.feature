@endpoint(forms) @endpoint(forms-v2)
Feature: Forms
  The Datadog Forms API lets you create and manage forms within the App
  Builder platform. You can configure form settings, manage versions, and
  publish forms.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Forms" API

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Clone a form returns "Bad Request" response
    Given operation "CloneForm" enabled
    And new "CloneForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Copy of My Form"}, "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Clone a form returns "Not Found" response
    Given operation "CloneForm" enabled
    And new "CloneForm" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"name": "Copy of My Form"}, "type": "forms"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Clone a form returns "OK" response
    Given operation "CloneForm" enabled
    And new "CloneForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Copy of My Form"}, "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

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
  Scenario: Create or update a form version returns "Bad Request" response
    Given operation "UpsertFormVersion" enabled
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "state": "frozen", "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "insert_only": false, "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Create or update a form version returns "Not Found" response
    Given operation "UpsertFormVersion" enabled
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "state": "frozen", "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "insert_only": false, "match_policy": "none"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Create or update a form version returns "OK" response
    Given operation "UpsertFormVersion" enabled
    And there is a valid "form" in the system
    And new "UpsertFormVersion" request
    And request contains "form_id" parameter from "form.data.id"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "state": "frozen", "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d", "insert_only": false, "match_policy": "none"}}, "type": "form_versions"}}
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
  Scenario: List form versions returns "Bad Request" response
    Given operation "ListFormVersions" enabled
    And new "ListFormVersions" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List form versions returns "Not Found" response
    Given operation "ListFormVersions" enabled
    And new "ListFormVersions" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List form versions returns "OK" response
    Given operation "ListFormVersions" enabled
    And new "ListFormVersions" request
    And request contains "form_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

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

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Publish a form version returns "Bad Request" response
    Given operation "PublishForm" enabled
    And new "PublishForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Publish a form version returns "Not Found" response
    Given operation "PublishForm" enabled
    And new "PublishForm" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Publish a form version returns "OK" response
    Given operation "PublishForm" enabled
    And there is a valid "form" in the system
    And new "PublishForm" request
    And request contains "form_id" parameter from "form.data.id"
    And body with value {"data": {"attributes": {"version": 1}, "type": "form_publications"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Revert a form to a prior version returns "Bad Request" response
    Given operation "RevertFormVersion" enabled
    And new "RevertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Revert a form to a prior version returns "Conflict" response
    Given operation "RevertFormVersion" enabled
    And new "RevertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Revert a form to a prior version returns "Not Found" response
    Given operation "RevertFormVersion" enabled
    And new "RevertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Revert a form to a prior version returns "OK" response
    Given operation "RevertFormVersion" enabled
    And new "RevertFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Update a form returns "Bad Request" response
    Given operation "UpdateForm" enabled
    And new "UpdateForm" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"form_update": {"datastore_config": {"datastore_id": "5108ea24-dd83-4696-9caa-f069f73d0fad", "primary_column_name": "id", "primary_key_generation_strategy": "none"}, "description": "An updated description.", "name": "Updated Form Name"}}, "id": "22f6006a-2302-4926-9396-d2dfcf7b0b34", "type": "forms"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Update a form returns "Not Found" response
    Given operation "UpdateForm" enabled
    And new "UpdateForm" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"form_update": {"datastore_config": {"datastore_id": "5108ea24-dd83-4696-9caa-f069f73d0fad", "primary_column_name": "id", "primary_key_generation_strategy": "none"}, "description": "An updated description.", "name": "Updated Form Name"}}, "id": "22f6006a-2302-4926-9396-d2dfcf7b0b34", "type": "forms"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Update a form returns "OK" response
    Given operation "UpdateForm" enabled
    And there is a valid "form" in the system
    And new "UpdateForm" request
    And request contains "form_id" parameter from "form.data.id"
    And body with value {"data": {"attributes": {"form_update": {"datastore_config": {"datastore_id": "5108ea24-dd83-4696-9caa-f069f73d0fad", "primary_column_name": "id", "primary_key_generation_strategy": "none"}, "description": "An updated description.", "name": "Updated Form Name"}}, "id": "22f6006a-2302-4926-9396-d2dfcf7b0b34", "type": "forms"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "Bad Request" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "Not Found" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Upsert and publish a form version returns "OK" response
    Given operation "UpsertAndPublishFormVersion" enabled
    And there is a valid "form" in the system
    And new "UpsertAndPublishFormVersion" request
    And request contains "form_id" parameter from "form.data.id"
    And body with value {"data": {"attributes": {"data_definition": {"description": "Welcome to the Engineering Experience Survey.", "required": [], "title": "Developer Experience Survey", "type": "object"}, "ui_definition": {"ui:order": [], "ui:theme": {"primaryColor": "gray"}}, "upsert_params": {"etag": "b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d"}}, "type": "form_versions"}}
    When the request is sent
    Then the response status is 200 OK
