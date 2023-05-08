@endpoint(organizations) @endpoint(organizations-v1)
Feature: Organizations
  Create, edit, and manage your organizations. Read more about [multi-org ac
  counts](https://docs.datadoghq.com/account_management/multi_organization).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Organizations" API

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create a child organization returns "Bad Request" response
    Given new "CreateChildOrg" request
    And body with value {"billing": {"type": "parent_billing"}, "name": "New child org", "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create a child organization returns "OK" response
    Given new "CreateChildOrg" request
    And body with value {"billing": {"type": "parent_billing"}, "name": "New child org", "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get organization information returns "Bad Request" response
    Given new "GetOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get organization information returns "OK" response
    Given new "GetOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: List your managed organizations returns "OK" response
    Given new "ListOrgs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Spin-off Child Organization returns "Bad Request" response
    Given new "DowngradeOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Spin-off Child Organization returns "OK" response
    Given new "DowngradeOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Update your organization returns "Bad Request" response
    Given new "UpdateOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"billing": {"type": "parent_billing"}, "description": "some description", "name": "New child org", "public_id": "abcdef12345", "settings": {"private_widget_share": false, "saml": {"enabled": false}, "saml_autocreate_access_role": "st", "saml_autocreate_users_domains": {"domains": ["example.com"], "enabled": false}, "saml_can_be_enabled": false, "saml_idp_endpoint": "https://my.saml.endpoint", "saml_idp_initiated_login": {"enabled": false}, "saml_idp_metadata_uploaded": false, "saml_login_url": "https://my.saml.login.url", "saml_strict_mode": {"enabled": false}}, "subscription": {"type": "pro"}, "trial": false}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Update your organization returns "OK" response
    Given new "UpdateOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"billing": {"type": "parent_billing"}, "description": "some description", "name": "New child org", "public_id": "abcdef12345", "settings": {"private_widget_share": false, "saml": {"enabled": false}, "saml_autocreate_access_role": "st", "saml_autocreate_users_domains": {"domains": ["example.com"], "enabled": false}, "saml_can_be_enabled": false, "saml_idp_endpoint": "https://my.saml.endpoint", "saml_idp_initiated_login": {"enabled": false}, "saml_idp_metadata_uploaded": false, "saml_login_url": "https://my.saml.login.url", "saml_strict_mode": {"enabled": false}}, "subscription": {"type": "pro"}, "trial": false}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/team-aaa
  Scenario: Upload IdP metadata returns "Bad Request" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "idp_file" parameter with value "./idp_metadata_invalid.xml"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/team-aaa
  Scenario: Upload IdP metadata returns "OK" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "idp_file" parameter with value "./idp_metadata.xml"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Upload IdP metadata returns "Unsupported Media Type" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 415 Unsupported Media Type
