@endpoint(elastic-cloud-cloud-cost-management) @endpoint(elastic-cloud-cloud-cost-management-v2)
Feature: Elastic Cloud Cloud Cost Management
  Manage Elastic Cloud accounts for the Cloud Cost Management interface
  (`elastic-cloud-ccm`), served by the Account Management Service (AMS).
  Concrete, strongly typed CRUD operations for the Cloud Cost Management
  interface.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ElasticCloudCloudCostManagement" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud CCM account returns "Bad Request" response
    Given operation "CreateElasticCloudCcmAccount" enabled
    And new "CreateElasticCloudCcmAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud CCM account returns "Created" response
    Given operation "CreateElasticCloudCcmAccount" enabled
    And new "CreateElasticCloudCcmAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud CCM account returns "Not Found" response
    Given operation "CreateElasticCloudCcmAccount" enabled
    And new "CreateElasticCloudCcmAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud CCM account returns "Bad Request" response
    Given operation "DeleteElasticCloudCcmAccount" enabled
    And new "DeleteElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud CCM account returns "No Content" response
    Given operation "DeleteElasticCloudCcmAccount" enabled
    And new "DeleteElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud CCM account returns "Not Found" response
    Given operation "DeleteElasticCloudCcmAccount" enabled
    And new "DeleteElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud CCM account returns "Bad Request" response
    Given operation "GetElasticCloudCcmAccount" enabled
    And new "GetElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud CCM account returns "Not Found" response
    Given operation "GetElasticCloudCcmAccount" enabled
    And new "GetElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud CCM account returns "OK" response
    Given operation "GetElasticCloudCcmAccount" enabled
    And new "GetElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud CCM accounts returns "Bad Request" response
    Given operation "ListElasticCloudCcmAccounts" enabled
    And new "ListElasticCloudCcmAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud CCM accounts returns "Not Found" response
    Given operation "ListElasticCloudCcmAccounts" enabled
    And new "ListElasticCloudCcmAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud CCM accounts returns "OK" response
    Given operation "ListElasticCloudCcmAccounts" enabled
    And new "ListElasticCloudCcmAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud CCM account returns "Bad Request" response
    Given operation "UpdateElasticCloudCcmAccount" enabled
    And new "UpdateElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud CCM account returns "Not Found" response
    Given operation "UpdateElasticCloudCcmAccount" enabled
    And new "UpdateElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud CCM account returns "OK" response
    Given operation "UpdateElasticCloudCcmAccount" enabled
    And new "UpdateElasticCloudCcmAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "your-billing-api-key", "type": "bearer_token"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-cost-data"}], "name": "elastic-cloud-ccm-prod", "settings": {"elastic_org_id": "2079364244"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
