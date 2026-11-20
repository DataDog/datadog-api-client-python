@endpoint(rum-audience-management) @endpoint(rum-audience-management-v2)
Feature: Rum Audience Management
  Auto-generated tag Rum Audience Management

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumAudienceManagement" API

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Create connection returns "Connection created successfully" response
    Given operation "CreateConnection" enabled
    And new "CreateConnection" request
    And request contains "entity" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": [{"description": "Customer subscription tier from `CRM`", "display_name": "Customer Tier", "id": "customer_tier", "source_name": "subscription_tier", "type": "string"}, {"description": "Customer lifetime value in `USD`", "display_name": "Lifetime Value", "id": "lifetime_value", "source_name": "ltv", "type": "number"}], "join_attribute": "user_email", "join_type": "email", "type": "ref_table"}, "id": "crm-integration", "type": "connection_id"}}
    When the request is sent
    Then the response status is 201 Connection created successfully

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Delete a user profile returns "Bad Request" response
    Given operation "DeleteUserProfile" enabled
    And new "DeleteUserProfile" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Delete a user profile returns "Deletion accepted; the profile will be removed asynchronously" response
    Given operation "DeleteUserProfile" enabled
    And new "DeleteUserProfile" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Deletion accepted; the profile will be removed asynchronously

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Delete connection returns "Connection deleted successfully" response
    Given operation "DeleteConnection" enabled
    And new "DeleteConnection" request
    And request contains "id" parameter from "REPLACE.ME"
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Connection deleted successfully

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Get mapping returns "Successful response with entity mapping configuration" response
    Given operation "GetMapping" enabled
    And new "GetMapping" request
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response with entity mapping configuration

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: List connections returns "Successful response with list of connections" response
    Given operation "ListConnections" enabled
    And new "ListConnections" request
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response with list of connections

  @generated @skip @team:ddoghq/audience-management-backend @team:ddoghq/product-analytics-ingestion
  Scenario: Update connection returns "Connection updated successfully" response
    Given operation "UpdateConnection" enabled
    And new "UpdateConnection" request
    And request contains "entity" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields_to_add": [{"description": "Net Promoter Score from customer surveys", "display_name": "NPS Score", "groups": ["Satisfaction", "Metrics"], "id": "nps_score", "source_name": "net_promoter_score", "type": "number"}], "fields_to_delete": ["old_revenue_field"], "fields_to_update": [{"field_id": "lifetime_value", "updated_display_name": "Customer Lifetime Value (`USD`)", "updated_groups": ["Financial", "Metrics"]}]}, "id": "crm-integration", "type": "connection_id"}}
    When the request is sent
    Then the response status is 200 Connection updated successfully
