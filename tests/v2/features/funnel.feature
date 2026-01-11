@endpoint(funnel) @endpoint(funnel-v2)
Feature: Funnel
  API for funnel.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Funnel" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get rum funnel returns "Successful response with funnel analysis data" response
    Given operation "GetRumFunnel" enabled
    And new "GetRumFunnel" request
    And body with value {"data": {"attributes": {"data_source": "rum", "enforced_execution_type": "", "request_id": "", "search": {"cross_session_filter": "", "query_string": "@type:view", "steps": [{"facet": "@view.name", "step_filter": "", "value": "/apm/home"}, {"facet": "@view.name", "step_filter": "", "value": "/apm/traces"}], "subquery_id": ""}, "time": {"from": 1756425600000, "to": 1756857600000}}, "id": "funnel_request", "type": "funnel_request"}}
    When the request is sent
    Then the response status is 200 Successful response with funnel analysis data

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get rum funnel step suggestions returns "Successful response with funnel step suggestions" response
    Given operation "GetRumFunnelStepSuggestions" enabled
    And new "GetRumFunnelStepSuggestions" request
    And body with value {"data": {"attributes": {"data_source": "", "search": {"cross_session_filter": "", "query_string": "@type:view", "steps": [{"facet": "@view.name", "step_filter": "", "value": "/apm/home"}], "subquery_id": ""}, "term_search": {"query": "apm"}, "time": {"from": 1756425600000, "to": 1756857600000}}, "id": "funnel_suggestion_request", "type": "funnel_suggestion_request"}}
    When the request is sent
    Then the response status is 200 Successful response with funnel step suggestions
