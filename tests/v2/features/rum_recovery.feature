@endpoint(rum-config) @endpoint(rum-config-v2) @endpoint(rum-recovery) @endpoint(rum-recovery-v2)
Feature: RUM Recovery
  Search archived RUM sessions and recover individual sessions or query-
  based batches. Your organization must have Managed Archives enabled.
  Creating, counting, listing, and canceling batches also require batch
  recovery enablement.  Requires `rum_rehydration_filter_read` for search
  and request details, or `rum_rehydration_index` to create, estimate
  recoverable sessions, list batches, or cancel recovery requests.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRecovery" API

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Cancel a batch recovery request returns "Bad Request" response
    Given new "UpdateRUMRecoveryBatchRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "cancelled"}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Cancel a batch recovery request returns "Conflict" response
    Given new "UpdateRUMRecoveryBatchRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "cancelled"}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Cancel a batch recovery request returns "Not Found" response
    Given new "UpdateRUMRecoveryBatchRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "cancelled"}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Cancel a batch recovery request returns "OK" response
    Given new "UpdateRUMRecoveryBatchRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "cancelled"}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Cancel an unknown batch recovery returns "Not Found" response
    Given new "UpdateRUMRecoveryBatchRequest" request
    And request contains "request_id" parameter with value "{{ uuid }}"
    And body with value {"data":{"type":"rum_recovery_request","attributes":{"status":"cancelled"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Count recoverable sessions accepts exactly 180 days
    Given new "GetRUMRecoverySessionCount" request
    And body with value {"data":{"type":"rum_recovery_count","attributes":{"query":"service:rum18600-fixture","from":{{ timestamp("now - 180d") }}000,"to":{{ timestamp("now") }}000}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "rum_recovery_count"
    And the response "data.attributes" has field "estimated_count"
    And the response "data.attributes" has field "max_recoverable_sessions"

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Count recoverable sessions rejects a range wider than 180 days
    Given new "GetRUMRecoverySessionCount" request
    And body with value {"data":{"type":"rum_recovery_count","attributes":{"query":"service:rum18600-fixture","from":{{ timestamp("now - 181d") }}000,"to":{{ timestamp("now") }}000}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create a recovery request returns "Accepted" response
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data": {"attributes": {"request_type": "sessions", "sessions": [{"application_id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "session_id": "00000000-0000-4000-8000-000000000001"}]}, "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create a recovery request returns "Bad Request" response
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data": {"attributes": {"request_type": "sessions", "sessions": [{"application_id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "session_id": "00000000-0000-4000-8000-000000000001"}]}, "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create a recovery request returns "Conflict. Targeted sessions are already retained, in flight, or previously failed, or a concurrent batch was created." response
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data": {"attributes": {"request_type": "sessions", "sessions": [{"application_id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "session_id": "00000000-0000-4000-8000-000000000001"}]}, "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 409 Conflict. Targeted sessions are already retained, in flight, or previously failed, or a concurrent batch was created.

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create a recovery request returns "Not Found" response
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data": {"attributes": {"request_type": "sessions", "sessions": [{"application_id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "session_id": "00000000-0000-4000-8000-000000000001"}]}, "type": "rum_recovery_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-go @skip-ruby @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create batch recovery rejects a range wider than 180 days
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data":{"type":"rum_recovery_request","attributes":{"request_type":"batch","query":"service:rum18600-fixture","from":{{ timestamp("now - 181d") }}000,"to":{{ timestamp("now") }}000}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-go @skip-ruby @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create targeted recovery rejects an empty sessions array
    Given new "CreateRUMRecoveryRequest" request
    And body with value {"data":{"type":"rum_recovery_request","attributes":{"sessions":[]}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Estimate recoverable sessions returns "Bad Request" response
    Given new "GetRUMRecoverySessionCount" request
    And body with value {"data": {"attributes": {"from": 1789905600000, "query": "service:web", "to": 1789992000000}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_count"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Estimate recoverable sessions returns "Not Found" response
    Given new "GetRUMRecoverySessionCount" request
    And body with value {"data": {"attributes": {"from": 1789905600000, "query": "service:web", "to": 1789992000000}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_count"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Estimate recoverable sessions returns "OK" response
    Given new "GetRUMRecoverySessionCount" request
    And body with value {"data": {"attributes": {"from": 1789905600000, "query": "service:web", "to": 1789992000000}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_recovery_count"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get an unknown recovery request returns "Not Found" response
    Given new "GetRUMRecoveryRequest" request
    And request contains "request_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get recovery request progress returns "Bad Request" response
    Given new "GetRUMRecoveryRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get recovery request progress returns "Not Found" response
    Given new "GetRUMRecoveryRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get recovery request progress returns "OK" response
    Given new "GetRUMRecoveryRequest" request
    And request contains "request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List batch history filters request creation time independently of session time
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter with value "batch"
    And request contains "from" parameter with value 1
    And request contains "to" parameter with value 2
    And request contains "query" parameter with value "service:rum18600-fixture AND @usr.id:(123 OR 456)"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
    And the response "meta" does not have field "next_cursor"

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List batch history rejects OR between filter terms
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter with value "batch"
    And request contains "query" parameter with value "service:web OR @usr.id:123"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List batch history rejects an invalid cursor
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter with value "batch"
    And request contains "cursor" parameter with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List batch history rejects equal creation-time bounds
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter with value "batch"
    And request contains "from" parameter with value 1789905600000
    And request contains "to" parameter with value 1789905600000
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: List batch recovery requests returns "Bad Request" response
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: List batch recovery requests returns "Not Found" response
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: List batch recovery requests returns "OK" response
    Given new "ListRUMRecoveryBatchRequests" request
    And request contains "type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Search archived sessions rejects an empty query
    Given new "SearchRUMArchiveSessions" request
    And body with value {"data":{"type":"rum_archive_sessions_request","attributes":{"query":"","from":1789905600000,"to":1789992000000}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Search archived sessions returns "Bad Request" response
    Given new "SearchRUMArchiveSessions" request
    And body with value {"data": {"attributes": {"cursor": "example", "from": 1789905600000, "hide_retained": false, "limit": 0, "query": "service:web", "to": 1789992000000}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_archive_sessions_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Search archived sessions returns "OK" response
    Given new "SearchRUMArchiveSessions" request
    And body with value {"data": {"attributes": {"cursor": "example", "from": 1789905600000, "hide_retained": false, "limit": 0, "query": "service:web", "to": 1789992000000}, "id": "11111111-1111-4111-8111-111111111111", "type": "rum_archive_sessions_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Search archived sessions returns canonical data and first-page metadata
    Given new "SearchRUMArchiveSessions" request
    And body with value {"data":{"type":"rum_archive_sessions_request","attributes":{"query":"service:rum18600-fixture","from":{{ timestamp("now - 7d") }}000,"to":{{ timestamp("now") }}000,"limit":1}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page" has field "total_count"
