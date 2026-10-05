@endpoint(experiments) @endpoint(experiments-v2)
Feature: Experiments
  Create and manage experiments, metrics, subject types, SQL models, and
  protocols.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Experiments" API

  @generated @skip @team:ddoghq/experimentation
  Scenario: Archive exposure SQL model returns "Malformed exposure SQL model ID (not a valid UUID)." response
    Given new "ArchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed exposure SQL model ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Archive exposure SQL model returns "No exposure SQL model with this ID exists for the organization." response
    Given new "ArchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No exposure SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Archive exposure SQL model returns "The exposure SQL model was archived. Archiving an already-archived model succeeds and leaves the original archive time in place." response
    Given new "ArchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The exposure SQL model was archived. Archiving an already-archived model succeeds and leaves the original archive time in place.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Cancel experiment returns "Malformed experiment ID, malformed request body, or a missing/blank reason." response
    Given new "CancelExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"reason": "Experiment configuration was incorrect"}, "type": "cancel-experiment-request"}}
    When the request is sent
    Then the response status is 400 Malformed experiment ID, malformed request body, or a missing/blank reason.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Cancel experiment returns "No experiment with this ID exists for the organization." response
    Given new "CancelExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"reason": "Experiment configuration was incorrect"}, "type": "cancel-experiment-request"}}
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Cancel experiment returns "The experiment cannot be canceled in its current state." response
    Given new "CancelExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"reason": "Experiment configuration was incorrect"}, "type": "cancel-experiment-request"}}
    When the request is sent
    Then the response status is 409 The experiment cannot be canceled in its current state.

  @team:ddoghq/experimentation
  Scenario: Cancel experiment returns "The experiment was canceled and unlinked from its feature flag allocations." response
    Given new "CancelExperiment" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And body with value {"data": {"type": "cancel-experiment-request", "attributes": {"reason": "Cancel the test experiment"}}}
    When the request is sent
    Then the response status is 204 The experiment was canceled and unlinked from its feature flag allocations.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Conclude experiment returns "Malformed experiment ID, malformed request body, or a missing decision_variant_key." response
    Given new "ConcludeExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"decision_variant_key": "treatment"}, "type": "conclude-experiment-request"}}
    When the request is sent
    Then the response status is 400 Malformed experiment ID, malformed request body, or a missing decision_variant_key.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Conclude experiment returns "No experiment with this ID exists for the organization." response
    Given new "ConcludeExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"decision_variant_key": "treatment"}, "type": "conclude-experiment-request"}}
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Conclude experiment returns "The experiment is not running or ready for a decision, its linked feature flag environment requires an approval for the rollout this would perform, or that flag has a pending suggestion for its allocations." response
    Given new "ConcludeExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"decision_variant_key": "treatment"}, "type": "conclude-experiment-request"}}
    When the request is sent
    Then the response status is 409 The experiment is not running or ready for a decision, its linked feature flag environment requires an approval for the rollout this would perform, or that flag has a pending suggestion for its allocations.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Conclude experiment returns "The experiment was concluded and the winning variant was rolled out to its linked feature flag allocation." response
    Given new "ConcludeExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"decision_variant_key": "treatment"}, "type": "conclude-experiment-request"}}
    When the request is sent
    Then the response status is 204 The experiment was concluded and the winning variant was rolled out to its linked feature flag allocation.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group from collection returns "Bad Request" response
    Given new "CreateExperimentMetricGroupFromCollection" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group from collection returns "Conflict" response
    Given new "CreateExperimentMetricGroupFromCollection" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/experimentation
  Scenario: Create experiment metric group from collection returns "Created" response
    Given new "CreateExperimentMetricGroupFromCollection" request
    And there is a valid "experiment_metric" in the system
    And there is a valid "experiment_metric_collection_with_metric" in the system
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And request contains "metric_collection_id" parameter from "experiment_metric_collection_with_metric.data.id"
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.metrics" has length 1

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group from collection returns "Not Found" response
    Given new "CreateExperimentMetricGroupFromCollection" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group returns "Bad Request" response
    Given new "CreateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Diagnostics"}, "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group returns "Conflict" response
    Given new "CreateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Diagnostics"}, "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/experimentation
  Scenario: Create experiment metric group returns "Created" response
    Given new "CreateExperimentMetricGroup" request
    And there is a valid "experiment_metric" in the system
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And body with value {"data": {"type": "experiment-metric-groups", "attributes": {"name": "ex-{{ unique_hash }}", "metrics": [{"metric_id": "{{ experiment_metric.data.id }}"}]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.metrics" has length 1

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group returns "Not Found" response
    Given new "CreateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Diagnostics"}, "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment metric group returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "CreateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Diagnostics"}, "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @team:ddoghq/experimentation
  Scenario: Create experiment returns "Created" response
    Given new "CreateExperiment" request
    And body with value {"data": {"type": "experiments", "attributes": {"name": "ex-{{ unique_hash }}"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.experiment_type" is equal to "STANDARD"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment returns "Invalid request body: missing required field, malformed variants or decision_metrics, or an unresolvable analysis configuration." response
    Given new "CreateExperiment" request
    And body with value {"data": {"attributes": {"assignments_end_date": "2026-08-15T00:00:00Z", "assignments_start_date": "2026-08-01T00:00:00Z", "datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440004", "targeting_rules": []}, "decision_metrics": [{"is_primary": true, "metric_id": "b1a2c3d4-0000-0000-0000-000000000000"}], "events_end_date": "2026-08-22T00:00:00Z", "events_start_date": "2026-08-01T00:00:00Z", "name": "Checkout button test", "structured_metadata": [{"enum_values": ["beta"], "field_key": "launch_stage"}, {"field_key": "notes", "freetext_value": "Checkout redesign"}], "subject_type_id": "c2b3d4e5-0000-0000-0000-000000000000", "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440010", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440011", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 400 Invalid request body: missing required field, malformed variants or decision_metrics, or an unresolvable analysis configuration.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "CreateExperiment" request
    And body with value {"data": {"attributes": {"assignments_end_date": "2026-08-15T00:00:00Z", "assignments_start_date": "2026-08-01T00:00:00Z", "datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440004", "targeting_rules": []}, "decision_metrics": [{"is_primary": true, "metric_id": "b1a2c3d4-0000-0000-0000-000000000000"}], "events_end_date": "2026-08-22T00:00:00Z", "events_start_date": "2026-08-01T00:00:00Z", "name": "Checkout button test", "structured_metadata": [{"enum_values": ["beta"], "field_key": "launch_stage"}, {"field_key": "notes", "freetext_value": "Checkout redesign"}], "subject_type_id": "c2b3d4e5-0000-0000-0000-000000000000", "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440010", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440011", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment returns "The requested configuration is incompatible with the experiment (code: unsupported_configuration)." response
    Given new "CreateExperiment" request
    And body with value {"data": {"attributes": {"assignments_end_date": "2026-08-15T00:00:00Z", "assignments_start_date": "2026-08-01T00:00:00Z", "datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440004", "targeting_rules": []}, "decision_metrics": [{"is_primary": true, "metric_id": "b1a2c3d4-0000-0000-0000-000000000000"}], "events_end_date": "2026-08-22T00:00:00Z", "events_start_date": "2026-08-01T00:00:00Z", "name": "Checkout button test", "structured_metadata": [{"enum_values": ["beta"], "field_key": "launch_stage"}, {"field_key": "notes", "freetext_value": "Checkout redesign"}], "subject_type_id": "c2b3d4e5-0000-0000-0000-000000000000", "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440010", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440011", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 409 The requested configuration is incompatible with the experiment (code: unsupported_configuration).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment returns "The supplied protocol is a draft or archived protocol and cannot be applied to a new experiment." response
    Given new "CreateExperiment" request
    And body with value {"data": {"attributes": {"assignments_end_date": "2026-08-15T00:00:00Z", "assignments_start_date": "2026-08-01T00:00:00Z", "datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440004", "targeting_rules": []}, "decision_metrics": [{"is_primary": true, "metric_id": "b1a2c3d4-0000-0000-0000-000000000000"}], "events_end_date": "2026-08-22T00:00:00Z", "events_start_date": "2026-08-01T00:00:00Z", "name": "Checkout button test", "structured_metadata": [{"enum_values": ["beta"], "field_key": "launch_stage"}, {"field_key": "notes", "freetext_value": "Checkout redesign"}], "subject_type_id": "c2b3d4e5-0000-0000-0000-000000000000", "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440010", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440011", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 422 The supplied protocol is a draft or archived protocol and cannot be applied to a new experiment.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create experiment returns "The supplied protocol_id does not identify a protocol in this organization." response
    Given new "CreateExperiment" request
    And body with value {"data": {"attributes": {"assignments_end_date": "2026-08-15T00:00:00Z", "assignments_start_date": "2026-08-01T00:00:00Z", "datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440004", "targeting_rules": []}, "decision_metrics": [{"is_primary": true, "metric_id": "b1a2c3d4-0000-0000-0000-000000000000"}], "events_end_date": "2026-08-22T00:00:00Z", "events_start_date": "2026-08-01T00:00:00Z", "name": "Checkout button test", "structured_metadata": [{"enum_values": ["beta"], "field_key": "launch_stage"}, {"field_key": "notes", "freetext_value": "Checkout redesign"}], "subject_type_id": "c2b3d4e5-0000-0000-0000-000000000000", "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440010", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440011", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 404 The supplied protocol_id does not identify a protocol in this organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create exposure SQL model returns "Created" response
    Given new "CreateExposureSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create exposure SQL model returns "Malformed body, validation failure, or the SQL was rejected by the warehouse validator." response
    Given new "CreateExposureSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 400 Malformed body, validation failure, or the SQL was rejected by the warehouse validator.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create exposure SQL model returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "CreateExposureSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create exposure SQL model returns "The write collided with an existing record for the organization." response
    Given new "CreateExposureSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 409 The write collided with an existing record for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric SQL model returns "Another metric SQL model in this organization already uses one of these values." response
    Given new "CreateMetricSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 409 Another metric SQL model in this organization already uses one of these values.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric SQL model returns "Created" response
    Given new "CreateMetricSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric SQL model returns "Malformed body, validation failure, the SQL was rejected by the warehouse validator, or the organization has no warehouse connection." response
    Given new "CreateMetricSQLModel" request
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 400 Malformed body, validation failure, the SQL was rejected by the warehouse validator, or the organization has no warehouse connection.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric collection returns "Bad Request" response
    Given new "CreateMetricCollection" request
    And body with value {"data": {"attributes": {"name": "Activation"}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric collection returns "Conflict" response
    Given new "CreateMetricCollection" request
    And body with value {"data": {"attributes": {"name": "Activation"}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/experimentation
  Scenario: Create metric collection returns "Created" response
    Given new "CreateMetricCollection" request
    And body with value {"data": {"type": "metric-collections", "attributes": {"name": "ex-{{ unique_hash }}"}}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric collection returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "CreateMetricCollection" request
    And body with value {"data": {"attributes": {"name": "Activation"}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric returns "Another metric in this organization already uses one of these values." response
    Given new "CreateMetric" request
    And body with value {"data": {"attributes": {"data_source_type": "CUSTOMER_WAREHOUSE", "description": null, "desired_change": "METRIC_INCREASES", "format_as_percent": true, "guardrail_cutoff_threshold": null, "name": "Checkout conversion", "numerator_aggregation": {"operation": "sum", "property_filters": [[{"operation": "IS", "property_id": "550e8400-e29b-41d4-a716-446655440023", "values": ["US"]}]], "timeframe_start_value": 0, "warehouse_metric_measure": {"id": "550e8400-e29b-41d4-a716-446655440021"}}}, "type": "metrics"}}
    When the request is sent
    Then the response status is 409 Another metric in this organization already uses one of these values.

  @team:ddoghq/experimentation
  Scenario: Create metric returns "Created" response
    Given new "CreateMetric" request
    And body with value {"data": {"type": "metrics", "attributes": {"name": "ex-{{ unique_hash }}", "data_source_type": "DATADOG", "desired_change": "METRIC_INCREASES", "numerator_aggregation": {"operation": "sum", "datadog_metric_measure": {"name": "ex-{{ unique_hash }} view duration", "source_type": "PRODUCT_ANALYTICS", "source_subtype": "RUM_VIEWS", "column_type": "double", "column_name": "@view.time_spent"}}}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.metric_type" is equal to "SIMPLE"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric returns "Malformed body, validation failure, or an aggregation that does not match metric_type." response
    Given new "CreateMetric" request
    And body with value {"data": {"attributes": {"data_source_type": "CUSTOMER_WAREHOUSE", "description": null, "desired_change": "METRIC_INCREASES", "format_as_percent": true, "guardrail_cutoff_threshold": null, "name": "Checkout conversion", "numerator_aggregation": {"operation": "sum", "property_filters": [[{"operation": "IS", "property_id": "550e8400-e29b-41d4-a716-446655440023", "values": ["US"]}]], "timeframe_start_value": 0, "warehouse_metric_measure": {"id": "550e8400-e29b-41d4-a716-446655440021"}}}, "type": "metrics"}}
    When the request is sent
    Then the response status is 400 Malformed body, validation failure, or an aggregation that does not match metric_type.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create metric returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "CreateMetric" request
    And body with value {"data": {"attributes": {"data_source_type": "CUSTOMER_WAREHOUSE", "description": null, "desired_change": "METRIC_INCREASES", "format_as_percent": true, "guardrail_cutoff_threshold": null, "name": "Checkout conversion", "numerator_aggregation": {"operation": "sum", "property_filters": [[{"operation": "IS", "property_id": "550e8400-e29b-41d4-a716-446655440023", "values": ["US"]}]], "timeframe_start_value": 0, "warehouse_metric_measure": {"id": "550e8400-e29b-41d4-a716-446655440021"}}}, "type": "metrics"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @team:ddoghq/experimentation
  Scenario: Create subject type returns "Created" response
    Given new "CreateSubjectType" request
    And body with value {"data": {"type": "subject-types", "attributes": {"name": "ex-{{ unique_hash }}", "product_analytics_attribute": "@account.id", "warehouse_column_names": ["account_id"]}}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/experimentation
  Scenario: Create subject type returns "Malformed body, or validation failure on name, product_analytics_attribute, or warehouse_column_names." response
    Given new "CreateSubjectType" request
    And body with value {"data": {"attributes": {"name": "User", "product_analytics_attribute": "@usr.id", "warehouse_column_names": ["user_id", "customer_id"]}, "type": "subject-types"}}
    When the request is sent
    Then the response status is 400 Malformed body, or validation failure on name, product_analytics_attribute, or warehouse_column_names.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment metric group returns "Bad Request" response
    Given new "DeleteExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment metric group returns "Conflict" response
    Given new "DeleteExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/experimentation
  Scenario: Delete experiment metric group returns "No Content" response
    Given new "DeleteExperimentMetricGroup" request
    And there is a valid "experiment_metric" in the system
    And there is a valid "experiment" in the system
    And there is a valid "experiment_metric_group" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And request contains "metric_group_id" parameter from "experiment_metric_group.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment metric group returns "Not Found" response
    Given new "DeleteExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment returns "Malformed experiment ID (not a valid UUID)." response
    Given new "DeleteExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID).

  @team:ddoghq/experimentation
  Scenario: Delete experiment returns "No Content" response
    Given new "DeleteExperiment" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment returns "No experiment with this ID exists for the organization." response
    Given new "DeleteExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment returns "The experiment has a published allocation on an archived flag, must be retained for selective holdout analysis, or its linked allocations changed during authorization. Nothing was deleted." response
    Given new "DeleteExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 The experiment has a published allocation on an archived flag, must be retained for selective holdout analysis, or its linked allocations changed during authorization. Nothing was deleted.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete experiment returns "The experiment was deleted." response
    Given new "DeleteExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The experiment was deleted.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete metric collection returns "Bad Request" response
    Given new "DeleteMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/experimentation
  Scenario: Delete metric collection returns "No Content" response
    Given new "DeleteMetricCollection" request
    And there is a valid "experiment_metric_collection" in the system
    And request contains "metric_collection_id" parameter from "experiment_metric_collection.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete metric collection returns "Not Found" response
    Given new "DeleteMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete metric returns "Malformed metric ID (not a valid UUID)." response
    Given new "DeleteMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed metric ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete metric returns "No metric with this ID exists for the organization." response
    Given new "DeleteMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No metric with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete metric returns "The metric is imported, certified, managed by metric sync, or still referenced by one or more experiments and cannot be deleted." response
    Given new "DeleteMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 The metric is imported, certified, managed by metric sync, or still referenced by one or more experiments and cannot be deleted.

  @team:ddoghq/experimentation
  Scenario: Delete metric returns "The metric was deleted." response
    Given new "DeleteMetric" request
    And there is a valid "experiment_metric" in the system
    And request contains "metric_id" parameter from "experiment_metric.data.id"
    When the request is sent
    Then the response status is 204 The metric was deleted.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete subject type returns "Either this subject type is the organization's default, or experiments, exposure SQL models, metric SQL models or protocols still reference it. When something references it, meta.blockers names them (capped per kind, with truncated set when more exist)." response
    Given new "DeleteSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Either this subject type is the organization's default, or experiments, exposure SQL models, metric SQL models or protocols still reference it. When something references it, meta.blockers names them (capped per kind, with truncated set when more exist).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete subject type returns "Malformed subject type ID (not a valid UUID)." response
    Given new "DeleteSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed subject type ID (not a valid UUID).

  @team:ddoghq/experimentation
  Scenario: Delete subject type returns "No Content" response
    Given new "DeleteSubjectType" request
    And there is a valid "experiment_subject_type" in the system
    And request contains "subject_type_id" parameter from "experiment_subject_type.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete subject type returns "No subject type with this ID exists for the organization." response
    Given new "DeleteSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No subject type with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Delete subject type returns "The subject type was deleted." response
    Given new "DeleteSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The subject type was deleted.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment analysis plan returns "Malformed experiment ID." response
    Given new "GetExperimentAnalysisPlan" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment analysis plan returns "Not Found" response
    Given new "GetExperimentAnalysisPlan" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/experimentation
  Scenario: Get experiment analysis plan returns "OK" response
    Given new "GetExperimentAnalysisPlan" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "experiment.data.id"
    And the response "data.type" is equal to "analysis-plans"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment diagnostics returns "Malformed experiment ID (not a valid UUID)." response
    Given new "GetExperimentDiagnostics" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment diagnostics returns "No experiment with this ID exists for the organization. Lifecycle statuses in a successful response explain whether analysis has started, is running, or completed without diagnostics." response
    Given new "GetExperimentDiagnostics" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization. Lifecycle statuses in a successful response explain whether analysis has started, is running, or completed without diagnostics.

  @team:ddoghq/experimentation
  Scenario: Get experiment diagnostics returns "OK" response
    Given new "GetExperimentDiagnostics" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.state" is equal to "NOT_STARTED"
    And the response "data.attributes.diagnostics" has length 0

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment protocol returns "Bad Request" response
    Given new "GetExperimentProtocol" request
    And request contains "protocol_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment protocol returns "Not Found" response
    Given new "GetExperimentProtocol" request
    And request contains "protocol_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment protocol returns "OK" response
    Given new "GetExperimentProtocol" request
    And request contains "protocol_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment results returns "Malformed experiment ID (not a valid UUID), or the experiment is not configured for analysis." response
    Given new "GetExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID), or the experiment is not configured for analysis.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment results returns "No experiment with this ID exists, or results are not available for it yet." response
    Given new "GetExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists, or results are not available for it yet.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment results returns "OK" response
    Given new "GetExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment results returns "The experiment's metrics are incompatible with analysis." response
    Given new "GetExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 The experiment's metrics are incompatible with analysis.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment returns "Malformed experiment ID (not a valid UUID)." response
    Given new "GetExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment returns "No experiment with this ID exists for the organization." response
    Given new "GetExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Get experiment returns "OK" response
    Given new "GetExperiment" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.experiment_type" is equal to "STANDARD"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment returns "The stored assignment configuration cannot be represented losslessly by this API (unsupported_configuration)." response
    Given new "GetExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 The stored assignment configuration cannot be represented losslessly by this API (unsupported_configuration).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment traffic summary returns "Malformed experiment ID (not a valid UUID), or the experiment is not configured for analysis." response
    Given new "GetExperimentTrafficSummary" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID), or the experiment is not configured for analysis.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment traffic summary returns "No experiment with this ID exists for the organization." response
    Given new "GetExperimentTrafficSummary" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Get experiment traffic summary returns "OK" response
    Given new "GetExperimentTrafficSummary" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.total_subjects" is equal to 0
    And the response "data.attributes.variants" has length 0

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get experiment traffic summary returns "The experiment's metrics are incompatible with analysis." response
    Given new "GetExperimentTrafficSummary" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 The experiment's metrics are incompatible with analysis.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get exposure SQL model returns "Malformed exposure SQL model ID (not a valid UUID), or unknown include value." response
    Given new "GetExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed exposure SQL model ID (not a valid UUID), or unknown include value.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get exposure SQL model returns "No exposure SQL model with this ID exists for the organization." response
    Given new "GetExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No exposure SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get exposure SQL model returns "OK" response
    Given new "GetExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric SQL model returns "Malformed metric SQL model ID (not a valid UUID), or unknown include value." response
    Given new "GetMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed metric SQL model ID (not a valid UUID), or unknown include value.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric SQL model returns "No metric SQL model with this ID exists for the organization." response
    Given new "GetMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No metric SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric SQL model returns "OK" response
    Given new "GetMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric collection returns "Bad Request" response
    Given new "GetMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric collection returns "Not Found" response
    Given new "GetMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/experimentation
  Scenario: Get metric collection returns "OK" response
    Given new "GetMetricCollection" request
    And there is a valid "experiment_metric_collection" in the system
    And request contains "metric_collection_id" parameter from "experiment_metric_collection.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric returns "Malformed metric ID (not a valid UUID)." response
    Given new "GetMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed metric ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get metric returns "No metric with this ID exists for the organization." response
    Given new "GetMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No metric with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Get metric returns "OK" response
    Given new "GetMetric" request
    And there is a valid "experiment_metric" in the system
    And request contains "metric_id" parameter from "experiment_metric.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "experiment_metric.data.id"
    And the response "data.attributes.metric_type" is equal to "SIMPLE"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get subject type returns "Malformed subject type ID (not a valid UUID), or an unsupported include value." response
    Given new "GetSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed subject type ID (not a valid UUID), or an unsupported include value.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Get subject type returns "No subject type with this ID exists for the organization." response
    Given new "GetSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No subject type with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Get subject type returns "OK" response
    Given new "GetSubjectType" request
    And there is a valid "experiment_subject_type" in the system
    And request contains "subject_type_id" parameter from "experiment_subject_type.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List experiment metric groups returns "Malformed experiment ID." response
    Given new "ListExperimentMetricGroups" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID.

  @generated @skip @team:ddoghq/experimentation
  Scenario: List experiment metric groups returns "No experiment with this ID exists for the organization." response
    Given new "ListExperimentMetricGroups" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: List experiment metric groups returns "OK" response
    Given new "ListExperimentMetricGroups" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @generated @skip @team:ddoghq/experimentation
  Scenario: List experiment protocols returns "Bad Request" response
    Given new "ListExperimentProtocols" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/experimentation
  Scenario: List experiment protocols returns "OK" response
    Given new "ListExperimentProtocols" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List experiments returns "Invalid query parameter: bad page[offset]/page[limit], unknown sort field, invalid status, malformed protocol_id UUID, invalid result timestamp range, or a timestamp filter that is not RFC3339." response
    Given new "ListExperiments" request
    When the request is sent
    Then the response status is 400 Invalid query parameter: bad page[offset]/page[limit], unknown sort field, invalid status, malformed protocol_id UUID, invalid result timestamp range, or a timestamp filter that is not RFC3339.

  @team:ddoghq/experimentation
  Scenario: List experiments returns "OK" response
    Given new "ListExperiments" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List exposure SQL models returns "Invalid query parameter: bad page[offset]/page[limit], search longer than 1024 bytes, unknown sort field, non-boolean include_archived, or unknown include value." response
    Given new "ListExposureSQLModels" request
    When the request is sent
    Then the response status is 400 Invalid query parameter: bad page[offset]/page[limit], search longer than 1024 bytes, unknown sort field, non-boolean include_archived, or unknown include value.

  @team:ddoghq/experimentation
  Scenario: List exposure SQL models returns "OK" response
    Given new "ListExposureSQLModels" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List metric SQL models returns "Invalid query parameter: bad page[offset]/page[limit], unknown sort field, or unknown include value." response
    Given new "ListMetricSQLModels" request
    When the request is sent
    Then the response status is 400 Invalid query parameter: bad page[offset]/page[limit], unknown sort field, or unknown include value.

  @team:ddoghq/experimentation
  Scenario: List metric SQL models returns "OK" response
    Given new "ListMetricSQLModels" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List metric collections returns "Bad Request" response
    Given new "ListMetricCollections" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/experimentation
  Scenario: List metric collections returns "OK" response
    Given new "ListMetricCollections" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List metrics returns "Invalid query parameter: bad page[offset]/page[limit], or unknown sort field." response
    Given new "ListMetrics" request
    When the request is sent
    Then the response status is 400 Invalid query parameter: bad page[offset]/page[limit], or unknown sort field.

  @team:ddoghq/experimentation
  Scenario: List metrics returns "OK" response
    Given new "ListMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: List subject types returns "Invalid query parameter: bad page[offset]/page[limit], or unknown sort field." response
    Given new "ListSubjectTypes" request
    When the request is sent
    Then the response status is 400 Invalid query parameter: bad page[offset]/page[limit], or unknown sort field.

  @team:ddoghq/experimentation
  Scenario: List subject types returns "OK" response
    Given new "ListSubjectTypes" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch experiment returns "Invalid request: malformed field, a read-only attribute was sent, a referenced ID doesn't exist, an allocation change is not supported after start, or the resulting analysis configuration is invalid. May return multiple errors." response
    Given new "PatchExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440014", "reset_on_feature_flag_change": true, "targeting_rules": []}, "structured_metadata": [{"enum_values": ["general_availability"], "field_key": "launch_stage"}], "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440020", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440021", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 400 Invalid request: malformed field, a read-only attribute was sent, a referenced ID doesn't exist, an allocation change is not supported after start, or the resulting analysis configuration is invalid. May return multiple errors.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch experiment returns "No experiment with this ID exists for the organization." response
    Given new "PatchExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440014", "reset_on_feature_flag_change": true, "targeting_rules": []}, "structured_metadata": [{"enum_values": ["general_availability"], "field_key": "launch_stage"}], "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440020", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440021", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Patch experiment returns "OK" response
    Given new "PatchExperiment" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And body with value {"data": {"type": "experiments", "attributes": {"name": "ex-{{ unique_hash }} updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.experiment_type" is equal to "STANDARD"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch experiment returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "PatchExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440014", "reset_on_feature_flag_change": true, "targeting_rules": []}, "structured_metadata": [{"enum_values": ["general_availability"], "field_key": "launch_stage"}], "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440020", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440021", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch experiment returns "The requested configuration is incompatible with the experiment, or a feature flag change requires explicit reset consent and a complete target configuration (codes: unsupported_configuration, feature_flag_change_requires_reset, or feature_flag_change_requires_complete_configuration)." response
    Given new "PatchExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"datadog_flag_configuration": {"entry_point": null, "environment_id": "550e8400-e29b-41d4-a716-446655440005", "feature_flag_id": "550e8400-e29b-41d4-a716-446655440014", "reset_on_feature_flag_change": true, "targeting_rules": []}, "structured_metadata": [{"enum_values": ["general_availability"], "field_key": "launch_stage"}], "traffic_exposure": {"fraction": 1, "mode": "STATIC"}, "variants": [{"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440020", "is_active": true, "is_control": true, "key": "control", "weight": 50}, {"feature_flag_variant_id": "550e8400-e29b-41d4-a716-446655440021", "is_active": true, "is_control": false, "key": "treatment", "weight": 50}]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 409 The requested configuration is incompatible with the experiment, or a feature flag change requires explicit reset consent and a complete target configuration (codes: unsupported_configuration, feature_flag_change_requires_reset, or feature_flag_change_requires_complete_configuration).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch subject type returns "Malformed subject type ID, malformed body, or no updatable field supplied." response
    Given new "PatchSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Updated User", "product_analytics_attribute": "@usr.id", "warehouse_column_names": ["user_id"]}, "type": "subject-types"}}
    When the request is sent
    Then the response status is 400 Malformed subject type ID, malformed body, or no updatable field supplied.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Patch subject type returns "No subject type with this ID exists for the organization." response
    Given new "PatchSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Updated User", "product_analytics_attribute": "@usr.id", "warehouse_column_names": ["user_id"]}, "type": "subject-types"}}
    When the request is sent
    Then the response status is 404 No subject type with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Patch subject type returns "OK" response
    Given new "PatchSubjectType" request
    And there is a valid "experiment_subject_type" in the system
    And request contains "subject_type_id" parameter from "experiment_subject_type.data.id"
    And body with value {"data": {"type": "subject-types", "attributes": {"name": "ex-{{ unique_hash }} updated"}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results for org returns "Accepted" response
    Given new "RefreshExperimentResultsForOrg" request
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results for org returns "The full_refresh query parameter is not a valid boolean." response
    Given new "RefreshExperimentResultsForOrg" request
    When the request is sent
    Then the response status is 400 The full_refresh query parameter is not a valid boolean.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results returns "A refresh is already queued or running for this experiment." response
    Given new "RefreshExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 A refresh is already queued or running for this experiment.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results returns "Accepted" response
    Given new "RefreshExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results returns "Malformed experiment ID (not a valid UUID), or full_refresh is not a valid boolean." response
    Given new "RefreshExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed experiment ID (not a valid UUID), or full_refresh is not a valid boolean.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Refresh experiment results returns "No experiment with this ID exists for the organization." response
    Given new "RefreshExperimentResults" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Set default subject type returns "Malformed subject type ID (not a valid UUID)." response
    Given new "SetDefaultSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed subject type ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Set default subject type returns "No subject type with this ID exists for the organization." response
    Given new "SetDefaultSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No subject type with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Set default subject type returns "The subject type is now the organization's default." response
    Given new "SetDefaultSubjectType" request
    And request contains "subject_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The subject type is now the organization's default.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Start experiment returns "Malformed experiment ID, a request body carrying attributes this endpoint does not accept, or an experiment managed by a specialized workflow that cannot use this start endpoint." response
    Given new "StartExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "start-experiment-request"}}
    When the request is sent
    Then the response status is 400 Malformed experiment ID, a request body carrying attributes this endpoint does not accept, or an experiment managed by a specialized workflow that cannot use this start endpoint.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Start experiment returns "No experiment with this ID exists for the organization." response
    Given new "StartExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "start-experiment-request"}}
    When the request is sent
    Then the response status is 404 No experiment with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Start experiment returns "The experiment cannot be started from its current state, its stored setup is incomplete (missing subject type, primary metric, variants, assignment source, or run window), its linked feature flag environment requires an approval, or that flag has a pending suggestion for a property this would change (environment status, override variant, rollout, or allocations)." response
    Given new "StartExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "start-experiment-request"}}
    When the request is sent
    Then the response status is 409 The experiment cannot be started from its current state, its stored setup is incomplete (missing subject type, primary metric, variants, assignment source, or run window), its linked feature flag environment requires an approval, or that flag has a pending suggestion for a property this would change (environment status, override variant, rollout, or allocations).

  @team:ddoghq/experimentation
  Scenario: Start experiment returns "The experiment was started." response
    Given new "StartExperiment" request
    And there is a valid "environment" in the system
    And there is a valid "feature_flag" in the system
    And there is a valid "experiment_subject_type" in the system
    And there is a valid "experiment_metric" in the system
    And there is a valid "configured_experiment" in the system
    And there is a valid "experiment_start_analysis_plan" in the system
    And request contains "experiment_id" parameter from "configured_experiment.data.id"
    When the request is sent
    Then the response status is 204 The experiment was started.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Unarchive exposure SQL model returns "Malformed exposure SQL model ID (not a valid UUID)." response
    Given new "UnarchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Malformed exposure SQL model ID (not a valid UUID).

  @generated @skip @team:ddoghq/experimentation
  Scenario: Unarchive exposure SQL model returns "No exposure SQL model with this ID exists for the organization." response
    Given new "UnarchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 No exposure SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Unarchive exposure SQL model returns "The exposure SQL model was unarchived. Unarchiving a model that is not archived succeeds and changes nothing." response
    Given new "UnarchiveExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The exposure SQL model was unarchived. Unarchiving a model that is not archived succeeds and changes nothing.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment analysis plan attributes returns "Bad Request" response
    Given new "UpdateExperimentAnalysisPlanAttributes" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bayesian_prior": {"degrees_of_freedom": null, "standard_deviation": 0.05}, "confidence_interval_method": "Bayesian", "confidence_level": 0.95, "cuped_lookback_period_days": 30, "experiment_auto_end_days": 0, "experiment_min_duration": 0, "experiment_min_sample_size": 0, "is_cuped_enabled": true, "is_multiple_testing_correction_enabled": false, "preferential_bonferroni_primary_metric_weight": 0.5, "target_duration_days": 14}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "analysis-plans"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment analysis plan attributes returns "Not Found" response
    Given new "UpdateExperimentAnalysisPlanAttributes" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bayesian_prior": {"degrees_of_freedom": null, "standard_deviation": 0.05}, "confidence_interval_method": "Bayesian", "confidence_level": 0.95, "cuped_lookback_period_days": 30, "experiment_auto_end_days": 0, "experiment_min_duration": 0, "experiment_min_sample_size": 0, "is_cuped_enabled": true, "is_multiple_testing_correction_enabled": false, "preferential_bonferroni_primary_metric_weight": 0.5, "target_duration_days": 14}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "analysis-plans"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/experimentation
  Scenario: Update experiment analysis plan attributes returns "OK" response
    Given new "UpdateExperimentAnalysisPlanAttributes" request
    And there is a valid "experiment" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And body with value {"data": {"type": "analysis-plans", "id": "{{ experiment.data.id }}", "attributes": {"confidence_level": 0.9}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "experiment.data.id"
    And the response "data.attributes.confidence_level" is equal to 0.9

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment analysis plan attributes returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "UpdateExperimentAnalysisPlanAttributes" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bayesian_prior": {"degrees_of_freedom": null, "standard_deviation": 0.05}, "confidence_interval_method": "Bayesian", "confidence_level": 0.95, "cuped_lookback_period_days": 30, "experiment_auto_end_days": 0, "experiment_min_duration": 0, "experiment_min_sample_size": 0, "is_cuped_enabled": true, "is_multiple_testing_correction_enabled": false, "preferential_bonferroni_primary_metric_weight": 0.5, "target_duration_days": 14}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "analysis-plans"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment analysis plan attributes returns "The requested change conflicts with settings locked by the experiment protocol." response
    Given new "UpdateExperimentAnalysisPlanAttributes" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bayesian_prior": {"degrees_of_freedom": null, "standard_deviation": 0.05}, "confidence_interval_method": "Bayesian", "confidence_level": 0.95, "cuped_lookback_period_days": 30, "experiment_auto_end_days": 0, "experiment_min_duration": 0, "experiment_min_sample_size": 0, "is_cuped_enabled": true, "is_multiple_testing_correction_enabled": false, "preferential_bonferroni_primary_metric_weight": 0.5, "target_duration_days": 14}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "analysis-plans"}}
    When the request is sent
    Then the response status is 409 The requested change conflicts with settings locked by the experiment protocol.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment metric group returns "Bad Request" response
    Given new "UpdateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Reliability"}, "id": "550e8400-e29b-41d4-a716-446655440022", "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment metric group returns "Conflict" response
    Given new "UpdateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Reliability"}, "id": "550e8400-e29b-41d4-a716-446655440022", "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment metric group returns "Not Found" response
    Given new "UpdateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Reliability"}, "id": "550e8400-e29b-41d4-a716-446655440022", "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/experimentation
  Scenario: Update experiment metric group returns "OK" response
    Given new "UpdateExperimentMetricGroup" request
    And there is a valid "experiment_metric" in the system
    And there is a valid "experiment" in the system
    And there is a valid "experiment_metric_group" in the system
    And request contains "experiment_id" parameter from "experiment.data.id"
    And request contains "metric_group_id" parameter from "experiment_metric_group.data.id"
    And body with value {"data": {"type": "experiment-metric-groups", "id": "{{ experiment_metric_group.data.id }}", "attributes": {"name": "ex-{{ unique_hash }} updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "ex-{{ unique_hash }} updated"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update experiment metric group returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "UpdateExperimentMetricGroup" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And request contains "metric_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"metric_id": "550e8400-e29b-41d4-a716-446655440021"}], "name": "Reliability"}, "id": "550e8400-e29b-41d4-a716-446655440022", "type": "experiment-metric-groups"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update exposure SQL model returns "Malformed exposure SQL model ID, malformed body, validation failure, or the SQL was rejected by the warehouse validator." response
    Given new "UpdateExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 400 Malformed exposure SQL model ID, malformed body, validation failure, or the SQL was rejected by the warehouse validator.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update exposure SQL model returns "No exposure SQL model with this ID exists for the organization." response
    Given new "UpdateExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 404 No exposure SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update exposure SQL model returns "OK" response
    Given new "UpdateExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update exposure SQL model returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "UpdateExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update exposure SQL model returns "The write collided with an existing record for the organization." response
    Given new "UpdateExposureSQLModel" request
    And request contains "exposure_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "experiment_column": "experiment_id", "name": "Exposure events", "properties": [{"column_name": "country", "column_type": "STRING", "description": null, "name": "country"}], "sql": "SELECT user_id, experiment_id, variant, exposed_at, country FROM analytics.exposures", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "exposed_at", "variant_column": "variant"}, "type": "exposure-sql-models"}}
    When the request is sent
    Then the response status is 409 The write collided with an existing record for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric SQL model returns "Malformed ID or body, validation failure, or the SQL was rejected by the warehouse validator." response
    Given new "UpdateMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 400 Malformed ID or body, validation failure, or the SQL was rejected by the warehouse validator.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric SQL model returns "No metric SQL model with this ID exists for the organization." response
    Given new "UpdateMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 404 No metric SQL model with this ID exists for the organization.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric SQL model returns "OK" response
    Given new "UpdateMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric SQL model returns "The model is certified or managed by metric sync, or the update would remove a measure or property still used by an active metric." response
    Given new "UpdateMetricSQLModel" request
    And request contains "metric_sql_model_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"date_partition_column": null, "description": null, "measures": [{"column_name": "revenue", "column_type": "FLOAT", "description": null, "name": null}], "name": "Order facts", "properties": [{"column_name": "item_type", "column_type": "STRING", "description": null, "name": "item_type"}], "sql": "SELECT user_id, order_id, item_type, revenue, created_at FROM analytics.orders", "subject_types": [{"column_name": "user_id", "subject_type_id": "550e8400-e29b-41d4-a716-446655440010"}], "timestamp_column": "created_at"}, "type": "metric-sql-models"}}
    When the request is sent
    Then the response status is 409 The model is certified or managed by metric sync, or the update would remove a measure or property still used by an active metric.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric collection returns "Bad Request" response
    Given new "UpdateMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": []}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric collection returns "Conflict" response
    Given new "UpdateMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": []}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric collection returns "Not Found" response
    Given new "UpdateMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": []}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/experimentation
  Scenario: Update metric collection returns "OK" response
    Given new "UpdateMetricCollection" request
    And there is a valid "experiment_metric_collection" in the system
    And request contains "metric_collection_id" parameter from "experiment_metric_collection.data.id"
    And body with value {"data": {"type": "metric-collections", "attributes": {"name": "ex-{{ unique_hash }} updated"}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric collection returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "UpdateMetricCollection" request
    And request contains "metric_collection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": []}, "type": "metric-collections"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric returns "Malformed ID or body, or validation failure." response
    Given new "UpdateMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Checkout conversion"}, "id": "550e8400-e29b-41d4-a716-446655440020", "type": "metrics"}}
    When the request is sent
    Then the response status is 400 Malformed ID or body, or validation failure.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric returns "No metric with this ID exists for the organization." response
    Given new "UpdateMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Checkout conversion"}, "id": "550e8400-e29b-41d4-a716-446655440020", "type": "metrics"}}
    When the request is sent
    Then the response status is 404 No metric with this ID exists for the organization.

  @team:ddoghq/experimentation
  Scenario: Update metric returns "OK" response
    Given new "UpdateMetric" request
    And there is a valid "experiment_metric" in the system
    And request contains "metric_id" parameter from "experiment_metric.data.id"
    And body with value {"data": {"type": "metrics", "id": "{{ experiment_metric.data.id }}", "attributes": {"name": "ex-{{ unique_hash }} updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "ex-{{ unique_hash }} updated"

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric returns "Request body sent with a media type other than application/json or application/vnd.api+json." response
    Given new "UpdateMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Checkout conversion"}, "id": "550e8400-e29b-41d4-a716-446655440020", "type": "metrics"}}
    When the request is sent
    Then the response status is 415 Request body sent with a media type other than application/json or application/vnd.api+json.

  @generated @skip @team:ddoghq/experimentation
  Scenario: Update metric returns "The metric is imported, certified, or managed by metric sync, or another metric in this organization already uses one of these values." response
    Given new "UpdateMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Checkout conversion"}, "id": "550e8400-e29b-41d4-a716-446655440020", "type": "metrics"}}
    When the request is sent
    Then the response status is 409 The metric is imported, certified, or managed by metric sync, or another metric in this organization already uses one of these values.
