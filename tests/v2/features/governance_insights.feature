@endpoint(governance-insights) @endpoint(governance-insights-v2)
Feature: Governance Insights
  Governance Insights surface key usage, configuration, and best-practice
  signals for an organization within the Governance Console. Each insight
  reports a current value (and, optionally, a previous value for comparison)
  along with the query used to compute it, so that the Console can render
  trends and highlight areas that need attention.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GovernanceInsights" API
    And operation "ListGovernanceInsights" enabled
    And new "ListGovernanceInsights" request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance insights returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance insights returns "OK" response
    When the request is sent
    Then the response status is 200 OK
