@endpoint(cloud-network-monitoring) @endpoint(cloud-network-monitoring-v2)
Feature: Cloud Network Monitoring
  The Cloud Network Monitoring API allows you to fetch aggregated
  connections and their attributes. See the [Cloud Network Monitoring page](
  https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudNetworkMonitoring" API
    And operation "GetAggregatedConnections" enabled
    And new "GetAggregatedConnections" request

  @team:Datadog/networks
  Scenario: Get aggregated connections returns "OK" response
    When the request is sent
    Then the response status is 200 OK

  @skip-python @skip-ruby @team:Datadog/networks
  Scenario: Get all aggregated connections returns "Bad Request" response
    Given request contains "limit" parameter with value 6000
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/networks
  Scenario: Get all aggregated connections returns "OK" response
    When the request is sent
    Then the response status is 200 OK
