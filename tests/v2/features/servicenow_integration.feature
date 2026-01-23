@endpoint(servicenow-integration) @endpoint(servicenow-integration-v2)
Feature: ServiceNow Integration
  Manage your ServiceNow Integration. ServiceNow is a cloud-based platform
  that helps organizations manage digital workflows for enterprise
  operations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceNowIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create ServiceNow template returns "Bad Request" response
    Given operation "CreateServiceNowTemplate" enabled
    And new "CreateServiceNowTemplate" request
    And body with value {"data": {"attributes": {"assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "fields_mapping": {"category": "software", "priority": "1"}, "handle_name": "incident-template", "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "servicenow_tablename": "incident", "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"}, "type": "servicenow_templates"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create ServiceNow template returns "Created" response
    Given operation "CreateServiceNowTemplate" enabled
    And new "CreateServiceNowTemplate" request
    And body with value {"data": {"attributes": {"assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "fields_mapping": {"category": "software", "priority": "1"}, "handle_name": "incident-template", "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "servicenow_tablename": "incident", "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"}, "type": "servicenow_templates"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete ServiceNow template returns "Bad Request" response
    Given operation "DeleteServiceNowTemplate" enabled
    And new "DeleteServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete ServiceNow template returns "Not Found" response
    Given operation "DeleteServiceNowTemplate" enabled
    And new "DeleteServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete ServiceNow template returns "OK" response
    Given operation "DeleteServiceNowTemplate" enabled
    And new "DeleteServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get ServiceNow template returns "Bad Request" response
    Given operation "GetServiceNowTemplate" enabled
    And new "GetServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get ServiceNow template returns "Not Found" response
    Given operation "GetServiceNowTemplate" enabled
    And new "GetServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get ServiceNow template returns "OK" response
    Given operation "GetServiceNowTemplate" enabled
    And new "GetServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow assignment groups returns "Bad Request" response
    Given operation "ListServiceNowAssignmentGroups" enabled
    And new "ListServiceNowAssignmentGroups" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow assignment groups returns "Not Found" response
    Given operation "ListServiceNowAssignmentGroups" enabled
    And new "ListServiceNowAssignmentGroups" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow assignment groups returns "OK" response
    Given operation "ListServiceNowAssignmentGroups" enabled
    And new "ListServiceNowAssignmentGroups" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow business services returns "Bad Request" response
    Given operation "ListServiceNowBusinessServices" enabled
    And new "ListServiceNowBusinessServices" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow business services returns "Not Found" response
    Given operation "ListServiceNowBusinessServices" enabled
    And new "ListServiceNowBusinessServices" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow business services returns "OK" response
    Given operation "ListServiceNowBusinessServices" enabled
    And new "ListServiceNowBusinessServices" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow instances returns "Not Found" response
    Given operation "ListServiceNowInstances" enabled
    And new "ListServiceNowInstances" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow instances returns "OK" response
    Given operation "ListServiceNowInstances" enabled
    And new "ListServiceNowInstances" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow templates returns "OK" response
    Given operation "ListServiceNowTemplates" enabled
    And new "ListServiceNowTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow users returns "Bad Request" response
    Given operation "ListServiceNowUsers" enabled
    And new "ListServiceNowUsers" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow users returns "Not Found" response
    Given operation "ListServiceNowUsers" enabled
    And new "ListServiceNowUsers" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List ServiceNow users returns "OK" response
    Given operation "ListServiceNowUsers" enabled
    And new "ListServiceNowUsers" request
    And request contains "instance_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update ServiceNow template returns "Bad Request" response
    Given operation "UpdateServiceNowTemplate" enabled
    And new "UpdateServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "fields_mapping": {"category": "hardware", "priority": "2"}, "handle_name": "incident-template-updated", "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "servicenow_tablename": "incident", "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"}, "type": "servicenow_templates"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update ServiceNow template returns "Not Found" response
    Given operation "UpdateServiceNowTemplate" enabled
    And new "UpdateServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "fields_mapping": {"category": "hardware", "priority": "2"}, "handle_name": "incident-template-updated", "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "servicenow_tablename": "incident", "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"}, "type": "servicenow_templates"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update ServiceNow template returns "OK" response
    Given operation "UpdateServiceNowTemplate" enabled
    And new "UpdateServiceNowTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "fields_mapping": {"category": "hardware", "priority": "2"}, "handle_name": "incident-template-updated", "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e", "servicenow_tablename": "incident", "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"}, "type": "servicenow_templates"}}
    When the request is sent
    Then the response status is 200 OK
