@endpoint(rum) @endpoint(rum-v2)
Feature: RUM
  Search your RUM events over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUM" API

  @generated @skip @team:DataDog/rum-back
  Scenario: Get a list of RUM events returns "Bad Request" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-back
  Scenario: Get a list of RUM events returns "OK" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-back
  Scenario: Search RUM events returns "Bad Request" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": null, "timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-back
  Scenario: Search RUM events returns "OK" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": 0, "timezone": "GMT"}, "page": {"limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK
