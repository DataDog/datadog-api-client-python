@endpoint(fleet-automation) @endpoint(fleet-automation-v2)
Feature: Fleet Automation
  Manage automated deployments across your fleet of hosts. Use these
  endpoints to create, retrieve, and cancel deployments that apply
  configuration changes to multiple hosts at once.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "FleetAutomation" API

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "Bad Request" response
    Given operation "CancelFleetDeployment" enabled
    And new "CancelFleetDeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "Deployment successfully canceled." response
    Given operation "CancelFleetDeployment" enabled
    And new "CancelFleetDeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Deployment successfully canceled.

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "Not Found" response
    Given operation "CancelFleetDeployment" enabled
    And new "CancelFleetDeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Create a deployment returns "Bad Request" response
    Given operation "CreateFleetDeploymentConfigure" enabled
    And new "CreateFleetDeploymentConfigure" request
    And body with value {"data": {"attributes": {"config_operations": [{"file_op": "merge-patch", "file_path": "/datadog.yaml", "patch": {"apm_config": {"enabled": true}, "log_level": "debug", "logs_enabled": true}}], "filter_query": "env:prod AND service:web"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Create a deployment returns "CREATED" response
    Given operation "CreateFleetDeploymentConfigure" enabled
    And new "CreateFleetDeploymentConfigure" request
    And body with value {"data": {"attributes": {"config_operations": [{"file_op": "merge-patch", "file_path": "/datadog.yaml", "patch": {"apm_config": {"enabled": true}, "log_level": "debug", "logs_enabled": true}}], "filter_query": "env:prod AND service:web"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "Bad Request" response
    Given operation "GetFleetDeployment" enabled
    And new "GetFleetDeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "Not Found" response
    Given operation "GetFleetDeployment" enabled
    And new "GetFleetDeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "OK" response
    Given operation "GetFleetDeployment" enabled
    And there is a valid "deployment" in the system
    And new "GetFleetDeployment" request
    And request contains "deployment_id" parameter from "deployment.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all deployments returns "Bad Request" response
    Given operation "ListFleetDeployments" enabled
    And new "ListFleetDeployments" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all deployments returns "OK" response
    Given operation "ListFleetDeployments" enabled
    And new "ListFleetDeployments" request
    When the request is sent
    Then the response status is 200 OK
