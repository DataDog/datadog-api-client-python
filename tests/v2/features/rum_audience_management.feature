@endpoint(rum-audience-management) @endpoint(rum-audience-management-v2)
Feature: Rum Audience Management
  Auto-generated tag Rum Audience Management

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumAudienceManagement" API

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Create connection returns "Connection created successfully" response
    Given operation "CreateConnection" enabled
    And new "CreateConnection" request
    And request contains "entity" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": [{"description": "Customer subscription tier from `CRM`", "display_name": "Customer Tier", "id": "customer_tier", "source_name": "subscription_tier", "type": "string"}, {"description": "Customer lifetime value in `USD`", "display_name": "Lifetime Value", "id": "lifetime_value", "source_name": "ltv", "type": "number"}], "join_attribute": "user_email", "join_type": "email", "type": "ref_table"}, "id": "crm-integration", "type": "connection_id"}}
    When the request is sent
    Then the response status is 201 Connection created successfully

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Delete connection returns "Connection deleted successfully" response
    Given operation "DeleteConnection" enabled
    And new "DeleteConnection" request
    And request contains "id" parameter from "REPLACE.ME"
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Connection deleted successfully

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Get account facet info returns "Successful response with facet information" response
    Given operation "GetAccountFacetInfo" enabled
    And new "GetAccountFacetInfo" request
    And body with value {"data": {"attributes": {"facet_id": "first_browser_name", "limit": 10, "search": {"query": "user_org_id:5001 AND first_country_code:US"}, "term_search": {"value": "Chrome"}}, "id": "facet_info_request", "type": "users_facet_info_request"}}
    When the request is sent
    Then the response status is 200 Successful response with facet information

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Get mapping returns "Successful response with entity mapping configuration" response
    Given operation "GetMapping" enabled
    And new "GetMapping" request
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response with entity mapping configuration

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Get user facet info returns "Successful response with facet information" response
    Given operation "GetUserFacetInfo" enabled
    And new "GetUserFacetInfo" request
    And body with value {"data": {"attributes": {"facet_id": "first_browser_name", "limit": 10, "search": {"query": "user_org_id:5001 AND first_country_code:US"}, "term_search": {"value": "Chrome"}}, "id": "facet_info_request", "type": "users_facet_info_request"}}
    When the request is sent
    Then the response status is 200 Successful response with facet information

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: List connections returns "Successful response with list of connections" response
    Given operation "ListConnections" enabled
    And new "ListConnections" request
    And request contains "entity" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response with list of connections

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Query accounts returns "Successful response with account data" response
    Given operation "QueryAccounts" enabled
    And new "QueryAccounts" request
    And body with value {"data": {"attributes": {"limit": 20, "query": "plan_type:enterprise AND user_count:>100 AND subscription_status:active", "select_columns": ["account_id", "account_name", "user_count", "plan_type", "subscription_status", "created_at", "mrr", "industry"], "sort": {"field": "user_count", "order": "DESC"}, "wildcard_search_term": "tech"}, "id": "query_account_request", "type": "query_account_request"}}
    When the request is sent
    Then the response status is 200 Successful response with account data

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Query event filtered users returns "Successful response with filtered user data" response
    Given operation "QueryEventFilteredUsers" enabled
    And new "QueryEventFilteredUsers" request
    And body with value {"data": {"attributes": {"event_query": {"query": "@type:view AND @view.loading_time:>3000 AND @application.name:ecommerce-platform", "time_frame": {"end": 1761309676, "start": 1760100076}}, "include_row_count": true, "limit": 25, "query": "user_org_id:5001 AND first_country_code:US AND first_browser_name:Chrome", "select_columns": ["user_id", "user_email", "first_country_code", "first_browser_name", "events_count", "session_count", "error_count", "avg_loading_time"]}, "id": "query_event_filtered_users_request", "type": "query_event_filtered_users_request"}}
    When the request is sent
    Then the response status is 200 Successful response with filtered user data

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Query users returns "Successful response with user data" response
    Given operation "QueryUsers" enabled
    And new "QueryUsers" request
    And body with value {"data": {"attributes": {"limit": 25, "query": "user_email:*@techcorp.com AND first_country_code:US AND first_browser_name:Chrome", "select_columns": ["user_id", "user_email", "user_name", "user_org_id", "first_country_code", "first_browser_name", "first_device_type", "last_seen"], "sort": {"field": "first_seen", "order": "DESC"}, "wildcard_search_term": "john"}, "id": "query_users_request", "type": "query_users_request"}}
    When the request is sent
    Then the response status is 200 Successful response with user data

  @generated @skip @team:DataDog/audience-management-backend @team:DataDog/pana-ingestion
  Scenario: Update connection returns "Connection updated successfully" response
    Given operation "UpdateConnection" enabled
    And new "UpdateConnection" request
    And request contains "entity" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields_to_add": [{"description": "Net Promoter Score from customer surveys", "display_name": "NPS Score", "groups": ["Satisfaction", "Metrics"], "id": "nps_score", "source_name": "net_promoter_score", "type": "number"}], "fields_to_delete": ["old_revenue_field"], "fields_to_update": [{"field_id": "lifetime_value", "updated_display_name": "Customer Lifetime Value (`USD`)", "updated_groups": ["Financial", "Metrics"]}]}, "id": "crm-integration", "type": "connection_id"}}
    When the request is sent
    Then the response status is 200 Connection updated successfully
