@endpoint(rum-user-segments) @endpoint(rum-user-segments-v2)
Feature: RUM User Segments
  Manage RUM user segments for audience targeting and analysis.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMUserSegments" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a RUM segment returns "Bad Request" response
    Given operation "CreateRumSegment" enabled
    And new "CreateRumSegment" request
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Users who visited the homepage.", "name": "My Segment", "tags": ["team:frontend"]}, "type": "segment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a RUM segment returns "Conflict" response
    Given operation "CreateRumSegment" enabled
    And new "CreateRumSegment" request
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Users who visited the homepage.", "name": "My Segment", "tags": ["team:frontend"]}, "type": "segment"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a RUM segment returns "Created" response
    Given operation "CreateRumSegment" enabled
    And new "CreateRumSegment" request
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Users who visited the homepage.", "name": "My Segment", "tags": ["team:frontend"]}, "type": "segment"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a static RUM segment returns "Bad Request" response
    Given operation "CreateRumStaticSegment" enabled
    And new "CreateRumStaticSegment" request
    And body with value {"data": {"attributes": {"description": "Users from a specific journey.", "journey_query_object": {"nodes": [{"filters": [{"attribute": "@type", "value": "view"}]}]}, "name": "My Static Segment", "tags": ["team:frontend"]}, "type": "create_static_segment_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a static RUM segment returns "Conflict" response
    Given operation "CreateRumStaticSegment" enabled
    And new "CreateRumStaticSegment" request
    And body with value {"data": {"attributes": {"description": "Users from a specific journey.", "journey_query_object": {"nodes": [{"filters": [{"attribute": "@type", "value": "view"}]}]}, "name": "My Static Segment", "tags": ["team:frontend"]}, "type": "create_static_segment_request"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create a static RUM segment returns "Created" response
    Given operation "CreateRumStaticSegment" enabled
    And new "CreateRumStaticSegment" request
    And body with value {"data": {"attributes": {"description": "Users from a specific journey.", "journey_query_object": {"nodes": [{"filters": [{"attribute": "@type", "value": "view"}]}]}, "name": "My Static Segment", "tags": ["team:frontend"]}, "type": "create_static_segment_request"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Delete a RUM segment returns "Not Found" response
    Given operation "DeleteRumSegment" enabled
    And new "DeleteRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Delete a RUM segment returns "OK" response
    Given operation "DeleteRumSegment" enabled
    And new "DeleteRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get a RUM segment returns "Bad Request" response
    Given operation "GetRumSegment" enabled
    And new "GetRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get a RUM segment returns "Not Found" response
    Given operation "GetRumSegment" enabled
    And new "GetRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get a RUM segment returns "OK" response
    Given operation "GetRumSegment" enabled
    And new "GetRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Initialize RUM segments returns "OK" response
    Given operation "InitializeRumSegments" enabled
    And new "InitializeRumSegments" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List RUM segment templates returns "Bad Request" response
    Given operation "ListRumSegmentTemplates" enabled
    And new "ListRumSegmentTemplates" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List RUM segment templates returns "OK" response
    Given operation "ListRumSegmentTemplates" enabled
    And new "ListRumSegmentTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List all RUM segments returns "Bad Request" response
    Given operation "ListRumSegments" enabled
    And new "ListRumSegments" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List all RUM segments returns "OK" response
    Given operation "ListRumSegments" enabled
    And new "ListRumSegments" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Update a RUM segment returns "Bad Request" response
    Given operation "UpdateRumSegment" enabled
    And new "UpdateRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Updated description.", "name": "Updated Segment Name", "tags": ["team:backend"]}, "id": "a1b2c3d4-1234-5678-9abc-123456789abc", "type": "segment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Update a RUM segment returns "Conflict" response
    Given operation "UpdateRumSegment" enabled
    And new "UpdateRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Updated description.", "name": "Updated Segment Name", "tags": ["team:backend"]}, "id": "a1b2c3d4-1234-5678-9abc-123456789abc", "type": "segment"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Update a RUM segment returns "No Content" response
    Given operation "UpdateRumSegment" enabled
    And new "UpdateRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Updated description.", "name": "Updated Segment Name", "tags": ["team:backend"]}, "id": "a1b2c3d4-1234-5678-9abc-123456789abc", "type": "segment"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Update a RUM segment returns "Not Found" response
    Given operation "UpdateRumSegment" enabled
    And new "UpdateRumSegment" request
    And request contains "segment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_query": {"combination": "(logs && apm_home) && NOT(apm_trace)", "event_platforms": [{"facet": "@usr.id", "from": 1709888355000, "name": "logs", "query": "@type:view @view.url_path:/logs", "to": 1710493155000}], "journeys": [{"conversion_type": "any", "group_by": "@usr.id", "name": "my_journey", "search": "@type:view"}], "reference_tables": [{"columns": [{"name": "user_id"}], "filter_query": "", "join_condition": {"column_name": "user_id", "facet": "@usr.id"}, "name": "my_ref_table", "table_name": "my_table"}], "static": [{"id": "static-list-1", "name": "My Static List", "user_count": 500}], "templates": [{"from": 1709888355000, "parameters": {"threshold": "5"}, "template_id": "stickiness-v1", "to": 1710493155000}]}, "description": "Updated description.", "name": "Updated Segment Name", "tags": ["team:backend"]}, "id": "a1b2c3d4-1234-5678-9abc-123456789abc", "type": "segment"}}
    When the request is sent
    Then the response status is 404 Not Found
