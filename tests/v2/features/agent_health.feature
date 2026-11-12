@endpoint(agent-health) @endpoint(agent-health-v2)
Feature: Agent Health
  List open Agent Health issues across your organization and get an issue
  with its available remediation. Issues are reported by node Agents,
  Cluster Agents, and OpenTelemetry collectors. The meaning of `resource_id`
  depends on `resource_kind`: hostname for `host`, DaemonSet UID for
  `deployment` (node Agent), cluster UUID for `cluster`, hostname of the
  host running the Cluster Agent for `cluster_agent`, or OpenTelemetry
  collector ID for `otel`.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "AgentHealth" API

  @skip @team:ddoghq/fleet-remediation
  Scenario: Get an Agent Health issue returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And operation "GetAgentHealthIssue" enabled
    And new "GetAgentHealthIssue" request
    And request contains "issue_id" parameter with value "does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/fleet-remediation
  Scenario: Get an Agent Health issue returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "GetAgentHealthIssue" enabled
    And new "GetAgentHealthIssue" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/fleet-remediation
  Scenario: List Agent Health issues returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "ListAgentHealthIssues" enabled
    And new "ListAgentHealthIssues" request
    And request contains "page[size]" parameter with value 1000
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/fleet-remediation
  Scenario: List Agent Health issues returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "ListAgentHealthIssues" enabled
    And new "ListAgentHealthIssues" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/fleet-remediation
  Scenario: List active Agent Health issues returns "Bad Request" response
    Given new "ListAgentHealthHostIssues" request
    And request contains "resource_id" parameter with value "123e4567-e89b-12d3-a456-426614174000"
    And request contains "agent_type" parameter with value "process"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/fleet-remediation
  Scenario: List active Agent Health issues returns "OK" response
    Given new "ListAgentHealthHostIssues" request
    And request contains "resource_id" parameter with value "123e4567-e89b-12d3-a456-426614174000"
    And request contains "agent_type" parameter with value "node"
    When the request is sent
    Then the response status is 200 OK
