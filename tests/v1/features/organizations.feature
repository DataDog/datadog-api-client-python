@endpoint(organizations)
Feature: Organizations
  Create, edit, and manage your organizations. Read more about [multi-org ac
  counts](https://docs.datadoghq.com/account_management/multi_organization).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Organizations" API

  @generated @skip
  Scenario: List your managed organizations returns "OK" response
    Given new "ListOrgs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a child organization returns "OK" response
    Given new "CreateChildOrg" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get organization information returns "OK" response
    Given new "GetOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update your organization returns "OK" response
    Given new "UpdateOrg" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Upload IdP metadata returns "OK" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK
