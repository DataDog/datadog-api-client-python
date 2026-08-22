@endpoint(data-deletion) @endpoint(data-deletion-v2)
Feature: Data Deletion
  The Data Deletion API allows the user to target and delete data from the
  allowed products. It's enabled for Logs and depends on the
  `logs_delete_data` permission.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DataDeletion" API

  @replay-only @team:DataDog/governance-tooling-and-systems
  Scenario: Cancels a data deletion request returns "Bad Request" response
    Given new "CancelDataDeletionRequest" request
    And request contains "id" parameter with value "id-1"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/governance-tooling-and-systems
  Scenario: Cancels a data deletion request returns "OK" response
    Given there is a valid "deletion_request" in the system
    And new "CancelDataDeletionRequest" request
    And request contains "id" parameter from "deletion_request.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ deletion_request.data.id }}"
    And the response "data.type" is equal to "{{ deletion_request.data.type }}"
    And the response "data.attributes.product" is equal to "{{ deletion_request.data.attributes.product }}"
    And the response "data.attributes.status" is equal to "canceled"

  @replay-only @team:DataDog/governance-tooling-and-systems
  Scenario: Cancels a data deletion request returns "Precondition failed error" response
    Given new "CancelDataDeletionRequest" request
    And request contains "id" parameter with value "-1"
    When the request is sent
    Then the response status is 412 Precondition failed error

  @generated @skip @team:DataDog/governance-tooling-and-systems
  Scenario: Creates a data deletion request returns "Bad Request" response
    Given new "CreateDataDeletionRequest" request
    And request contains "product" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"displayed_total": 100, "from": 1672527600000, "indexes": ["test-index", "test-index-2"], "query": {"host": "abc", "service": "xyz"}, "to": 1704063600000}, "type": "create_deletion_req"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/governance-tooling-and-systems
  Scenario: Creates a data deletion request returns "OK" response
    Given new "CreateDataDeletionRequest" request
    And request contains "product" parameter with value "logs"
    And body with value {"data": {"attributes": {"displayed_total": 100, "from": 1672527600000, "indexes": ["test-index", "test-index-2"], "query": {"host": "abc", "service": "xyz"}, "to": 1704063600000}, "type": "create_deletion_req"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "deletion_request"
    And the response "data.attributes.product" is equal to "logs"
    And the response "data.attributes.status" is equal to "pending"

  @replay-only @team:DataDog/governance-tooling-and-systems
  Scenario: Creates a data deletion request returns "Precondition failed error" response
    Given new "CreateDataDeletionRequest" request
    And request contains "product" parameter with value "logs"
    And body with value {"data": {"attributes": {"displayed_total": 100, "from": 1672527600000, "indexes": ["test-index", "test-index-2"], "query": {}, "to": 1704063600000}, "type": "create_deletion_req"}}
    When the request is sent
    Then the response status is 412 Precondition failed error

  @generated @skip @team:DataDog/governance-tooling-and-systems
  Scenario: Gets a list of data deletion requests returns "Bad Request" response
    Given new "GetDataDeletionRequests" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/governance-tooling-and-systems
  Scenario: Gets a list of data deletion requests returns "OK" response
    Given there is a valid "deletion_request" in the system
    And new "GetDataDeletionRequests" request
    When the request is sent
    Then the response status is 200 OK
