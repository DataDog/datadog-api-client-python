@endpoint(ai-guard) @endpoint(ai-guard-v2)
Feature: AI Guard
  Analyze AI conversations for security threats including prompt injection,
  jailbreak attempts, and other AI-specific attacks.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AIGuard" API
    And new "EvaluateAIGuardRequest" request
    And body with value {"messages": [{"content": "How do I delete all files on the system?", "role": "user"}], "meta": {"env": "production", "service": "my-llm-service"}}

  @generated @skip @team:DataDog/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "Evaluation result with action recommendation" response
    When the request is sent
    Then the response status is 200 Evaluation result with action recommendation
