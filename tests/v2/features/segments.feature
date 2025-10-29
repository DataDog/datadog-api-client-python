@endpoint(segments) @endpoint(segments-v2)
Feature: Segments
  API for segments.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Segments" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Create rum segment returns "Segment created successfully" response
    Given operation "CreateRumSegment" enabled
    And new "CreateRumSegment" request
    And body with value {"data": {"attributes": {"created_at": "0001-01-01T00:00:00Z", "created_by": {"handle": "", "id": "", "uuid": ""}, "data_query": {"event_platform": [{"facet": "@usr.id", "from": "2025-08-01", "name": "high_value_users", "query": "@type:view @view.name:/logs @usr.session_duration:>300000", "to": "2025-09-01"}]}, "description": "Users who frequently visit logs and have high session duration", "modified_at": "0001-01-01T00:00:00Z", "modified_by": {"handle": "", "id": "", "uuid": ""}, "name": "High-Value Users", "org_id": 123456, "source": 0, "tags": ["high-value", "logs", "active"], "version": 1}, "id": "segment-12345", "type": "segment"}}
    When the request is sent
    Then the response status is 201 Segment created successfully

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Initialize rum segments returns "Default segments created successfully" response
    Given operation "InitializeRumSegments" enabled
    And new "InitializeRumSegments" request
    When the request is sent
    Then the response status is 200 Default segments created successfully

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List rum segments returns "Successful response with list of segments" response
    Given operation "ListRumSegments" enabled
    And new "ListRumSegments" request
    When the request is sent
    Then the response status is 200 Successful response with list of segments
