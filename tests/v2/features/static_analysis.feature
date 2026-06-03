@endpoint(static-analysis) @endpoint(static-analysis-v2)
Feature: Static Analysis
  API for static analysis

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "StaticAnalysis" API

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule Revision returns "Bad request" response
    Given operation "CreateCustomRuleRevision" enabled
    And new "CreateCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "type": "custom_rule_revision"}}
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule Revision returns "Rule not found" response
    Given operation "CreateCustomRuleRevision" enabled
    And new "CreateCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "type": "custom_rule_revision"}}
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule Revision returns "Successfully created" response
    Given operation "CreateCustomRuleRevision" enabled
    And new "CreateCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "type": "custom_rule_revision"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule returns "Bad request" response
    Given operation "CreateCustomRule" enabled
    And new "CreateCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule returns "Conflict - rule already exists" response
    Given operation "CreateCustomRule" enabled
    And new "CreateCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 409 Conflict - rule already exists

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule returns "Precondition failed - validation error or ruleset not found" response
    Given operation "CreateCustomRule" enabled
    And new "CreateCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 412 Precondition failed - validation error or ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Rule returns "Successfully created" response
    Given operation "CreateCustomRule" enabled
    And new "CreateCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "custom_rule"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Ruleset returns "Bad Request" response
    Given operation "CreateCustomRuleset" enabled
    And new "CreateCustomRuleset" request
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Ruleset returns "Conflict" response
    Given operation "CreateCustomRuleset" enabled
    And new "CreateCustomRuleset" request
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Ruleset returns "OK" response
    Given operation "CreateCustomRuleset" enabled
    And new "CreateCustomRuleset" request
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create Custom Ruleset returns "Precondition Failed" response
    Given operation "CreateCustomRuleset" enabled
    And new "CreateCustomRuleset" request
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 412 Precondition Failed

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule returns "Bad Request" response
    Given operation "CreateAiCustomRule" enabled
    And new "CreateAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-ai-rule"}, "id": "my-ai-rule", "type": "ai_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule returns "Conflict - rule already exists" response
    Given operation "CreateAiCustomRule" enabled
    And new "CreateAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-ai-rule"}, "id": "my-ai-rule", "type": "ai_rule"}}
    When the request is sent
    Then the response status is 409 Conflict - rule already exists

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule returns "Precondition Failed - validation error or ruleset not found" response
    Given operation "CreateAiCustomRule" enabled
    And new "CreateAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-ai-rule"}, "id": "my-ai-rule", "type": "ai_rule"}}
    When the request is sent
    Then the response status is 412 Precondition Failed - validation error or ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule returns "Successfully created" response
    Given operation "CreateAiCustomRule" enabled
    And new "CreateAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-ai-rule"}, "id": "my-ai-rule", "type": "ai_rule"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule revision returns "Bad Request" response
    Given operation "CreateAiCustomRuleRevision" enabled
    And new "CreateAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "SECURITY", "content": "Content", "cwe": "79", "description": "Ruleset description", "directories": [], "execution_mode": "auto", "globs": ["**/*.py"], "is_published": false, "is_testing": false, "severity": "ERROR", "short_description": "Ruleset short description", "version_id": 1}, "id": "revision-abc-123", "type": "ai_rule_revision"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule revision returns "Rule not found" response
    Given operation "CreateAiCustomRuleRevision" enabled
    And new "CreateAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "SECURITY", "content": "Content", "cwe": "79", "description": "Ruleset description", "directories": [], "execution_mode": "auto", "globs": ["**/*.py"], "is_published": false, "is_testing": false, "severity": "ERROR", "short_description": "Ruleset short description", "version_id": 1}, "id": "revision-abc-123", "type": "ai_rule_revision"}}
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom rule revision returns "Successfully created" response
    Given operation "CreateAiCustomRuleRevision" enabled
    And new "CreateAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "SECURITY", "content": "Content", "cwe": "79", "description": "Ruleset description", "directories": [], "execution_mode": "auto", "globs": ["**/*.py"], "is_published": false, "is_testing": false, "severity": "ERROR", "short_description": "Ruleset short description", "version_id": 1}, "id": "revision-abc-123", "type": "ai_rule_revision"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom ruleset returns "Bad Request" response
    Given operation "CreateAiCustomRuleset" enabled
    And new "CreateAiCustomRuleset" request
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom ruleset returns "Conflict - ruleset already exists" response
    Given operation "CreateAiCustomRuleset" enabled
    And new "CreateAiCustomRuleset" request
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 409 Conflict - ruleset already exists

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom ruleset returns "Precondition Failed - validation error" response
    Given operation "CreateAiCustomRuleset" enabled
    And new "CreateAiCustomRuleset" request
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 412 Precondition Failed - validation error

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI custom ruleset returns "Successfully created" response
    Given operation "CreateAiCustomRuleset" enabled
    And new "CreateAiCustomRuleset" request
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI memory violation result returns "Bad Request" response
    Given operation "CreateAiMemoryViolationResult" enabled
    And new "CreateAiMemoryViolationResult" request
    And body with value {"data": {"attributes": {"line": 10, "message": "This is a false positive because the input is sanitized.", "name": "src/main.py", "repository_id": "my-repo", "rule": "my-ai-ruleset/my-ai-rule", "sha": "abc123def456789012345678901234567890abcd", "type": "FP"}, "id": "violation-abc", "type": "ai_memory_violation_result"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI memory violation result returns "Not Found" response
    Given operation "CreateAiMemoryViolationResult" enabled
    And new "CreateAiMemoryViolationResult" request
    And body with value {"data": {"attributes": {"line": 10, "message": "This is a false positive because the input is sanitized.", "name": "src/main.py", "repository_id": "my-repo", "rule": "my-ai-ruleset/my-ai-rule", "sha": "abc123def456789012345678901234567890abcd", "type": "FP"}, "id": "violation-abc", "type": "ai_memory_violation_result"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Create an AI memory violation result returns "Successfully created" response
    Given operation "CreateAiMemoryViolationResult" enabled
    And new "CreateAiMemoryViolationResult" request
    And body with value {"data": {"attributes": {"line": 10, "message": "This is a false positive because the input is sanitized.", "name": "src/main.py", "repository_id": "my-repo", "rule": "my-ai-ruleset/my-ai-rule", "sha": "abc123def456789012345678901234567890abcd", "type": "FP"}, "id": "violation-abc", "type": "ai_memory_violation_result"}}
    When the request is sent
    Then the response status is 200 Successfully created

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Rule returns "Bad request" response
    Given operation "DeleteCustomRule" enabled
    And new "DeleteCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Rule returns "Rule not found" response
    Given operation "DeleteCustomRule" enabled
    And new "DeleteCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Rule returns "Successfully deleted" response
    Given operation "DeleteCustomRule" enabled
    And new "DeleteCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully deleted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Ruleset returns "Bad request" response
    Given operation "DeleteCustomRuleset" enabled
    And new "DeleteCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Ruleset returns "Ruleset not found" response
    Given operation "DeleteCustomRuleset" enabled
    And new "DeleteCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete Custom Ruleset returns "Successfully deleted" response
    Given operation "DeleteCustomRuleset" enabled
    And new "DeleteCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully deleted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom rule returns "Bad Request" response
    Given operation "DeleteAiCustomRule" enabled
    And new "DeleteAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom rule returns "Rule not found" response
    Given operation "DeleteAiCustomRule" enabled
    And new "DeleteAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom rule returns "Successfully deleted" response
    Given operation "DeleteAiCustomRule" enabled
    And new "DeleteAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully deleted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom ruleset returns "Bad Request" response
    Given operation "DeleteAiCustomRuleset" enabled
    And new "DeleteAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom ruleset returns "Ruleset not found" response
    Given operation "DeleteAiCustomRuleset" enabled
    And new "DeleteAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI custom ruleset returns "Successfully deleted" response
    Given operation "DeleteAiCustomRuleset" enabled
    And new "DeleteAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully deleted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI memory violation result returns "Bad Request" response
    Given operation "DeleteAiMemoryViolationResult" enabled
    And new "DeleteAiMemoryViolationResult" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI memory violation result returns "Memory violation result not found" response
    Given operation "DeleteAiMemoryViolationResult" enabled
    And new "DeleteAiMemoryViolationResult" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Memory violation result not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Delete an AI memory violation result returns "Successfully deleted" response
    Given operation "DeleteAiMemoryViolationResult" enabled
    And new "DeleteAiMemoryViolationResult" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully deleted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule returns "Bad Request" response
    Given operation "GetAiCustomRule" enabled
    And new "GetAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule returns "Rule not found" response
    Given operation "GetAiCustomRule" enabled
    And new "GetAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule returns "Successful response" response
    Given operation "GetAiCustomRule" enabled
    And new "GetAiCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule revision returns "Bad Request" response
    Given operation "GetAiCustomRuleRevision" enabled
    And new "GetAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule revision returns "Revision not found" response
    Given operation "GetAiCustomRuleRevision" enabled
    And new "GetAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Revision not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom rule revision returns "Successful response" response
    Given operation "GetAiCustomRuleRevision" enabled
    And new "GetAiCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom ruleset returns "Bad Request" response
    Given operation "GetAiCustomRuleset" enabled
    And new "GetAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom ruleset returns "Ruleset not found" response
    Given operation "GetAiCustomRuleset" enabled
    And new "GetAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get an AI custom ruleset returns "Successful response" response
    Given operation "GetAiCustomRuleset" enabled
    And new "GetAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Get the list of SPDX licenses returns "OK" response
    Given operation "ListSCALicenses" enabled
    And new "ListSCALicenses" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI custom rule revisions returns "Bad Request" response
    Given operation "ListAiCustomRuleRevisions" enabled
    And new "ListAiCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI custom rule revisions returns "Rule not found" response
    Given operation "ListAiCustomRuleRevisions" enabled
    And new "ListAiCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI custom rule revisions returns "Successful response" response
    Given operation "ListAiCustomRuleRevisions" enabled
    And new "ListAiCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast @with-pagination
  Scenario: List AI custom rule revisions returns "Successful response" response with pagination
    Given operation "ListAiCustomRuleRevisions" enabled
    And new "ListAiCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI custom rulesets returns "Successful response" response
    Given operation "ListAiCustomRulesets" enabled
    And new "ListAiCustomRulesets" request
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI memory violation results returns "Bad Request" response
    Given operation "ListAiMemoryViolationResults" enabled
    And new "ListAiMemoryViolationResults" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI memory violation results returns "Not Found" response
    Given operation "ListAiMemoryViolationResults" enabled
    And new "ListAiMemoryViolationResults" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI memory violation results returns "Successful response" response
    Given operation "ListAiMemoryViolationResults" enabled
    And new "ListAiMemoryViolationResults" request
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI prompts returns "Bad Request" response
    Given operation "ListAiPrompts" enabled
    And new "ListAiPrompts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI prompts returns "Not Found" response
    Given operation "ListAiPrompts" enabled
    And new "ListAiPrompts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List AI prompts returns "Successful response" response
    Given operation "ListAiPrompts" enabled
    And new "ListAiPrompts" request
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List Custom Rule Revisions returns "Bad request" response
    Given operation "ListCustomRuleRevisions" enabled
    And new "ListCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List Custom Rule Revisions returns "Rule not found" response
    Given operation "ListCustomRuleRevisions" enabled
    And new "ListCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List Custom Rule Revisions returns "Successful response" response
    Given operation "ListCustomRuleRevisions" enabled
    And new "ListCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast @with-pagination
  Scenario: List Custom Rule Revisions returns "Successful response" response with pagination
    Given operation "ListCustomRuleRevisions" enabled
    And new "ListCustomRuleRevisions" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List Custom Rulesets returns "OK" response
    Given operation "ListCustomRulesets" enabled
    And new "ListCustomRulesets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: POST request to resolve vulnerable symbols returns "OK" response
    Given operation "CreateSCAResolveVulnerableSymbols" enabled
    And new "CreateSCAResolveVulnerableSymbols" request
    And body with value {"data": {"attributes": {"purls": []}, "type": "resolve-vulnerable-symbols-request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Post dependencies for analysis returns "OK" response
    Given operation "CreateSCAResult" enabled
    And new "CreateSCAResult" request
    And body with value {"data": {"attributes": {"commit": {}, "dependencies": [{"exclusions": [], "locations": [{"block": {"end": {}, "start": {}}, "name": {"end": {}, "start": {}}, "namespace": {"end": {}, "start": {}}, "version": {"end": {}, "start": {}}}], "reachable_symbol_properties": [{}]}], "files": [{}], "relations": [{"depends_on": []}], "repository": {}, "vulnerabilities": [{"affects": [{}]}]}, "type": "scarequests"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Retrieve a dependency scan result returns "Not Found" response
    Given operation "GetSCAScan" enabled
    And new "GetSCAScan" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Retrieve a dependency scan result returns "OK" response
    Given operation "GetSCAScan" enabled
    And new "GetSCAScan" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Revert Custom Rule Revision returns "Bad request" response
    Given operation "RevertCustomRuleRevision" enabled
    And new "RevertCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "revert_custom_rule_revision_request"}}
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Revert Custom Rule Revision returns "Successfully reverted" response
    Given operation "RevertCustomRuleRevision" enabled
    And new "RevertCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "revert_custom_rule_revision_request"}}
    When the request is sent
    Then the response status is 200 Successfully reverted

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule Revision returns "Bad request" response
    Given operation "GetCustomRuleRevision" enabled
    And new "GetCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule Revision returns "Revision not found" response
    Given operation "GetCustomRuleRevision" enabled
    And new "GetCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Revision not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule Revision returns "Successful response" response
    Given operation "GetCustomRuleRevision" enabled
    And new "GetCustomRuleRevision" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule returns "Bad request" response
    Given operation "GetCustomRule" enabled
    And new "GetCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule returns "Rule not found" response
    Given operation "GetCustomRule" enabled
    And new "GetCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Rule not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Rule returns "Successful response" response
    Given operation "GetCustomRule" enabled
    And new "GetCustomRule" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And request contains "rule_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Ruleset returns "Bad request" response
    Given operation "GetCustomRuleset" enabled
    And new "GetCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Ruleset returns "Ruleset not found" response
    Given operation "GetCustomRuleset" enabled
    And new "GetCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Show Custom Ruleset returns "Successful response" response
    Given operation "GetCustomRuleset" enabled
    And new "GetCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful response

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Submit libraries for vulnerability scanning returns "Accepted" response
    Given operation "CreateSCAScan" enabled
    And new "CreateSCAScan" request
    And body with value {"data": {"attributes": {"commit_hash": "0e9fc8de83eaabecd722e1cd0ed44fb489fe15fc", "libraries": [{"exclusions": [], "is_dev": false, "is_direct": true, "package_manager": "nuget", "purl": "pkg:nuget/Newtonsoft.Json@13.0.1", "target_frameworks": []}], "resource_name": "my-org/my-repo"}, "type": "mcpscanrequest"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/k9-vm-sca
  Scenario: Submit libraries for vulnerability scanning returns "Bad Request" response
    Given operation "CreateSCAScan" enabled
    And new "CreateSCAScan" request
    And body with value {"data": {"attributes": {"commit_hash": "0e9fc8de83eaabecd722e1cd0ed44fb489fe15fc", "libraries": [{"exclusions": [], "is_dev": false, "is_direct": true, "package_manager": "nuget", "purl": "pkg:nuget/Newtonsoft.Json@13.0.1", "target_frameworks": []}], "resource_name": "my-org/my-repo"}, "type": "mcpscanrequest"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update Custom Ruleset returns "Bad request" response
    Given operation "UpdateCustomRuleset" enabled
    And new "UpdateCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update Custom Ruleset returns "Precondition failed - validation error or ruleset not found" response
    Given operation "UpdateCustomRuleset" enabled
    And new "UpdateCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 412 Precondition failed - validation error or ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update Custom Ruleset returns "Successfully updated" response
    Given operation "UpdateCustomRuleset" enabled
    And new "UpdateCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rules": [{"created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "last_revision": {"attributes": {"arguments": [{"description": "YXJndW1lbnQgZGVzY3JpcHRpb24=", "name": "YXJndW1lbnRfbmFtZQ=="}], "category": "SECURITY", "checksum": "8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99", "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "created_at": "2026-01-09T13:00:57.473141Z", "created_by": "foobarbaz", "creation_message": "Initial revision", "cve": "CVE-2024-1234", "cwe": "CWE-79", "description": "bG9uZyBkZXNjcmlwdGlvbg==", "documentation_url": "https://docs.example.com/rules/my-rule", "is_published": false, "is_testing": false, "language": "PYTHON", "severity": "ERROR", "short_description": "c2hvcnQgZGVzY3JpcHRpb24=", "should_use_ai_fix": false, "tags": ["security", "custom"], "tests": [{"annotation_count": 1, "code": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==", "filename": "test.yaml"}], "tree_sitter_query": "Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ=="}, "id": "revision-123", "type": "custom_rule_revision"}, "name": "my-rule"}]}, "type": "custom_ruleset"}}
    When the request is sent
    Then the response status is 200 Successfully updated

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update an AI custom ruleset returns "Bad Request" response
    Given operation "UpdateAiCustomRuleset" enabled
    And new "UpdateAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update an AI custom ruleset returns "Precondition Failed - validation error or ruleset not found" response
    Given operation "UpdateAiCustomRuleset" enabled
    And new "UpdateAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 412 Precondition Failed - validation error or ruleset not found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Update an AI custom ruleset returns "Successfully updated" response
    Given operation "UpdateAiCustomRuleset" enabled
    And new "UpdateAiCustomRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Ruleset description", "name": "my-ai-ruleset", "short_description": "Ruleset short description"}, "id": "my-ai-ruleset", "type": "ai_ruleset"}}
    When the request is sent
    Then the response status is 200 Successfully updated
