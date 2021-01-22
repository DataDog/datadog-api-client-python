@endpoint(gcp-integration)
Feature: GCP Integration
  Configure your Datadog-Google Cloud Platform (GCP) integration directly
  through the Datadog API. Read more about the [Datadog-Google Cloud
  Platform integration](https://docs.datadoghq.com/integrations/google_cloud
  _platform).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GCPIntegration" API

  @generated @skip
  Scenario: Create a GCP integration returns "Bad Request" response
    Given new "CreateGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a GCP integration returns "OK" response
    Given new "CreateGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a GCP integration returns "Bad Request" response
    Given new "DeleteGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete a GCP integration returns "OK" response
    Given new "DeleteGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List all GCP integrations returns "Bad Request" response
    Given new "ListGCPIntegration" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: List all GCP integrations returns "OK" response
    Given new "ListGCPIntegration" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a GCP integration returns "Bad Request" response
    Given new "UpdateGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a GCP integration returns "OK" response
    Given new "UpdateGCPIntegration" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
