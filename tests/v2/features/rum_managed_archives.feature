@endpoint(rum-config) @endpoint(rum-config-v2) @endpoint(rum-managed-archives) @endpoint(rum-managed-archives-v2)
Feature: RUM Managed Archives
  Configure Managed Archives for RUM applications. Your organization must
  have Managed Archives enabled.  Requires `rum_rehydration_filter_read` to
  list or get configurations, or `rum_rehydration_filter_write` to create,
  update, or delete them.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMManagedArchives" API

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "Bad Request" response
    Given new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 90}, "id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "Not Found" response
    Given new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 90}, "id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "OK" response
    Given new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 90}, "id": "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "Bad Request" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "No Content" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "Not Found" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete an unknown archive configuration returns "Not Found" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "Bad Request" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "Not Found" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "OK" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get an unknown archive configuration returns "Not Found" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1

  @skip-go @skip-java @skip-python @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get archive configuration rejects an invalid application ID
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-python @skip-ruby @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List archive configurations rejects an invalid page size
    Given new "ListRUMArchiveConfigs" request
    And request contains "page[size]" parameter with value 101
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/rum-backend
  Scenario: List archive configurations returns "Bad Request" response
    Given new "ListRUMArchiveConfigs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List archive configurations returns "OK" response
    Given new "ListRUMArchiveConfigs" request
    And request contains "page[number]" parameter with value 0
    And request contains "page[size]" parameter with value 1
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page" has field "total_filtered_count"

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Update archive configuration with unsupported enabled retention returns "Bad Request" response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter with value "{{ rum_application.data.id }}"
    And body with value {"data":{"id":"{{ rum_application.data.id }}","type":"rum_archive_config","attributes":{"enabled":true,"retention_days":31}}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
