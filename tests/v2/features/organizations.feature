@endpoint(organizations) @endpoint(organizations-v2)
Feature: Organizations
  Create, edit, and manage your organizations. Read more about [multi-org ac
  counts](https://docs.datadoghq.com/account_management/multi_organization).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Organizations" API

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Get a specific Org Config value returns "Bad Request" response
    Given new "GetOrgConfig" request
    And request contains "org_config_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa-identity
  Scenario: Get a specific Org Config value returns "Not Found" response
    Given new "GetOrgConfig" request
    And request contains "org_config_name" parameter with value "i_dont_exist"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa-identity
  Scenario: Get a specific Org Config value returns "OK" response
    Given new "GetOrgConfig" request
    And request contains "org_config_name" parameter with value "custom_roles"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: List Org Configs returns "Bad Request" response
    Given new "ListOrgConfigs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa-identity
  Scenario: List Org Configs returns "OK" response
    Given new "ListOrgConfigs" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa-identity
  Scenario: Update a specific Org Config returns "Bad Request" response
    Given new "UpdateOrgConfig" request
    And request contains "org_config_name" parameter with value "custom_roles"
    And body with value {"data": {"attributes": {"value": "not-a-boolean"}, "type": "org_configs"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa-identity
  Scenario: Update a specific Org Config returns "Not Found" response
    Given new "UpdateOrgConfig" request
    And request contains "org_config_name" parameter with value "i_dont_exist"
    And body with value {"data": {"attributes": {"value": []}, "type": "org_configs"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa-identity
  Scenario: Update a specific Org Config returns "OK" response
    Given new "UpdateOrgConfig" request
    And request contains "org_config_name" parameter with value "monitor_timezone"
    And body with value {"data": {"attributes": {"value": "UTC"}, "type": "org_configs"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "Bad Request - caused by either malformed XML or invalid SAML IdP metadata" response
    Given new "UploadIdPMetadata" request
    And request contains "idp_file" parameter with value "fixtures/organizations/saml_configurations/invalid_idp_metadata.xml"
    When the request is sent
    Then the response status is 400 Bad Request - caused by either malformed XML or invalid SAML IdP metadata

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "Bad Request" response
    Given new "UploadIdPMetadata" request
    When the request is sent
    Then the response status is 400 Bad Request

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "OK" response
    Given new "UploadIdPMetadata" request
    And request contains "idp_file" parameter with value "fixtures/organizations/saml_configurations/valid_idp_metadata.xml"
    When the request is sent
    Then the response status is 200 OK
