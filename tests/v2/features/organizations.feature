@endpoint(organizations) @endpoint(organizations-v2)
Feature: Organizations
  Create, edit, and manage your organizations. Read more about [multi-org ac
  counts](https://docs.datadoghq.com/account_management/multi_organization).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Organizations" API
    And new "UploadIdPMetadata" request

  @skip-go @skip-java @skip-python @skip-ruby @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "Bad Request - caused by either malformed XML or invalid SAML IdP metadata" response
    Given request contains "idp_file" parameter with value "fixtures/organizations/saml_configurations/invalid_idp_metadata.xml"
    When the request is sent
    Then the response status is 400 Bad Request - caused by either malformed XML or invalid SAML IdP metadata

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-go @skip-java @skip-python @skip-ruby @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/team-aaa-identity
  Scenario: Upload IdP metadata returns "OK" response
    Given request contains "idp_file" parameter with value "fixtures/organizations/saml_configurations/valid_idp_metadata.xml"
    When the request is sent
    Then the response status is 200 OK
