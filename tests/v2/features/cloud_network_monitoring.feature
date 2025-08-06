@endpoint(cloud-network-monitoring) @endpoint(cloud-network-monitoring-v2)
Feature: Cloud Network Monitoring
  The Cloud Network Monitoring API allows you to fetch aggregated
  connections and DNS traffic with their attributes. See the [Cloud Network
  Monitoring page](https://docs.datadoghq.com/network_monitoring/cloud_netwo
  rk_monitoring/) and [DNS Monitoring
  page](https://docs.datadoghq.com/network_monitoring/dns/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudNetworkMonitoring" API

  @team:Datadog/networks
  Scenario: Get aggregated connections returns "OK" response
    Given new "GetAggregatedConnections" request
    When the request is sent
    Then the response status is 200 OK

  @team:Datadog/networks
  Scenario: Get all aggregated DNS traffic returns "Bad Request" response
    Given new "GetAggregatedDns" request
    And request contains "group_by" parameter with value "server_ungrouped,server_service"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/networks
  Scenario: Get all aggregated DNS traffic returns "OK" response
    Given new "GetAggregatedDns" request
    When the request is sent
    Then the response status is 200 OK

  @skip-python @skip-ruby @team:Datadog/networks
  Scenario: Get all aggregated connections returns "Bad Request" response
    Given new "GetAggregatedConnections" request
    And request contains "limit" parameter with value 8000
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/networks
  Scenario: Get all aggregated connections returns "OK" response
    Given new "GetAggregatedConnections" request
    When the request is sent
    Then the response status is 200 OK
