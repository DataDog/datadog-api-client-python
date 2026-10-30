@endpoint(ai-guard) @endpoint(ai-guard-v2)
Feature: AI Guard
  Evaluate LLM interactions for security threats such as prompt injection
  and jailbreak attempts.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AIGuard" API
    And operation "EvaluateAIGuardRequest" enabled
    And new "EvaluateAIGuardRequest" request

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request rejects empty multipart user content
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user","content":[]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request rejects image parts without a URL
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user","content":[{"type":"image_url","image_url":{"url":""}}]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request rejects text parts without text
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user","content":[{"type":"text"}]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "Bad Request" response
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user"}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "OK" response
    Given body with value {"data": {"type": "evaluations", "attributes": {"messages": [{"content": "Hello world!", "role": "user"}], "meta": {"confidence_threshold": 0.8}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "Payload Too Large" response
    Given body with value {"data": {"attributes": {"messages": [{"content": "Hello world!", "role": "user"}], "meta": {"confidence_threshold": 0.8}}, "type": "evaluations"}}
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request returns "Request Timeout" response
    Given body with value {"data": {"attributes": {"messages": [{"content": "Hello world!", "role": "user"}], "meta": {"confidence_threshold": 0.8}}, "type": "evaluations"}}
    When the request is sent
    Then the response status is 408 Request Timeout

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request with a numeric confidence threshold
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user","content":"Hello world!"}],"meta":{"confidence_threshold":0.8}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "evaluations"
    And the response "data.attributes" has field "action"
    And the response "data.attributes" has field "is_blocking_enabled"

  @team:ddoghq/k9-ai-guard
  Scenario: Evaluate an AI Guard request with per-category confidence thresholds
    Given body with value {"data":{"type":"evaluations","attributes":{"messages":[{"role":"user","content":"Hello world!"}],"meta":{"confidence_threshold":{"flagging_global":0.6,"policy-evasion":0.9,"indirect-prompt-injection":0.4}}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "evaluations"
    And the response "data.attributes" has field "action"
    And the response "data.attributes" has field "is_blocking_enabled"
