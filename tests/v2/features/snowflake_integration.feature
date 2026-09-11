@endpoint(snowflake-integration) @endpoint(snowflake-integration-v2)
Feature: Snowflake Integration
  Manage your Datadog Snowflake integration accounts and account resources
  directly through the Datadog API. See the [Snowflake integration
  page](https://docs.datadoghq.com/integrations/snowflake_web/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SnowflakeIntegration" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Snowflake integration account returns "Bad Request" response
    Given operation "CreateSnowflakeIntegrationAccount" enabled
    And new "CreateSnowflakeIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Snowflake integration account returns "Created" response
    Given operation "CreateSnowflakeIntegrationAccount" enabled
    And new "CreateSnowflakeIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Snowflake integration account returns "Not Found" response
    Given operation "CreateSnowflakeIntegrationAccount" enabled
    And new "CreateSnowflakeIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Snowflake integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateSnowflakeIntegrationAccount" enabled
    And new "CreateSnowflakeIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Snowflake integration account returns "Bad Request" response
    Given operation "DeleteSnowflakeIntegrationAccount" enabled
    And new "DeleteSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Snowflake integration account returns "Not Found" response
    Given operation "DeleteSnowflakeIntegrationAccount" enabled
    And new "DeleteSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Snowflake integration account returns "OK" response
    Given operation "DeleteSnowflakeIntegrationAccount" enabled
    And new "DeleteSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Snowflake integration account returns "Bad Request" response
    Given operation "GetSnowflakeIntegrationAccount" enabled
    And new "GetSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Snowflake integration account returns "Not Found" response
    Given operation "GetSnowflakeIntegrationAccount" enabled
    And new "GetSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Snowflake integration account returns "OK" response
    Given operation "GetSnowflakeIntegrationAccount" enabled
    And new "GetSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Snowflake integration accounts returns "Bad Request" response
    Given operation "ListSnowflakeIntegrationAccounts" enabled
    And new "ListSnowflakeIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Snowflake integration accounts returns "Not Found" response
    Given operation "ListSnowflakeIntegrationAccounts" enabled
    And new "ListSnowflakeIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Snowflake integration accounts returns "OK" response
    Given operation "ListSnowflakeIntegrationAccounts" enabled
    And new "ListSnowflakeIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Snowflake integration account returns "Bad Request" response
    Given operation "UpdateSnowflakeIntegrationAccount" enabled
    And new "UpdateSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Snowflake integration account returns "Not Found" response
    Given operation "UpdateSnowflakeIntegrationAccount" enabled
    And new "UpdateSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Snowflake integration account returns "OK" response
    Given operation "UpdateSnowflakeIntegrationAccount" enabled
    And new "UpdateSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Snowflake integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateSnowflakeIntegrationAccount" enabled
    And new "UpdateSnowflakeIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "snowflake-private-key", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "private_key_name": "my-rsa-key", "private_key_passphrase": "your-private-key-passphrase"}, "dataflows": {"snowflake-account-usage-metrics": {"enabled": true, "settings": {"account_usage_metrics_aggregate_last_24h": false}}, "snowflake-cloud-cost-metrics": {"enabled": true, "settings": {"query_tags": "env,team,cost_center"}}, "snowflake-data-observability-quality-monitoring": {"enabled": true, "settings": {"do_table_crawler_cron": "0 */6 * * *", "sync_snowflake_system_database": true}}, "snowflake-event-table-logs": {"enabled": true, "settings": {"event_table_events_enabled": true, "event_table_logs_enabled": true, "event_table_logs_interval_min": 15, "event_table_span_events_enabled": false, "event_table_spans_enabled": false}}, "snowflake-organization-usage-metrics": {"enabled": true, "settings": {"organization_usage_metrics_aggregate_last_24h": false}}, "snowflake-query-history-logs": {"enabled": true, "settings": {"join_query_history_with_access_history_enabled": true, "query_history_logs_interval_min": 15}}, "snowflake-security-logs": {"enabled": true, "settings": {"security_logs_interval_min": 60}}, "snowflake-task-history-logs": {"enabled": true, "settings": {"task_history_logs_interval_min": 30}}}, "name": "prod-snowflake", "settings": {"snowflake_account_identifier": "myorg-myaccount", "username": "datadog_user"}}, "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
