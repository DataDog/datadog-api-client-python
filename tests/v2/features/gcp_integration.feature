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

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Create a Datadog GCP principal returns "Conflict" response
    Given new "MakeGCPSTSDelegate" request
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/gcp-integrations
  Scenario: Create a Datadog GCP principal returns "OK" response
    Given new "MakeGCPSTSDelegate" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "gcp_sts_delegate"

  @team:DataDog/gcp-integrations
  Scenario: Create a Datadog GCP principal with empty body returns "OK" response
    Given new "MakeGCPSTSDelegate" request
    And body with value {}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "gcp_sts_delegate"

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account returns "Bad Request" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"account_tags": [], "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": [], "is_security_command_center_enabled": true}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account returns "Conflict" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"account_tags": [], "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": [], "is_security_command_center_enabled": true}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account returns "OK" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "gcp_service_account"
    And the response "data.attributes.client_email" is equal to "{{ unique_hash }}@test-project.iam.gserviceaccount.com"

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account with account_tags returns "OK" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"account_tags": ["lorem", "ipsum"], "client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "gcp_service_account"
    And the response "data.attributes.client_email" is equal to "{{ unique_hash }}@test-project.iam.gserviceaccount.com"
    And the response "data.attributes.account_tags" is equal to ["lorem", "ipsum"]

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account with cspm enabled returns "OK" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"is_cspm_enabled": true, "resource_collection_enabled": true, "client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "gcp_service_account"
    And the response "data.attributes.client_email" is equal to "{{ unique_hash }}@test-project.iam.gserviceaccount.com"
    And the response "data.attributes.is_cspm_enabled" is equal to true

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account with resource collection enabled disabled and cspm enabled returns "Bad Request" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"resource_collection_enabled": false, "is_cspm_enabled": true, "client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account with resource collection enabled returns "OK" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"resource_collection_enabled": true, "client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "gcp_service_account"
    And the response "data.attributes.client_email" is equal to "{{ unique_hash }}@test-project.iam.gserviceaccount.com"
    And the response "data.attributes.resource_collection_enabled" is equal to true

  @team:DataDog/gcp-integrations
  Scenario: Create a new entry for your service account with security command center enabled returns "OK" response
    Given new "CreateGCPSTSAccount" request
    And body with value {"data": {"attributes": {"is_security_command_center_enabled": true, "client_email": "{{ unique_hash }}@test-project.iam.gserviceaccount.com", "host_filters": []}, "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.type" is equal to "gcp_service_account"
    And the response "data.attributes.client_email" is equal to "{{ unique_hash }}@test-project.iam.gserviceaccount.com"
    And the response "data.attributes.is_security_command_center_enabled" is equal to true

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Delete an STS enabled GCP Account returns "Bad Request" response
    Given new "DeleteGCPSTSAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Delete an STS enabled GCP Account returns "No Content" response
    Given new "DeleteGCPSTSAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: List all GCP STS-enabled service accounts returns "Not Found" response
    Given new "ListGCPSTSAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/gcp-integrations
  Scenario: List all GCP STS-enabled service accounts returns "OK" response
    Given there is a valid "gcp_sts_account" in the system
    And new "ListGCPSTSAccounts" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "type" with value "gcp_service_account"

  @team:DataDog/gcp-integrations
  Scenario: List delegate account returns "OK" response
    Given new "GetGCPSTSDelegate" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "gcp_sts_delegate"

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Update STS Service Account returns "Bad Request" response
    Given new "UpdateGCPSTSAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": [], "is_security_command_center_enabled": true}, "id": "d291291f-12c2-22g4-j290-123456678897", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/gcp-integrations
  Scenario: Update STS Service Account returns "Not Found" response
    Given new "UpdateGCPSTSAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "client_email": "datadog-service-account@test-project.iam.gserviceaccount.com", "host_filters": [], "is_security_command_center_enabled": true}, "id": "d291291f-12c2-22g4-j290-123456678897", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/gcp-integrations
  Scenario: Update STS Service Account returns "OK" response
    Given there is a valid "gcp_sts_account" in the system
    And new "UpdateGCPSTSAccount" request
    And request contains "account_id" parameter from "gcp_sts_account.data.id"
    And body with value {"data": {"attributes": {"client_email": "{{ unique_hash }}@example.com", "host_filters": ["foo:bar"]}, "id": "{{ gcp_sts_account.data.id }}", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK

  @team:DataDog/gcp-integrations
  Scenario: Update STS Service Account returns "OK" response with enable resource collection turned on
    Given there is a valid "gcp_sts_account" in the system
    And new "UpdateGCPSTSAccount" request
    And request contains "account_id" parameter from "gcp_sts_account.data.id"
    And body with value {"data": {"attributes": {"client_email": "{{ unique_hash }}@example.com", "resource_collection_enabled": true}, "id": "{{ gcp_sts_account.data.id }}", "type": "gcp_service_account"}}
    When the request is sent
    Then the response status is 201 OK
