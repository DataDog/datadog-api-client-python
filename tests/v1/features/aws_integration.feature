@endpoint(aws-integration)
Feature: AWS Integration
  Configure your Datadog-AWS integration directly through the Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/integrations/amazon_web_services).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSIntegration" API

  @generated @skip
  Scenario: Delete an AWS integration returns "OK" response
    Given new "DeleteAWSAccount" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List all AWS integrations returns "OK" response
    Given new "ListAWSAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create an AWS integration returns "OK" response
    Given new "CreateAWSAccount" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an AWS integration returns "OK" response
    Given new "UpdateAWSAccount" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List namespace rules returns "OK" response
    Given new "ListAvailableAWSNamespaces" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Generate a new external ID returns "OK" response
    Given new "CreateNewAWSExternalID" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a tag filtering entry returns "OK" response
    Given new "DeleteAWSTagFilter" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all AWS tag filters returns "OK" response
    Given new "ListAWSTagFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Set an AWS tag filter returns "OK" response
    Given new "CreateAWSTagFilter" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
