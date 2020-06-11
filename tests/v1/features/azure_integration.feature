@endpoint(azure-integration)
Feature: Azure Integration
  Configure your Datadog-Azure integration directly through the Datadog API.
  For more information, see the [Datadog-Azure integration
  page](https://docs.datadoghq.com/integrations/azure).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AzureIntegration" API

  @generated @skip
  Scenario: Delete an Azure integration returns "OK" response
    Given new "DeleteAzureIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List all Azure integrations returns "OK" response
    Given new "ListAzureIntegration" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create an Azure integration returns "OK" response
    Given new "CreateAzureIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an Azure integration returns "OK" response
    Given new "UpdateAzureIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update Azure integration host filters returns "OK" response
    Given new "UpdateAzureHostFilters" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
