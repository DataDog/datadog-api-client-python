@endpoint(fleet-automation) @endpoint(fleet-automation-v2)
Feature: Fleet Automation
  Manage automated deployments across your fleet of hosts.  Fleet Automation
  provides two types of deployments:  Configuration Deployments
  (`/configure`): - Apply configuration file changes to target hosts -
  Support merge-patch operations to update specific configuration fields -
  Support delete operations to remove configuration files - Useful for
  updating Datadog Agent settings, integration configs, and more  Package
  Upgrade Deployments (`/upgrade`): - Upgrade the Datadog Agent to specific
  versions

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "FleetAutomation" API

  @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "Bad Request" response
    Given new "CancelFleetDeploymentV2" request
    And request contains "deployment_id" parameter with value "not-a-valid-deployment-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "Not Found" response
    Given new "CancelFleetDeploymentV2" request
    And request contains "deployment_id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/fleet-automation
  Scenario: Cancel a deployment returns "OK" response
    Given there is a valid "deployment" in the system
    And new "CancelFleetDeploymentV2" request
    And request contains "deployment_id" parameter from "deployment.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/fleet-automation
  Scenario: Create a configuration deployment returns "Bad Request" response
    Given new "CreateFleetDeploymentConfigureV2" request
    And body with value {"data": {"attributes": {"filter_query": "env:prod AND service:{{ unique_lower }}"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Create a configuration deployment returns "CREATED" response
    Given new "CreateFleetDeploymentConfigureV2" request
    And body with value {"data": {"attributes": {"config_operations": [{"file_op": "merge-patch", "file_path": "/datadog.yaml", "patch": {"apm_config": {"enabled": true}, "log_level": "info", "logs_enabled": true}}], "filter_query": "env:prod AND service:{{ unique_lower }}"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 201 CREATED

  @skip @team:DataDog/fleet-automation
  Scenario: Create a configuration deployment returns "OK" response
    Given new "CreateFleetDeploymentConfigureV2" request
    And body with value {"data": {"attributes": {"config_operations": [{"file_op": "merge-patch", "file_path": "/datadog.yaml", "patch": {"log_level": "info"}}], "dry_run": true, "filter_query": "env:prod AND service:{{ unique_lower }}"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Create a schedule returns "Bad Request" response
    Given operation "CreateFleetSchedule" enabled
    And new "CreateFleetSchedule" request
    And body with value {"data": {"attributes": {"name": "Weekly Production Agent Updates", "query": "env:prod AND service:web", "rule": {"days_of_week": ["Mon", "Wed", "Fri"], "maintenance_window_duration": 1200, "start_maintenance_window": "02:00", "timezone": "America/New_York"}, "status": "active", "version_to_latest": 0}, "type": "schedule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Create a schedule returns "CREATED" response
    Given operation "CreateFleetSchedule" enabled
    And new "CreateFleetSchedule" request
    And body with value {"data": {"attributes": {"name": "Weekly Production Agent Updates", "query": "env:prod AND service:web", "rule": {"days_of_week": ["Mon", "Wed", "Fri"], "maintenance_window_duration": 1200, "start_maintenance_window": "02:00", "timezone": "America/New_York"}, "status": "active", "version_to_latest": 0}, "type": "schedule"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Delete a schedule returns "Bad Request" response
    Given operation "DeleteFleetSchedule" enabled
    And new "DeleteFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Delete a schedule returns "Not Found" response
    Given operation "DeleteFleetSchedule" enabled
    And new "DeleteFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Delete a schedule returns "Schedule successfully deleted." response
    Given operation "DeleteFleetSchedule" enabled
    And new "DeleteFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Schedule successfully deleted.

  @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "Bad Request" response
    Given new "GetFleetDeploymentV2" request
    And request contains "deployment_id" parameter with value "not-a-valid-deployment-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "Not Found" response
    Given new "GetFleetDeploymentV2" request
    And request contains "deployment_id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/fleet-automation
  Scenario: Get a deployment by ID returns "OK" response
    Given there is a valid "deployment" in the system
    And new "GetFleetDeploymentV2" request
    And request contains "deployment_id" parameter from "deployment.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/fleet-automation
  Scenario: Get a schedule by ID returns "Bad Request" response
    Given new "GetFleetScheduleV2" request
    And request contains "id" parameter with value "not-a-valid-schedule-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Get a schedule by ID returns "Not Found" response
    Given new "GetFleetScheduleV2" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/fleet-automation
  Scenario: Get a schedule by ID returns "OK" response
    Given there is a valid "fleet_schedule" in the system
    And new "GetFleetScheduleV2" request
    And request contains "id" parameter from "schedule.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/fleet-automation
  Scenario: Get detailed information about an agent returns "Bad Request" response
    Given new "GetFleetAgentDetailV2" request
    And request contains "agent_key" parameter with value "not-a-valid-agent-key"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Get detailed information about an agent returns "Not Found" response
    Given new "GetFleetAgentDetailV2" request
    And request contains "agent_key" parameter with value "00000000000000000000000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @integration-only @skip @team:DataDog/fleet-automation
  Scenario: Get detailed information about an agent returns "OK" response
    Given new "GetFleetAgentDetailV2" request
    And request contains "agent_key" parameter with value "a1b2c3d4e5f67890a1b2c3d4e5f67890"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all Datadog Agents returns "Bad Request" response
    Given new "ListFleetAgentsV2" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all Datadog Agents returns "OK" response
    Given new "ListFleetAgentsV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all deployments returns "Bad Request" response
    Given new "ListFleetDeploymentsV2" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all deployments returns "OK" response
    Given new "ListFleetDeploymentsV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all fleet tracers returns "Bad Request" response
    Given operation "ListFleetTracers" enabled
    And new "ListFleetTracers" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all fleet tracers returns "Not Found" response
    Given operation "ListFleetTracers" enabled
    And new "ListFleetTracers" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all fleet tracers returns "OK" response
    Given operation "ListFleetTracers" enabled
    And new "ListFleetTracers" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all schedules returns "Bad Request" response
    Given new "ListFleetSchedulesV2" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List all schedules returns "OK" response
    Given new "ListFleetSchedulesV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List available Datadog Agent versions returns "Not Found" response
    Given new "ListFleetAgentVersionsV2" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List available Datadog Agent versions returns "OK" response
    Given new "ListFleetAgentVersionsV2" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List tracers for a specific agent returns "Bad Request" response
    Given operation "ListFleetAgentTracers" enabled
    And new "ListFleetAgentTracers" request
    And request contains "agent_key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List tracers for a specific agent returns "Not Found" response
    Given operation "ListFleetAgentTracers" enabled
    And new "ListFleetAgentTracers" request
    And request contains "agent_key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: List tracers for a specific agent returns "OK" response
    Given operation "ListFleetAgentTracers" enabled
    And new "ListFleetAgentTracers" request
    And request contains "agent_key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Trigger a schedule deployment returns "Bad Request" response
    Given operation "TriggerFleetSchedule" enabled
    And new "TriggerFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Trigger a schedule deployment returns "CREATED - Deployment successfully created and started." response
    Given operation "TriggerFleetSchedule" enabled
    And new "TriggerFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 CREATED - Deployment successfully created and started.

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Trigger a schedule deployment returns "Not Found" response
    Given operation "TriggerFleetSchedule" enabled
    And new "TriggerFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Update a schedule returns "Bad Request" response
    Given operation "UpdateFleetSchedule" enabled
    And new "UpdateFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Weekly Production Agent Updates", "query": "env:prod AND service:web", "rule": {"days_of_week": ["Mon", "Wed", "Fri"], "maintenance_window_duration": 1200, "start_maintenance_window": "02:00", "timezone": "America/New_York"}, "status": "active", "version_to_latest": 0}, "type": "schedule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Update a schedule returns "Not Found" response
    Given operation "UpdateFleetSchedule" enabled
    And new "UpdateFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Weekly Production Agent Updates", "query": "env:prod AND service:web", "rule": {"days_of_week": ["Mon", "Wed", "Fri"], "maintenance_window_duration": 1200, "start_maintenance_window": "02:00", "timezone": "America/New_York"}, "status": "active", "version_to_latest": 0}, "type": "schedule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/fleet-automation
  Scenario: Update a schedule returns "OK" response
    Given operation "UpdateFleetSchedule" enabled
    And new "UpdateFleetSchedule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Weekly Production Agent Updates", "query": "env:prod AND service:web", "rule": {"days_of_week": ["Mon", "Wed", "Fri"], "maintenance_window_duration": 1200, "start_maintenance_window": "02:00", "timezone": "America/New_York"}, "status": "active", "version_to_latest": 0}, "type": "schedule"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/fleet-automation
  Scenario: Upgrade hosts returns "Bad Request" response
    Given new "CreateFleetDeploymentUpgradeV2" request
    And body with value {"data": {"attributes": {"filter_query": "env:prod AND service:{{ unique_lower }}"}, "type": "deployment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/fleet-automation
  Scenario: Upgrade hosts returns "CREATED" response
    Given new "CreateFleetDeploymentUpgradeV2" request
    And body with value {"data": {"attributes": {"filter_query": "env:prod AND service:{{ unique_lower }}", "target_packages": [{"name": "datadog-agent", "version": "7.52.0"}]}, "type": "deployment"}}
    When the request is sent
    Then the response status is 201 CREATED

  @skip @team:DataDog/fleet-automation
  Scenario: Upgrade hosts returns "Conflict" response
    Given there is a valid "package_deployment" in the system
    And new "CreateFleetDeploymentUpgradeV2" request
    And body with value {"data": {"attributes": {"filter_query": "env:prod AND service:{{ unique_lower }}", "target_packages": [{"name": "datadog-agent", "version": "7.52.0"}]}, "type": "deployment"}}
    When the request is sent
    Then the response status is 409 Conflict
