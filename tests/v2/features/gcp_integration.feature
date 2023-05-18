@endpoint(gcp-integration) @endpoint(gcp-integration-v2)
Feature: GCP Integration
  Configure your Datadog-Google Cloud Platform (GCP) integration directly
  through the Datadog API. Read more about the [Datadog-Google Cloud
  Platform integration](https://docs.datadoghq.com/integrations/google_cloud
  _platform).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GCPIntegration" API

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Create a Datadog GCP principal returns "Conflict Error" response
    Given new "MakeDelegateV2" request
    When the request is sent
    Then the response status is 409 Conflict Error

  @team:DataDog/cloud-integrations
  Scenario: Create a Datadog GCP principal returns "OK" response
    Given new "MakeDelegateV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Create a new entry for your service account returns "Bad Request" response
    Given new "CreateGCPSTSAccountsV2" request
    And body with value {"data": {"attributes": {"client_email": "dd-integration@datadog-staging.iam.gserviceaccount.com", "host_filters": []}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Create a new entry for your service account returns "Conflict Error" response
    Given new "CreateGCPSTSAccountsV2" request
    And body with value {"data": {"attributes": {"client_email": "dd-integration@datadog-staging.iam.gserviceaccount.com", "host_filters": []}}}
    When the request is sent
    Then the response status is 409 Conflict Error

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Create a new entry for your service account returns "OK" response
    Given new "CreateGCPSTSAccountsV2" request
    And body with value {"data": {"attributes": {"client_email": "dd-integration@datadog-staging.iam.gserviceaccount.com", "host_filters": []}}}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Delete an STS enabled GCP Account returns "Bad Request" response
    Given new "DeleteGCPSTSAccountsV2" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Delete an STS enabled GCP Account returns "No Content" response
    Given new "DeleteGCPSTSAccountsV2" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: List all GCP STS-enabled service accounts returns "Not Found" response
    Given new "ListGCPSTSAccountsV2" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-integrations
  Scenario: List all GCP STS-enabled service accounts returns "OK" response
    Given new "ListGCPSTSAccountsV2" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-integrations
  Scenario: List delegate account returns "OK" response
    Given new "GetDelegateV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Update STS Service Account returns "Bad Request" response
    Given new "UpdateGCPSTSAccountsV2" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": []}, "id": "d291291f-12c2-22g4-j290-123456678897", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Update STS Service Account returns "Not Found" response
    Given new "UpdateGCPSTSAccountsV2" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": []}, "id": "d291291f-12c2-22g4-j290-123456678897", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Update STS Service Account returns "OK" response
    Given new "UpdateGCPSTSAccountsV2" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": []}, "id": "d291291f-12c2-22g4-j290-123456678897", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
