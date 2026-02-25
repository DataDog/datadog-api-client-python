@endpoint(product-analytics) @endpoint(product-analytics-v2)
Feature: Product Analytics
  Send server-side events to Product Analytics. Server-Side Events Ingestion
  allows you to collect custom events from any server-side source, and
  retains events for 15 months. Server-side events are helpful for
  understanding causes of a funnel drop-off which are external to the
  client-side (for example, payment processing error). See the [Product
  Analytics page](https://docs.datadoghq.com/product_analytics/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "ProductAnalytics" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute scalar analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsScalar" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute scalar analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsScalar" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute timeseries analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsTimeseries" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute timeseries analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsTimeseries" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Bad Request" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Payload Too Large" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Request Timeout" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 408 Request Timeout

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 202 Request accepted for processing (always 202 empty JSON).
