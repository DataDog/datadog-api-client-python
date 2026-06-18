@endpoint(rum-remote-config) @endpoint(rum-remote-config-v2)
Feature: RUM Remote Config
  Manage [RUM SDK
  configurations](https://docs.datadoghq.com/real_user_monitoring/)
  delivered to RUM applications via Remote Configuration.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRemoteConfig" API

  @team:DataDog/rum-backend
  Scenario: Get a RUM SDK configuration returns "Forbidden" response
    Given operation "GetRumSdkConfig" enabled
    And new "GetRumSdkConfig" request
    And request contains "config_id" parameter with value "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    When the request is sent
    Then the response status is 403 Forbidden

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM SDK configuration returns "Not Found" response
    Given operation "GetRumSdkConfig" enabled
    And new "GetRumSdkConfig" request
    And request contains "config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM SDK configuration returns "OK" response
    Given operation "GetRumSdkConfig" enabled
    And new "GetRumSdkConfig" request
    And request contains "config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM SDK configuration returns "Bad Request" response
    Given operation "UpdateRumSdkConfig" enabled
    And new "UpdateRumSdkConfig" request
    And request contains "config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rum": {"allowed_tracing_urls": [{"match": {"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}, "propagator_types": ["datadog", "tracecontext"]}], "allowed_tracking_origins": [{"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}], "context": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "default_privacy_level": "mask", "enable_privacy_for_action_name": true, "env": "production", "service": "my-service", "session_replay_sample_rate": 20, "session_sample_rate": 75, "trace_sample_rate": 100, "track_session_across_subdomains": false, "user": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "version": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "rum_sdk_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Update a RUM SDK configuration returns "Forbidden" response
    Given operation "UpdateRumSdkConfig" enabled
    And new "UpdateRumSdkConfig" request
    And request contains "config_id" parameter with value "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    And body with value {"data": {"id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "type": "rum_sdk_config", "attributes": {"rum": {"session_sample_rate": 75, "session_replay_sample_rate": 20, "default_privacy_level": "mask", "enable_privacy_for_action_name": true}}}}
    When the request is sent
    Then the response status is 403 Forbidden

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM SDK configuration returns "Not Found" response
    Given operation "UpdateRumSdkConfig" enabled
    And new "UpdateRumSdkConfig" request
    And request contains "config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rum": {"allowed_tracing_urls": [{"match": {"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}, "propagator_types": ["datadog", "tracecontext"]}], "allowed_tracking_origins": [{"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}], "context": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "default_privacy_level": "mask", "enable_privacy_for_action_name": true, "env": "production", "service": "my-service", "session_replay_sample_rate": 20, "session_sample_rate": 75, "trace_sample_rate": 100, "track_session_across_subdomains": false, "user": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "version": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "rum_sdk_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM SDK configuration returns "OK" response
    Given operation "UpdateRumSdkConfig" enabled
    And new "UpdateRumSdkConfig" request
    And request contains "config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"rum": {"allowed_tracing_urls": [{"match": {"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}, "propagator_types": ["datadog", "tracecontext"]}], "allowed_tracking_origins": [{"rc_serialized_type": "string", "value": "https://app.datadoghq.com"}], "context": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "default_privacy_level": "mask", "enable_privacy_for_action_name": true, "env": "production", "service": "my-service", "session_replay_sample_rate": 20, "session_sample_rate": 75, "trace_sample_rate": 100, "track_session_across_subdomains": false, "user": [{"key": "id", "value": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}], "version": {"attribute": "data-version", "extractor": {"rc_serialized_type": "regex", "value": "^https://app-.*.datadoghq.com"}, "key": "app.version", "name": "app_version", "path": "application.version", "rc_serialized_type": "dynamic", "selector": "#app-version", "strategy": "js"}}}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "rum_sdk_config"}}
    When the request is sent
    Then the response status is 200 OK
