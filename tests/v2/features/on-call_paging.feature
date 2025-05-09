@endpoint(on-call-paging) @endpoint(on-call-paging-v2)
Feature: On-Call Paging
  Trigger and manage [Datadog On-
  Call](https://docs.datadoghq.com/service_management/on-call/) pages
  directly through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "On-CallPaging" API

  @generated @skip @team:DataDog/bugle
  Scenario: Acknowledge On-Call Page returns "Accepted." response
    Given new "AcknowledgeOnCallPage" request
    And request contains "page_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted.

  @generated @skip @team:DataDog/bugle
  Scenario: Create On-Call Page returns "OK." response
    Given new "CreateOnCallPage" request
    And body with value {"data": {"attributes": {"description": "Page details.", "tags": ["service:test"], "target": {"identifier": "my-team", "type": "team_handle"}, "title": "Page title", "urgency": "low"}, "type": "pages"}}
    When the request is sent
    Then the response status is 200 OK.

  @generated @skip @team:DataDog/bugle
  Scenario: Escalate On-Call Page returns "Accepted." response
    Given new "EscalateOnCallPage" request
    And request contains "page_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted.

  @generated @skip @team:DataDog/bugle
  Scenario: Resolve On-Call Page returns "Accepted." response
    Given new "ResolveOnCallPage" request
    And request contains "page_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted.
