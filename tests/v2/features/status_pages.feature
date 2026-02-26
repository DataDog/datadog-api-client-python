@endpoint(status-pages) @endpoint(status-pages-v2)
Feature: Status Pages
  Manage your status pages and communicate service disruptions to
  stakeholders via Datadog's API. See the [Status Pages
  documentation](https://docs.datadoghq.com/incident_response/status_pages/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "StatusPages" API

  @team:DataDog/incident-app
  Scenario: Create component returns "Created" response
    Given there is a valid "status_page" in the system
    And new "CreateComponent" request
    And request contains "page_id" parameter from "status_page.data.id"
    And body with value {"data": {"attributes": {"name": "Logs", "position": 0, "type": "component"}, "type": "components"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.status" is equal to "operational"

  @team:DataDog/incident-app
  Scenario: Create degradation returns "Created" response
    Given there is a valid "status_page" in the system
    And new "CreateDegradation" request
    And request contains "page_id" parameter from "status_page.data.id"
    And body with value {"data": {"attributes": {"components_affected": [{"id": "{{ status_page.data.attributes.components[0].components[0].id }}", "status": "major_outage"}], "description": "Our API is experiencing elevated latency. We are investigating the issue.", "status": "investigating", "title": "Elevated API Latency"}, "type": "degradations"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.updates" has length 1

  @team:DataDog/incident-app
  Scenario: Create maintenance returns "Created" response
    Given there is a valid "status_page" in the system
    And new "CreateMaintenance" request
    And request contains "page_id" parameter from "status_page.data.id"
    And body with value {"data": {"attributes": {"title": "API Maintenance", "scheduled_description": "We will be performing maintenance on the API to improve performance.", "in_progress_description": "We are currently performing maintenance on the API to improve performance.", "completed_description": "We have completed maintenance on the API to improve performance.", "start_date": "{{ timeISO('now + 1h') }}", "completed_date": "{{ timeISO('now + 2h') }}", "components_affected": [{"id": "{{ status_page.data.attributes.components[0].components[0].id }}", "status": "operational"}]}, "type": "maintenances"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.updates" has length 1

  @team:DataDog/incident-app
  Scenario: Create status page returns "Created" response
    Given new "CreateStatusPage" request
    And body with value {"data": {"attributes": {"name": "A Status Page", "domain_prefix": "{{ unique_hash }}", "components":[{"name": "Login", "type": "component", "position": 0},{"name": "Settings", "type": "component", "position": 1}], "enabled": true, "type": "internal", "visualization_type": "bars_and_uptime_percentage"}, "type": "status_pages"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/incident-app
  Scenario: Delete component returns "No Content" response
    Given new "DeleteComponent" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "component_id" parameter from "status_page.data.attributes.components[0].id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/incident-app
  Scenario: Delete degradation returns "No Content" response
    Given new "DeleteDegradation" request
    And there is a valid "status_page" in the system
    And there is a valid "degradation" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "degradation_id" parameter from "degradation.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/incident-app
  Scenario: Delete status page returns "No Content" response
    Given new "DeleteStatusPage" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/incident-app
  Scenario: Get component returns "OK" response
    Given new "GetComponent" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "component_id" parameter from "status_page.data.attributes.components[0].id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: Get degradation returns "OK" response
    Given new "GetDegradation" request
    And there is a valid "status_page" in the system
    And there is a valid "degradation" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "degradation_id" parameter from "degradation.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: Get maintenance returns "OK" response
    Given there is a valid "status_page" in the system
    And there is a valid "maintenance" in the system
    And new "GetMaintenance" request
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "maintenance_id" parameter from "maintenance.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: Get status page returns "OK" response
    Given new "GetStatusPage" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: List components returns "OK" response
    Given new "ListComponents" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: List degradations returns "OK" response
    Given new "ListDegradations" request
    And there is a valid "status_page" in the system
    And there is a valid "degradation" in the system
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: List maintenances returns "OK" response
    Given there is a valid "status_page" in the system
    And there is a valid "maintenance" in the system
    And new "ListMaintenances" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: List status pages returns "OK" response
    Given new "ListStatusPages" request
    And there is a valid "status_page" in the system
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Schedule maintenance returns "Created" response
    Given new "CreateMaintenance" request
    And request contains "page_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"completed_date": "2026-02-18T19:51:13.332360075Z", "completed_description": "We have completed maintenance on the API to improve performance.", "components_affected": [{"id": "1234abcd-12ab-34cd-56ef-123456abcdef", "status": "operational"}], "in_progress_description": "We are currently performing maintenance on the API to improve performance.", "scheduled_description": "We will be performing maintenance on the API to improve performance.", "start_date": "2026-02-18T19:21:13.332360075Z", "title": "API Maintenance"}, "type": "maintenances"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/incident-app
  Scenario: Update component returns "OK" response
    Given new "UpdateComponent" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "component_id" parameter from "status_page.data.attributes.components[0].id"
    And body with value {"data": {"attributes": {"name": "Logs Indexing"}, "id": "{{ status_page.data.attributes.components[0].id }}", "type": "components"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "Logs Indexing"

  @team:DataDog/incident-app
  Scenario: Update degradation returns "OK" response
    Given new "UpdateDegradation" request
    And there is a valid "status_page" in the system
    And there is a valid "degradation" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "degradation_id" parameter from "degradation.data.id"
    And body with value {"data": {"attributes": {"title": "Elevated API Latency in US1"}, "id": "{{ degradation.data.id }}", "type": "degradations"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.title" is equal to "Elevated API Latency in US1"

  @team:DataDog/incident-app
  Scenario: Update maintenance returns "OK" response
    Given there is a valid "status_page" in the system
    And there is a valid "maintenance" in the system
    And new "UpdateMaintenance" request
    And request contains "page_id" parameter from "status_page.data.id"
    And request contains "maintenance_id" parameter from "maintenance.data.id"
    And body with value {"data": {"attributes": {"scheduled_description": "We will be performing maintenance on the API to improve performance for 40 minutes.", "in_progress_description": "We are currently performing maintenance on the API to improve performance for 40 minutes."}, "id": "{{ maintenance.data.id }}", "type": "maintenances"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: Update status page returns "OK" response
    Given new "UpdateStatusPage" request
    And there is a valid "status_page" in the system
    And request contains "page_id" parameter from "status_page.data.id"
    And body with value {"data": {"attributes": {"name": "A Status Page in US1"}, "id": "{{ status_page.data.id }}", "type": "status_pages"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "A Status Page in US1"
