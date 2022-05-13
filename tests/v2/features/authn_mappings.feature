@endpoint(authn-mappings) @endpoint(authn-mappings-v2)
Feature: AuthN Mappings
  [AuthN Mappings API](https://docs.datadoghq.com/account_management/authn_m
  apping/?tab=example) is used to automatically map group of users to roles
  in Datadog using attributes sent from Identity Providers.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AuthNMappings" API

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an AuthN Mapping returns "Bad Request" response
    Given new "CreateAuthNMapping" request
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an AuthN Mapping returns "Not Found" response
    Given new "CreateAuthNMapping" request
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Create an AuthN Mapping returns "OK" response
    Given there is a valid "role" in the system
    And new "CreateAuthNMapping" request
    And body with value {"data": {"attributes": {"attribute_key": "{{ unique_lower_alnum }}", "attribute_value": "{{ unique }}"}, "relationships": {"role": {"data": {"id": "{{ role.data.id }}", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an AuthN Mapping returns "Not Found" response
    Given new "DeleteAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Delete an AuthN Mapping returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "authn_mapping" in the system
    And new "DeleteAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "authn_mapping.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an AuthN Mapping returns "Bad Request" response
    Given new "UpdateAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an AuthN Mapping returns "Conflict" response
    Given new "UpdateAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an AuthN Mapping returns "Not Found" response
    Given new "UpdateAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Edit an AuthN Mapping returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "authn_mapping" in the system
    And new "UpdateAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "authn_mapping.data.id"
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "id": "{{ authn_mapping.data.id }}", "relationships": {"role": {"data": {"id": "{{ role.data.id }}", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an AuthN Mapping returns "Unprocessable Entity" response
    Given new "UpdateAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"attribute_key": "member-of", "attribute_value": "Development"}, "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "relationships": {"role": {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}}, "type": "authn_mappings"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get an AuthN Mapping by UUID returns "Not Found" response
    Given new "GetAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Get an AuthN Mapping by UUID returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "authn_mapping" in the system
    And new "GetAuthNMapping" request
    And request contains "authn_mapping_id" parameter from "authn_mapping.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa
  Scenario: List all AuthN Mappings returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "authn_mapping" in the system
    And new "ListAuthNMappings" request
    When the request is sent
    Then the response status is 200 OK
