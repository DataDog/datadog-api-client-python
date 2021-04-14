@endpoint(organizations)
Feature: Organizations
  Create, edit, and manage your organizations. Read more about [multi-org ac
  counts](https://docs.datadoghq.com/account_management/multi_organization).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Organizations" API

  @generated @skip
  Scenario: Create a child organization returns "Bad Request" response
    Given new "CreateChildOrg" request
    And body {"billing": {"type": "parent_billing"}, "name": "New child org", "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a child organization returns "OK" response
    Given new "CreateChildOrg" request
    And body {"billing": {"type": "parent_billing"}, "name": "New child org", "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get organization information returns "Bad Request" response
    Given new "GetOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get organization information returns "OK" response
    Given new "GetOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List your managed organizations returns "OK" response
    Given new "ListOrgs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update your organization returns "Bad Request" response
    Given new "UpdateOrg" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"billing": {"type": "parent_billing"}, "created": "2019-09-26T17:28:28Z", "description": "some description", "name": "New child org", "public_id": "abcdef12345", "settings": {"private_widget_share": false, "saml": {"enabled": false}, "saml_autocreate_access_role": "st", "saml_autocreate_users_domains": {"domains": ["example.com"], "enabled": false}, "saml_can_be_enabled": false, "saml_idp_endpoint": "https://my.saml.endpoint", "saml_idp_initiated_login": {"enabled": false}, "saml_idp_metadata_uploaded": false, "saml_login_url": "https://my.saml.login.url", "saml_strict_mode": {"enabled": false}}, "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update your organization returns "OK" response
    Given new "UpdateOrg" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"billing": {"type": "parent_billing"}, "created": "2019-09-26T17:28:28Z", "description": "some description", "name": "New child org", "public_id": "abcdef12345", "settings": {"private_widget_share": false, "saml": {"enabled": false}, "saml_autocreate_access_role": "st", "saml_autocreate_users_domains": {"domains": ["example.com"], "enabled": false}, "saml_can_be_enabled": false, "saml_idp_endpoint": "https://my.saml.endpoint", "saml_idp_initiated_login": {"enabled": false}, "saml_idp_metadata_uploaded": false, "saml_login_url": "https://my.saml.login.url", "saml_strict_mode": {"enabled": false}}, "subscription": {"type": "pro"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Upload IdP metadata returns "Bad Request" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Upload IdP metadata returns "OK" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Upload IdP metadata returns "Unsupported Media Type" response
    Given new "UploadIdPForOrg" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 415 Unsupported Media Type
