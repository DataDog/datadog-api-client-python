@endpoint(csm-ownership) @endpoint(csm-ownership-v2)
Feature: CSM Ownership
  Datadog Cloud Security Management (CSM) Ownership infers the most likely
  owner for a cloud resource by combining ownership signals from across the
  platform, and lets you review the inference, inspect its evidence, and
  submit feedback to persist, override, or correct the inferred owner. For
  more information, see [Cloud Security Management](https://docs.datadoghq.c
  om/security/cloud_security_management).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CSMOwnership" API

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Count untagged findings by ownership confidence returns "OK" response
    Given operation "GetOwnershipUntaggedFindings" enabled
    And new "GetOwnershipUntaggedFindings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get an ownership inference by owner type returns "Bad Request" response
    Given operation "GetOwnershipInference" enabled
    And new "GetOwnershipInference" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get an ownership inference by owner type returns "Not Found" response
    Given operation "GetOwnershipInference" enabled
    And new "GetOwnershipInference" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get an ownership inference by owner type returns "OK" response
    Given operation "GetOwnershipInference" enabled
    And new "GetOwnershipInference" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get ownership settings for the org returns "OK" response
    Given operation "GetOwnershipSettings" enabled
    And new "GetOwnershipSettings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get the evidence for an ownership inference returns "Bad Request" response
    Given operation "GetOwnershipEvidence" enabled
    And new "GetOwnershipEvidence" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get the evidence for an ownership inference returns "Not Found" response
    Given operation "GetOwnershipEvidence" enabled
    And new "GetOwnershipEvidence" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get the evidence for an ownership inference returns "OK" response
    Given operation "GetOwnershipEvidence" enabled
    And new "GetOwnershipEvidence" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership history by owner type returns "Bad Request" response
    Given operation "ListOwnershipHistoryByOwnerType" enabled
    And new "ListOwnershipHistoryByOwnerType" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership history by owner type returns "OK" response
    Given operation "ListOwnershipHistoryByOwnerType" enabled
    And new "ListOwnershipHistoryByOwnerType" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership inference history for a resource returns "Bad Request" response
    Given operation "ListOwnershipHistory" enabled
    And new "ListOwnershipHistory" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership inference history for a resource returns "OK" response
    Given operation "ListOwnershipHistory" enabled
    And new "ListOwnershipHistory" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership inferences for a resource returns "Bad Request" response
    Given operation "ListOwnershipInferences" enabled
    And new "ListOwnershipInferences" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership inferences for a resource returns "Not Found" response
    Given operation "ListOwnershipInferences" enabled
    And new "ListOwnershipInferences" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List ownership inferences for a resource returns "OK" response
    Given operation "ListOwnershipInferences" enabled
    And new "ListOwnershipInferences" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Submit feedback on an ownership inference returns "Bad Request" response
    Given operation "CreateOwnershipFeedback" enabled
    And new "CreateOwnershipFeedback" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": "confirm", "actor_handle": "user@example.com", "actor_type": "user", "corrected_owner_handle": "team-b", "corrected_owner_type": "team", "inference_checksum": "abc123", "reason": "Confirmed by team lead."}, "type": "ownership_feedback"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Submit feedback on an ownership inference returns "Conflict" response
    Given operation "CreateOwnershipFeedback" enabled
    And new "CreateOwnershipFeedback" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": "confirm", "actor_handle": "user@example.com", "actor_type": "user", "corrected_owner_handle": "team-b", "corrected_owner_type": "team", "inference_checksum": "abc123", "reason": "Confirmed by team lead."}, "type": "ownership_feedback"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Submit feedback on an ownership inference returns "Created" response
    Given operation "CreateOwnershipFeedback" enabled
    And new "CreateOwnershipFeedback" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": "confirm", "actor_handle": "user@example.com", "actor_type": "user", "corrected_owner_handle": "team-b", "corrected_owner_type": "team", "inference_checksum": "abc123", "reason": "Confirmed by team lead."}, "type": "ownership_feedback"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Submit feedback on an ownership inference returns "Not Found" response
    Given operation "CreateOwnershipFeedback" enabled
    And new "CreateOwnershipFeedback" request
    And request contains "resource_id" parameter from "REPLACE.ME"
    And request contains "owner_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": "confirm", "actor_handle": "user@example.com", "actor_type": "user", "corrected_owner_handle": "team-b", "corrected_owner_type": "team", "inference_checksum": "abc123", "reason": "Confirmed by team lead."}, "type": "ownership_feedback"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Update ownership settings for the org returns "Bad Request" response
    Given operation "PostOwnershipSettings" enabled
    And new "PostOwnershipSettings" request
    And body with value {"data": {"attributes": {"auto_tag": true, "confidence_level": "high"}, "type": "ownership_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Update ownership settings for the org returns "OK" response
    Given operation "PostOwnershipSettings" enabled
    And new "PostOwnershipSettings" request
    And body with value {"data": {"attributes": {"auto_tag": true, "confidence_level": "high"}, "type": "ownership_settings"}}
    When the request is sent
    Then the response status is 200 OK
