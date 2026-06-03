@endpoint(rum-config) @endpoint(rum-config-v2)
Feature: Rum Config
  Manage the [Real User Monitoring
  (RUM)](https://docs.datadoghq.com/real_user_monitoring/) configuration for
  your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumConfig" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create the RUM configuration returns "Bad Request" response
    Given operation "CreateRumConfig" enabled
    And new "CreateRumConfig" request
    And body with value {"data": {"attributes": {"enforced_application_tags": true}, "type": "rum_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create the RUM configuration returns "Created" response
    Given operation "CreateRumConfig" enabled
    And new "CreateRumConfig" request
    And body with value {"data": {"attributes": {"enforced_application_tags": true}, "type": "rum_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get the RUM configuration returns "OK" response
    Given operation "GetRumConfig" enabled
    And new "GetRumConfig" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update the RUM configuration returns "Bad Request" response
    Given operation "UpdateRumConfig" enabled
    And new "UpdateRumConfig" request
    And body with value {"data": {"attributes": {"enforced_application_tags": true}, "type": "rum_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update the RUM configuration returns "OK" response
    Given operation "UpdateRumConfig" enabled
    And new "UpdateRumConfig" request
    And body with value {"data": {"attributes": {"enforced_application_tags": true}, "type": "rum_config"}}
    When the request is sent
    Then the response status is 200 OK
