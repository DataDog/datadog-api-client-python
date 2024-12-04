@endpoint(scim) @endpoint(scim-v2)
Feature: Scim
  Provision Datadog teams using SCIM group APIs.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Scim" API

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create SCIM group returns "Bad Request" response
    Given new "CreateSCIMGroup" request
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create SCIM group returns "Created" response
    Given new "CreateSCIMGroup" request
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete SCIM group returns "Bad Request" response
    Given new "DeleteSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete SCIM group returns "No Content" response
    Given new "DeleteSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete SCIM group returns "Not Found" response
    Given new "DeleteSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get SCIM group returns "Bad Request" response
    Given new "GetSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get SCIM group returns "Not Found" response
    Given new "GetSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get SCIM group returns "OK" response
    Given new "GetSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List SCIM groups returns "Bad Request" response
    Given new "ListSCIMGroups" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List SCIM groups returns "OK" response
    Given new "ListSCIMGroups" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Patch SCIM group returns "Bad Request" response
    Given new "PatchSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"Operations": [{"op": "replace", "path": null, "value": {"displayName": "Real new group", "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad"}}, {"op": "remove", "path": "members[value eq \"fddf0cf2-9b60-11ef-ad4b-d6754a54a839\"]", "value": null}], "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Patch SCIM group returns "Not Found" response
    Given new "PatchSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"Operations": [{"op": "replace", "path": null, "value": {"displayName": "Real new group", "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad"}}, {"op": "remove", "path": "members[value eq \"fddf0cf2-9b60-11ef-ad4b-d6754a54a839\"]", "value": null}], "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Patch SCIM group returns "OK" response
    Given new "PatchSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"Operations": [{"op": "replace", "path": null, "value": {"displayName": "Real new group", "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad"}}, {"op": "remove", "path": "members[value eq \"fddf0cf2-9b60-11ef-ad4b-d6754a54a839\"]", "value": null}], "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update SCIM group returns "Bad Request" response
    Given new "UpdateSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update SCIM group returns "Conflict" response
    Given new "UpdateSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update SCIM group returns "Not Found" response
    Given new "UpdateSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update SCIM group returns "OK" response
    Given new "UpdateSCIMGroup" request
    And request contains "group_id" parameter from "REPLACE.ME"
    And body with value {"members": [{"$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6", "type": "User"}], "meta": {"resourceType": "Group"}, "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]}
    When the request is sent
    Then the response status is 200 OK
