@endpoint(logs-archives)
Feature: Logs Archives
  Archives forward all the logs ingested to a cloud storage system.  See the
  [Archives Page](https://app.datadoghq.com/logs/pipelines/archives) for a
  list of the archives currently configured in our UI.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsArchives" API

  @generated @skip
  Scenario: Get all archives returns "OK" response
    Given new "ListLogsArchives" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create an archive returns "OK" response
    Given new "CreateLogsArchive" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an archive returns "OK" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get an archive returns "OK" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an archive returns "OK" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Revoke role from an archive returns "OK" response
    Given operation "RemoveRoleFromArchive" enabled
    And new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: List read roles for an archive returns "OK" response
    Given operation "ListArchiveReadRoles" enabled
    And new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Grant role to an archive returns "OK" response
    Given operation "AddReadRoleToArchive" enabled
    And new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get archive order returns "OK" response
    Given new "GetLogsArchiveOrder" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update archive order returns "OK" response
    Given new "UpdateLogsArchiveOrder" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update archive order returns "Bad Request" response
    Given new "UpdateLogsArchiveOrder" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update archive order returns "Unprocessable Entity" response
    Given new "UpdateLogsArchiveOrder" request
    And body {}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip
  Scenario: Create an archive returns "Bad Request" response
    Given new "CreateLogsArchive" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete an archive returns "Bad Request" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete an archive returns "Not found" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Get an archive returns "Bad Request" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get an archive returns "Not found" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Update an archive returns "Bad Request" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an archive returns "Not found" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Revoke role from an archive returns "Bad Request" response
    Given operation "RemoveRoleFromArchive" enabled
    And new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Revoke role from an archive returns "Not found" response
    Given operation "RemoveRoleFromArchive" enabled
    And new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: List read roles for an archive returns "Bad Request" response
    Given operation "ListArchiveReadRoles" enabled
    And new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: List read roles for an archive returns "Not found" response
    Given operation "ListArchiveReadRoles" enabled
    And new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Grant role to an archive returns "Bad Request" response
    Given operation "AddReadRoleToArchive" enabled
    And new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Grant role to an archive returns "Not found" response
    Given operation "AddReadRoleToArchive" enabled
    And new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not found
