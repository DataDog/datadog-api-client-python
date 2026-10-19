@endpoint(agent-health) @endpoint(agent-health-v2)
Feature: Agent Health
  View Agent Health issues reported for node Agents and Cluster Agents.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "AgentHealth" API
    And new "ListAgentHealthHostIssues" request
    And request contains "resource_id" parameter with value "123e4567-e89b-12d3-a456-426614174000"

  @skip @team:ddoghq/fleet-remediation
  Scenario: List active Agent Health issues returns "Bad Request" response
    Given request contains "agent_type" parameter with value "process"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:ddoghq/fleet-remediation
  Scenario: List active Agent Health issues returns "OK" response
    Given request contains "agent_type" parameter with value "node"
    When the request is sent
    Then the response status is 200 OK
