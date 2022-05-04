@endpoint(logs-archives) @endpoint(logs-archives-v2)
Feature: Logs Archives
  Archives forward all the logs ingested to a cloud storage system.  See the
  [Archives Page](https://app.datadoghq.com/logs/pipelines/archives) for a
  list of the archives currently configured in web UI.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsArchives" API

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create an archive returns "Bad Request" response
    Given new "CreateLogsArchive" request
    And body with value {"data": {"attributes": {"destination": {"container": "container-name", "integration": {"client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storage_account": "account-name", "type": "azure"}, "include_tags": false, "name": "Nginx Archive", "query": "source:nginx", "rehydration_max_scan_size_in_gb": 100, "rehydration_tags": ["team:intake", "team:app"]}, "type": "archives"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create an archive returns "OK" response
    Given new "CreateLogsArchive" request
    And body with value {"data": {"attributes": {"destination": {"container": "container-name", "integration": {"client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storage_account": "account-name", "type": "azure"}, "include_tags": false, "name": "Nginx Archive", "query": "source:nginx", "rehydration_max_scan_size_in_gb": 100, "rehydration_tags": ["team:intake", "team:app"]}, "type": "archives"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Delete an archive returns "Bad Request" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Delete an archive returns "Not found" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: Delete an archive returns "OK" response
    Given new "DeleteLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get all archives returns "OK" response
    Given new "ListLogsArchives" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get an archive returns "Bad Request" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get an archive returns "Not found" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get an archive returns "OK" response
    Given new "GetLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get archive order returns "OK" response
    Given new "GetLogsArchiveOrder" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Grant role to an archive returns "Bad Request" response
    Given new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Grant role to an archive returns "Not found" response
    Given new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: Grant role to an archive returns "OK" response
    Given new "AddReadRoleToArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: List read roles for an archive returns "Bad Request" response
    Given new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: List read roles for an archive returns "Not found" response
    Given new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: List read roles for an archive returns "OK" response
    Given new "ListArchiveReadRoles" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Revoke role from an archive returns "Bad Request" response
    Given new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Revoke role from an archive returns "Not found" response
    Given new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: Revoke role from an archive returns "OK" response
    Given new "RemoveRoleFromArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update an archive returns "Bad Request" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"destination": {"container": "container-name", "integration": {"client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storage_account": "account-name", "type": "azure"}, "include_tags": false, "name": "Nginx Archive", "query": "source:nginx", "rehydration_max_scan_size_in_gb": 100, "rehydration_tags": ["team:intake", "team:app"]}, "type": "archives"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update an archive returns "Not found" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"destination": {"container": "container-name", "integration": {"client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storage_account": "account-name", "type": "azure"}, "include_tags": false, "name": "Nginx Archive", "query": "source:nginx", "rehydration_max_scan_size_in_gb": 100, "rehydration_tags": ["team:intake", "team:app"]}, "type": "archives"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update an archive returns "OK" response
    Given new "UpdateLogsArchive" request
    And request contains "archive_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"destination": {"container": "container-name", "integration": {"client_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenant_id": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storage_account": "account-name", "type": "azure"}, "include_tags": false, "name": "Nginx Archive", "query": "source:nginx", "rehydration_max_scan_size_in_gb": 100, "rehydration_tags": ["team:intake", "team:app"]}, "type": "archives"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update archive order returns "Bad Request" response
    Given new "UpdateLogsArchiveOrder" request
    And body with value {"data": {"attributes": {"archive_ids": ["a2zcMylnM4OCHpYusxIi1g", "a2zcMylnM4OCHpYusxIi2g", "a2zcMylnM4OCHpYusxIi3g"]}, "type": "archive_order"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update archive order returns "OK" response
    Given new "UpdateLogsArchiveOrder" request
    And body with value {"data": {"attributes": {"archive_ids": ["a2zcMylnM4OCHpYusxIi1g", "a2zcMylnM4OCHpYusxIi2g", "a2zcMylnM4OCHpYusxIi3g"]}, "type": "archive_order"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update archive order returns "Unprocessable Entity" response
    Given new "UpdateLogsArchiveOrder" request
    And body with value {"data": {"attributes": {"archive_ids": ["a2zcMylnM4OCHpYusxIi1g", "a2zcMylnM4OCHpYusxIi2g", "a2zcMylnM4OCHpYusxIi3g"]}, "type": "archive_order"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
