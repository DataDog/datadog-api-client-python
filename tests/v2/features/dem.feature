@endpoint(dem) @endpoint(dem-v2)
Feature: DEM
  Manage Digital Experience Monitoring journeys.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DEM" API

  @generated @skip @team:DataDog/dem-features
  Scenario: Batch get DEM journeys by test suite IDs returns "Bad Request" response
    Given new "BatchGetJourneysByTestSuiteIDs" request
    And body with value {"data": {"attributes": {"test_suite_ids": ["suite-abc123", "suite-def456"]}, "type": "batch_get_journeys_by_test_suite_ids_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dem-features
  Scenario: Batch get DEM journeys by test suite IDs returns "Not Found" response
    Given new "BatchGetJourneysByTestSuiteIDs" request
    And body with value {"data": {"attributes": {"test_suite_ids": ["suite-abc123", "suite-def456"]}, "type": "batch_get_journeys_by_test_suite_ids_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Batch get DEM journeys by test suite IDs returns "OK" response
    Given new "BatchGetJourneysByTestSuiteIDs" request
    And body with value {"data": {"attributes": {"test_suite_ids": ["suite-abc123", "suite-def456"]}, "type": "batch_get_journeys_by_test_suite_ids_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a DEM journey returns "OK" response
    Given new "CreateJourney" request
    And body with value {"data": {"attributes": {"description": "Tracks the user checkout flow from cart to confirmation.", "journey_rum": {"filter": "env:prod", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "name": "Checkout Flow", "tags": ["team:synthetics", "env:prod"], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "type": "journeys"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a DEM journey variant returns "Bad Request" response
    Given new "CreateJourneyVariant" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a DEM journey variant returns "Not Found" response
    Given new "CreateJourneyVariant" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a DEM journey variant returns "OK" response
    Given new "CreateJourneyVariant" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a test suite for a DEM journey returns "Created" response
    Given new "CreateTestSuiteForJourney" request
    And request contains "public_journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"include_tests_from_journey_coverage": true, "test_suite_name": "My Custom Suite"}, "type": "create_test_suite_for_journey_request"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/dem-features
  Scenario: Create a test suite for a DEM journey returns "Not Found" response
    Given new "CreateTestSuiteForJourney" request
    And request contains "public_journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"include_tests_from_journey_coverage": true, "test_suite_name": "My Custom Suite"}, "type": "create_test_suite_for_journey_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete a DEM journey returns "No Content" response
    Given new "DeleteJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete a DEM journey returns "Not Found" response
    Given new "DeleteJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete a DEM journey variant returns "No Content" response
    Given new "DeleteJourneyVariant" request
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete a DEM journey variant returns "Not Found" response
    Given new "DeleteJourneyVariant" request
    And request contains "variant_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete an ignored inferred DEM journey returns "No Content" response
    Given new "DeleteIgnoredInferredJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dem-features
  Scenario: Delete an ignored inferred DEM journey returns "Not Found" response
    Given new "DeleteIgnoredInferredJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Get a DEM journey returns "Not Found" response
    Given new "GetJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Get a DEM journey returns "OK" response
    Given new "GetJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Get recommended tests for a DEM journey returns "Not Found" response
    Given new "GetJourneyRecommendedTests" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Get recommended tests for a DEM journey returns "OK" response
    Given new "GetJourneyRecommendedTests" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Ignore an inferred DEM journey returns "No Content" response
    Given new "IgnoreInferredJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dem-features
  Scenario: Ignore an inferred DEM journey returns "Not Found" response
    Given new "IgnoreInferredJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Search DEM journeys returns "Bad Request" response
    Given new "SearchJourneys" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dem-features
  Scenario: Search DEM journeys returns "Not Found" response
    Given new "SearchJourneys" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Search DEM journeys returns "OK" response
    Given new "SearchJourneys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Search inferred DEM journeys returns "Bad Request" response
    Given new "SearchInferredJourneys" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dem-features
  Scenario: Search inferred DEM journeys returns "Not Found" response
    Given new "SearchInferredJourneys" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Search inferred DEM journeys returns "OK" response
    Given new "SearchInferredJourneys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Update a DEM journey returns "Not Found" response
    Given new "UpdateJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Tracks the user checkout flow from cart to confirmation.", "journey_rum": {"filter": "env:prod", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "name": "Checkout Flow", "tags": ["team:synthetics", "env:prod"], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "type": "journeys"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Update a DEM journey returns "OK" response
    Given new "UpdateJourney" request
    And request contains "journey_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Tracks the user checkout flow from cart to confirmation.", "journey_rum": {"filter": "env:prod", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "name": "Checkout Flow", "tags": ["team:synthetics", "env:prod"], "variants": [{"name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}]}, "type": "journeys"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dem-features
  Scenario: Update a DEM journey variant returns "Bad Request" response
    Given new "UpdateJourneyVariant" request
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dem-features
  Scenario: Update a DEM journey variant returns "Not Found" response
    Given new "UpdateJourneyVariant" request
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dem-features
  Scenario: Update a DEM journey variant returns "OK" response
    Given new "UpdateJourneyVariant" request
    And request contains "variant_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"filter": "device.type:mobile", "name": "Mobile checkout", "rum_steps": [{"nodes": [{"query": "action.name:'checkout'"}], "type": "start"}, {"nodes": [{"query": "action.name:'confirmation'"}], "type": "stop"}]}, "type": "variants"}}
    When the request is sent
    Then the response status is 200 OK
