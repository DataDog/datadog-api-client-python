@endpoint(rum) @endpoint(rum-v2)
Feature: RUM
  Manage your Real User Monitoring (RUM) applications, and search or
  aggregate your RUM events over HTTP. See the [RUM & Session Replay
  page](https://docs.datadoghq.com/real_user_monitoring/) for more
  information

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUM" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Aggregate RUM events returns "Bad Request" response
    Given new "AggregateRUMEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "group_by": [{"facet": "@view.time_spent", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Aggregate RUM events returns "OK" response
    Given new "AggregateRUMEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "metric": "@view.time_spent", "type": "total"}], "filter": {"from": "now-15m", "query": "@type:view AND @session.type:user", "to": "now"}, "group_by": [{"facet": "@view.time_spent", "limit": 10, "total": false}], "options": {"timezone": "GMT"}, "page": { "limit": 25}}
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.status" is equal to "done"
    And the response "data.buckets" has length 0

  @skip @team:DataDog/rum-backend
  Scenario: Create a new RUM application returns "Bad Request" response
    Given new "CreateRUMApplication" request
    And body with value {"data": {"attributes": {"name": "wrong_rum_application", "type": "wrong_android"}, "type": "wrong_rum_application_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/rum-backend
  Scenario: Create a new RUM application returns "OK" response
    Given new "CreateRUMApplication" request
    And body with value {"data": {"attributes": {"name": "test-rum-{{ unique_hash }}", "type": "ios"}, "type": "rum_application_create"}}
    When the request is sent
    Then the response status is 200 RUM application.
    And the response "data.type" is equal to "rum_application"
    And the response "data.attributes.type" is equal to "ios"
    And the response "data.attributes.name" is equal to "test-rum-{{ unique_hash }}"
    And the response "data.attributes.product_scales.rum_event_processing_scale.state" is equal to "ALL"
    And the response "data.attributes.product_scales.product_analytics_retention_scale.state" is equal to "NONE"
    And the response "data.attributes.product_scales.rum_event_processing_scale" has field "last_modified_at"
    And the response "data.attributes.product_scales.product_analytics_retention_scale" has field "last_modified_at"

  @skip-validation @team:DataDog/rum-backend
  Scenario: Create a new RUM application with Product Scales returns "OK" response
    Given new "CreateRUMApplication" request
    And body with value {"data": {"attributes": {"name": "test-rum-with-product-scales-{{ unique_hash }}", "type": "browser", "rum_event_processing_state": "ERROR_FOCUSED_MODE", "product_analytics_retention_state": "NONE"}, "type": "rum_application_create"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "rum_application"
    And the response "data.attributes.name" is equal to "test-rum-with-product-scales-{{ unique_hash }}"
    And the response "data.attributes.product_scales.rum_event_processing_scale.state" is equal to "ERROR_FOCUSED_MODE"
    And the response "data.attributes.product_scales.product_analytics_retention_scale.state" is equal to "NONE"
    And the response "data.attributes.product_scales.rum_event_processing_scale" has field "last_modified_at"
    And the response "data.attributes.product_scales.product_analytics_retention_scale" has field "last_modified_at"

  @skip-validation @team:DataDog/rum-backend
  Scenario: Delete a RUM application returns "No Content" response
    Given there is a valid "rum_application" in the system
    And new "DeleteRUMApplication" request
    And request contains "id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/rum-backend
  Scenario: Delete a RUM application returns "Not Found" response
    Given new "DeleteRUMApplication" request
    And request contains "id" parameter with value "abcde-12345"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Get a RUM application returns "Not Found" response
    Given new "GetRUMApplication" request
    And request contains "id" parameter with value "abcd1234-0000-0000-abcd-1234abcd5678"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/rum-backend
  Scenario: Get a RUM application returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "GetRUMApplication" request
    And request contains "id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "rum_application"
    And the response "data.attributes.type" is equal to "ios"
    And the response "data.attributes.name" is equal to "test-rum-{{ unique_hash }}"
    And the response "data.attributes" has field "product_scales"

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a list of RUM events returns "Bad Request" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Get a list of RUM events returns "OK" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/rum-backend @with-pagination
  Scenario: Get a list of RUM events returns "OK" response with pagination
    Given new "ListRUMEvents" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/rum-backend
  Scenario: List all the RUM applications returns "Not Found" response
    Given new "GetRUMApplications" request
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/rum-backend
  Scenario: List all the RUM applications returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "GetRUMApplications" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.application_id" with value "{{ rum_application.data.id }}"
    And the response "data" has item with field "attributes.product_scales.rum_event_processing_scale.state" with value "ALL"
    And the response "data" has item with field "attributes.product_scales.product_analytics_retention_scale.state" with value "NONE"

  @generated @skip @team:DataDog/rum-backend
  Scenario: Search RUM events returns "Bad Request" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Search RUM events returns "OK" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": 0, "timezone": "GMT"}, "page": {"limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/rum-backend @with-pagination
  Scenario: Search RUM events returns "OK" response with pagination
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": 0, "timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM application returns "Bad Request" response
    Given new "UpdateRUMApplication" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "updated_name_for_my_existing_rum_application", "product_analytics_retention_state": "MAX", "rum_event_processing_state": "ALL", "type": "browser"}, "id": "abcd1234-0000-0000-abcd-1234abcd5678", "type": "rum_application_update"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM application returns "Not Found" response
    Given new "UpdateRUMApplication" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "updated_name_for_my_existing_rum_application", "product_analytics_retention_state": "MAX", "rum_event_processing_state": "ALL", "type": "browser"}, "id": "abcd1234-0000-0000-abcd-1234abcd5678", "type": "rum_application_update"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/rum-backend
  Scenario: Update a RUM application returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMApplication" request
    And request contains "id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"name": "updated_name_for_my_existing_rum_application", "type": "browser"}, "id": "{{ rum_application.data.id }}","type": "rum_application_update"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "rum_application"
    And the response "data.attributes.application_id" is equal to "{{ rum_application.data.id }}"
    And the response "data.attributes.type" is equal to "browser"
    And the response "data.attributes.name" is equal to "updated_name_for_my_existing_rum_application"
    And the response "data.attributes.product_scales.rum_event_processing_scale.state" is equal to "ALL"
    And the response "data.attributes.product_scales.product_analytics_retention_scale.state" is equal to "NONE"
    And the response "data.attributes.product_scales.rum_event_processing_scale" has field "last_modified_at"
    And the response "data.attributes.product_scales.product_analytics_retention_scale" has field "last_modified_at"

  @skip-validation @team:DataDog/rum-backend
  Scenario: Update a RUM application returns "Unprocessable Entity." response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMApplication" request
    And request contains "id" parameter from "rum_application.data.id"
    And body with value {"data": {"id": "this_id_will_not_match", "type": "rum_application_update"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity.

  @skip-validation @team:DataDog/rum-backend
  Scenario: Update a RUM application with Product Scales returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMApplication" request
    And request contains "id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"name": "updated_rum_with_product_scales", "rum_event_processing_state": "ALL", "product_analytics_retention_state": "MAX"}, "id": "{{ rum_application.data.id }}", "type": "rum_application_update"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "rum_application"
    And the response "data.attributes.name" is equal to "updated_rum_with_product_scales"
    And the response "data.attributes.product_scales.rum_event_processing_scale.state" is equal to "ALL"
    And the response "data.attributes.product_scales.product_analytics_retention_scale.state" is equal to "MAX"
    And the response "data.attributes.product_scales.rum_event_processing_scale" has field "last_modified_at"
    And the response "data.attributes.product_scales.product_analytics_retention_scale" has field "last_modified_at"
