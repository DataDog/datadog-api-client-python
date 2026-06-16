@endpoint(network-health-insights) @endpoint(network-health-insights-v2)
Feature: Network Health Insights
  Analyze network health by surfacing actionable insights for services
  experiencing connectivity issues. Insights are derived from DNS failure
  data (timeouts, NXDOMAIN, SERVFAIL, general failures), TLS certificate
  health (expired, expiring soon), and security group denials.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "NetworkHealthInsights" API
    And operation "ListNetworkHealthInsights" enabled
    And new "ListNetworkHealthInsights" request

  @generated @skip @team:DataDog/cloud-network-monitoring
  Scenario: List network health insights returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-network-monitoring
  Scenario: List network health insights returns "OK" response
    When the request is sent
    Then the response status is 200 OK
