@endpoint(ai-impact) @endpoint(ai-impact-v2)
Feature: AI Impact
  Send AI coding tool usage data to measure the impact of AI tools on
  software delivery.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "AIImpact" API
    And new "CreateAIImpactUserActivity" request
    And body with value {"data": [{"attributes": {"day": "2026-05-26", "is_active": true, "models": ["claude-sonnet-4.5", "gpt-5"], "tools": ["Claude Code", "Cursor"], "user_email": "user@example.com"}, "type": "ai_impact_user_activity"}]}

  @generated @skip @team:ddoghq/ci-app-backend
  Scenario: Send AI tool user activity returns "Bad Request: the batch is empty, has more than 1,000 entries, or contains an invalid entry." response
    When the request is sent
    Then the response status is 400 Bad Request: the batch is empty, has more than 1,000 entries, or contains an invalid entry.

  @generated @skip @team:ddoghq/ci-app-backend
  Scenario: Send AI tool user activity returns "OK" response
    When the request is sent
    Then the response status is 200 OK
