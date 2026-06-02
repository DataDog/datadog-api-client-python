@endpoint(salesforce-integration) @endpoint(salesforce-integration-v2)
Feature: Salesforce Integration
  Configure your [Datadog Salesforce
  integration](https://docs.datadoghq.com/integrations/salesforce/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SalesforceIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Salesforce incident template returns "Bad Request" response
    Given new "CreateIncidentTemplate" request
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Salesforce incident template returns "CREATED" response
    Given new "CreateIncidentTemplate" request
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Salesforce incident template returns "Conflict" response
    Given new "CreateIncidentTemplate" request
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Salesforce incident template returns "Not Found" response
    Given new "CreateIncidentTemplate" request
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a Salesforce incident template returns "Not Found" response
    Given new "DeleteIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a Salesforce incident template returns "OK" response
    Given new "DeleteIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a connected Salesforce organization returns "Bad Request" response
    Given new "DeleteSalesforceOrganization" request
    And request contains "salesforce_org_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a connected Salesforce organization returns "Not Found" response
    Given new "DeleteSalesforceOrganization" request
    And request contains "salesforce_org_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a connected Salesforce organization returns "OK" response
    Given new "DeleteSalesforceOrganization" request
    And request contains "salesforce_org_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all Salesforce incident templates returns "OK" response
    Given new "GetIncidentTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all connected Salesforce organizations returns "Bad Request" response
    Given new "GetSalesforceOrganizations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all connected Salesforce organizations returns "Not Found" response
    Given new "GetSalesforceOrganizations" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all connected Salesforce organizations returns "OK" response
    Given new "GetSalesforceOrganizations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Salesforce incident template returns "Bad Request" response
    Given new "UpdateIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Salesforce incident template returns "Conflict" response
    Given new "UpdateIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Salesforce incident template returns "Not Found" response
    Given new "UpdateIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Salesforce incident template returns "OK" response
    Given new "UpdateIncidentTemplate" request
    And request contains "incident_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "An incident was detected by Datadog monitors.", "name": "production-outage", "owner_id": "005000000000000", "priority": "High", "salesforce_org_id": "596da4af-0563-4097-90ff-07230c3f9db3", "subject": "Datadog Incident: Production Outage"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "salesforce-incidents-incident-template"}}
    When the request is sent
    Then the response status is 200 OK
