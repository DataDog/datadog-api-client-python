@endpoint(rum-insights) @endpoint(rum-insights-v2)
Feature: RUM Insights
  Get insights into the performance of your Real User Monitoring (RUM)
  applications over HTTP. See the [RUM & Session Replay
  page](https://docs.datadoghq.com/real_user_monitoring/) for more
  information

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMInsights" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated long tasks returns "Bad Request" response
    Given operation "QueryAggregatedLongTasks" enabled
    And new "QueryAggregatedLongTasks" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "filter": "@session.type:user", "from": 1762437564, "sample_size": 20, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_long_tasks"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated long tasks returns "Successful response" response
    Given operation "QueryAggregatedLongTasks" enabled
    And new "QueryAggregatedLongTasks" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "filter": "@session.type:user", "from": 1762437564, "sample_size": 20, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_long_tasks"}}
    When the request is sent
    Then the response status is 201 Successful response

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated signals and problems returns "Bad Request" response
    Given operation "QueryAggregatedSignalsProblems" enabled
    And new "QueryAggregatedSignalsProblems" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "detection_types": ["high_script_evaluations", "uncompressed_resources"], "filter": "@session.type:user", "from": 1762437564, "sample_size": 30, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_signals_problems"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated signals and problems returns "Successful response" response
    Given operation "QueryAggregatedSignalsProblems" enabled
    And new "QueryAggregatedSignalsProblems" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "detection_types": ["high_script_evaluations", "uncompressed_resources"], "filter": "@session.type:user", "from": 1762437564, "sample_size": 30, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_signals_problems"}}
    When the request is sent
    Then the response status is 201 Successful response

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated waterfall returns "Bad Request" response
    Given operation "QueryAggregatedWaterfall" enabled
    And new "QueryAggregatedWaterfall" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "filter": "@session.type:user", "from": 1762437564, "include_global_appearance": false, "sample_size": 20, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_waterfall"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Query aggregated waterfall returns "Successful response" response
    Given operation "QueryAggregatedWaterfall" enabled
    And new "QueryAggregatedWaterfall" request
    And body with value {"data": {"attributes": {"application_id": "ccbc53b1-74f2-496b-bdd7-9a8fa7b7376b", "criteria": {"max": 5.0, "metric": "largest_contentful_paint", "min": 2.5}, "filter": "@session.type:user", "from": 1762437564, "include_global_appearance": false, "sample_size": 20, "to": 1762523964, "view_name": "/account/login(/:type)"}, "type": "aggregated_waterfall"}}
    When the request is sent
    Then the response status is 201 Successful response
