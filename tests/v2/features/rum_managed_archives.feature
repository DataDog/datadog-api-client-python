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

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "Bad Request" response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 31}, "id": "{{ rum_application.data.id }}", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "Not Found" response
    Given new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 90}, "id": "00000000-0000-0000-0000-000000000000", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update an archive configuration returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "UpdateRUMArchiveConfig" request
    And request contains "app_id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "retention_days": 90}, "id": "{{ rum_application.data.id }}", "type": "rum_archive_config"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_application.data.id }}"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.retention_days" is equal to 90

  @skip-go @skip-java @skip-python @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "Bad Request" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "No Content" response
    Given there is a valid "rum_application" in the system
    And there is a valid "rum_archive_config" in the system
    And new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete an archive configuration returns "Not Found" response
    Given new "DeleteRUMArchiveConfig" request
    And request contains "app_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-go @skip-java @skip-python @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "Bad Request" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "Not Found" response
    Given new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get an archive configuration returns "OK" response
    Given there is a valid "rum_application" in the system
    And there is a valid "rum_archive_config" in the system
    And new "GetRUMArchiveConfig" request
    And request contains "app_id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_application.data.id }}"
    And the response "data.attributes.retention_days" is equal to 90

  @skip-python @skip-ruby @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: List archive configurations returns "Bad Request" response
    Given new "ListRUMArchiveConfigs" request
    And request contains "page[size]" parameter with value 101
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
