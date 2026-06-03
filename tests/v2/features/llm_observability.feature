@endpoint(llm-observability) @endpoint(llm-observability-v2)
Feature: LLM Observability
  Manage LLM Observability spans, data, projects, datasets, dataset records,
  experiments, and annotations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LLMObservability" API

  @skip @team:DataDog/ml-observability
  Scenario: Add a display_block interaction returns "Created" response
    Given operation "CreateLLMObsAnnotationQueueInteractions" enabled
    And new "CreateLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interactions": [{"type": "display_block", "display_block": [{"type": "markdown", "content": "## Triage Instructions"}]}]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:DataDog/ml-observability
  Scenario: Add a display_block interaction with an image block missing url returns "Bad Request" response
    Given operation "CreateLLMObsAnnotationQueueInteractions" enabled
    And new "CreateLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interactions": [{"type": "display_block", "display_block": [{"type": "image"}]}]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Add annotation queue interactions returns "Bad Request" response
    Given operation "CreateLLMObsAnnotationQueueInteractions" enabled
    And new "CreateLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interactions": [{"content_id": "trace-abc-123", "type": "trace"}]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Add annotation queue interactions returns "Created" response
    Given operation "CreateLLMObsAnnotationQueueInteractions" enabled
    And new "CreateLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interactions": [{"content_id": "trace-abc-123", "type": "trace"}]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Add annotation queue interactions returns "Not Found" response
    Given operation "CreateLLMObsAnnotationQueueInteractions" enabled
    And new "CreateLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interactions": [{"content_id": "trace-abc-123", "type": "trace"}]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Aggregate LLM Observability experimentation returns "Bad Request" response
    Given operation "AggregateLLMObsExperimentation" enabled
    And new "AggregateLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"aggregate": {"compute": [{"metric": "score_value", "name": "avg_faithfulness"}], "dataset_version": null, "group_by": [{"field": "span_id"}], "indexes": ["experiment-evals"], "limit": 1000, "search": {"query": "@experiment_id:3fd6b5e0-8910-4b1c-a7d0-5b84de329012"}, "time": {"from": 1705312200000, "to": 1705315800000}}}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Aggregate LLM Observability experimentation returns "OK" response
    Given operation "AggregateLLMObsExperimentation" enabled
    And new "AggregateLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"aggregate": {"compute": [{"metric": "score_value", "name": "avg_faithfulness"}], "dataset_version": null, "group_by": [{"field": "span_id"}], "indexes": ["experiment-evals"], "limit": 1000, "search": {"query": "@experiment_id:3fd6b5e0-8910-4b1c-a7d0-5b84de329012"}, "time": {"from": 1705312200000, "to": 1705315800000}}}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Append records to an LLM Observability dataset returns "Bad Request" response
    Given operation "CreateLLMObsDatasetRecords" enabled
    And new "CreateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Append records to an LLM Observability dataset returns "Created" response
    Given operation "CreateLLMObsDatasetRecords" enabled
    And new "CreateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Append records to an LLM Observability dataset returns "Not Found" response
    Given operation "CreateLLMObsDatasetRecords" enabled
    And new "CreateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Append records to an LLM Observability dataset returns "OK" response
    Given operation "CreateLLMObsDatasetRecords" enabled
    And new "CreateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Batch update LLM Observability dataset records returns "Bad Request" response
    Given operation "BatchUpdateLLMObsDataset" enabled
    And new "BatchUpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"create_new_version": true, "delete_records": [], "insert_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}, "tags": []}], "tags": [], "update_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}}]}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Batch update LLM Observability dataset records returns "Not Found" response
    Given operation "BatchUpdateLLMObsDataset" enabled
    And new "BatchUpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"create_new_version": true, "delete_records": [], "insert_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}, "tags": []}], "tags": [], "update_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}}]}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Batch update LLM Observability dataset records returns "OK" response
    Given operation "BatchUpdateLLMObsDataset" enabled
    And new "BatchUpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"create_new_version": true, "delete_records": [], "insert_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}, "tags": []}], "tags": [], "update_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}}]}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Batch update LLM Observability dataset records returns "Payload Too Large" response
    Given operation "BatchUpdateLLMObsDataset" enabled
    And new "BatchUpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"create_new_version": true, "delete_records": [], "insert_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}, "tags": []}], "tags": [], "update_records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null, "tag_operations": {"add": [], "remove": [], "set": []}}]}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:DataDog/ml-observability
  Scenario: Clone an LLM Observability dataset returns "Bad Request" response
    Given operation "CloneLLMObsDataset" enabled
    And new "CloneLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Clone of the original dataset for experimentation.", "name": "My cloned dataset"}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Clone an LLM Observability dataset returns "Not Found" response
    Given operation "CloneLLMObsDataset" enabled
    And new "CloneLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Clone of the original dataset for experimentation.", "name": "My cloned dataset"}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Clone an LLM Observability dataset returns "OK" response
    Given operation "CloneLLMObsDataset" enabled
    And new "CloneLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Clone of the original dataset for experimentation.", "name": "My cloned dataset"}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability annotation queue returns "Bad Request" response
    Given operation "CreateLLMObsAnnotationQueue" enabled
    And new "CreateLLMObsAnnotationQueue" request
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}, "description": "Queue for annotating customer support traces", "name": "My annotation queue", "project_id": "00000000-0000-0000-0000-000000000002"}, "type": "queues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability annotation queue returns "Created" response
    Given operation "CreateLLMObsAnnotationQueue" enabled
    And new "CreateLLMObsAnnotationQueue" request
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}, "description": "Queue for annotating customer support traces", "name": "My annotation queue", "project_id": "00000000-0000-0000-0000-000000000002"}, "type": "queues"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability dataset returns "Bad Request" response
    Given operation "CreateLLMObsDataset" enabled
    And new "CreateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My LLM Dataset"}, "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability dataset returns "Created" response
    Given operation "CreateLLMObsDataset" enabled
    And new "CreateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My LLM Dataset"}, "type": "datasets"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability dataset returns "Not Found" response
    Given operation "CreateLLMObsDataset" enabled
    And new "CreateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My LLM Dataset"}, "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability dataset returns "OK" response
    Given operation "CreateLLMObsDataset" enabled
    And new "CreateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My LLM Dataset"}, "type": "datasets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability experiment returns "Bad Request" response
    Given operation "CreateLLMObsExperiment" enabled
    And new "CreateLLMObsExperiment" request
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "name": "My Experiment v1", "parent_experiment_id": "3fd6b5e0-8910-4b1c-a7d0-5b84de329012", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability experiment returns "Created" response
    Given operation "CreateLLMObsExperiment" enabled
    And new "CreateLLMObsExperiment" request
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "name": "My Experiment v1", "parent_experiment_id": "3fd6b5e0-8910-4b1c-a7d0-5b84de329012", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability experiment returns "OK" response
    Given operation "CreateLLMObsExperiment" enabled
    And new "CreateLLMObsExperiment" request
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "name": "My Experiment v1", "parent_experiment_id": "3fd6b5e0-8910-4b1c-a7d0-5b84de329012", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability project returns "Bad Request" response
    Given operation "CreateLLMObsProject" enabled
    And new "CreateLLMObsProject" request
    And body with value {"data": {"attributes": {"name": "My LLM Project"}, "type": "projects"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability project returns "Created" response
    Given operation "CreateLLMObsProject" enabled
    And new "CreateLLMObsProject" request
    And body with value {"data": {"attributes": {"name": "My LLM Project"}, "type": "projects"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create an LLM Observability project returns "OK" response
    Given operation "CreateLLMObsProject" enabled
    And new "CreateLLMObsProject" request
    And body with value {"data": {"attributes": {"name": "My LLM Project"}, "type": "projects"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create or update a custom evaluator configuration returns "Bad Request" response
    Given operation "UpdateLLMObsCustomEvalConfig" enabled
    And new "UpdateLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "Custom", "eval_name": "my-custom-evaluator", "llm_judge_config": {"assessment_criteria": {"max_threshold": 1.0, "min_threshold": 0.7, "pass_values": ["pass", "yes"], "pass_when": true}, "inference_params": {"frequency_penalty": 0.0, "max_tokens": 1024, "presence_penalty": 0.0, "temperature": 0.7, "top_k": 50, "top_p": 1.0}, "last_used_library_prompt_template_name": "sentiment-analysis-v1", "modified_library_prompt_template": false, "output_schema": null, "parsing_type": "structured_output", "prompt_template": [{"content": "Rate the quality of the following response:", "contents": [{"type": "text", "value": {"text": "What is the sentiment of this review?", "tool_call": {"arguments": "{\"location\": \"San Francisco\"}", "id": "call_abc123", "name": "get_weather", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "sunny, 72F", "tool_id": "call_abc123", "type": "function"}}}], "role": "user"}]}, "llm_provider": {"bedrock": {"region": "us-east-1"}, "integration_account_id": "my-account-id", "integration_provider": "openai", "model_name": "gpt-4o", "vertex_ai": {"location": "us-central1", "project": "my-gcp-project"}}, "target": {"application_name": "my-llm-app", "enabled": true, "eval_scope": "span", "filter": "@service:my-service", "root_spans_only": true, "sampling_percentage": 50.0}}, "id": "my-custom-evaluator", "type": "evaluator_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create or update a custom evaluator configuration returns "Not Found" response
    Given operation "UpdateLLMObsCustomEvalConfig" enabled
    And new "UpdateLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "Custom", "eval_name": "my-custom-evaluator", "llm_judge_config": {"assessment_criteria": {"max_threshold": 1.0, "min_threshold": 0.7, "pass_values": ["pass", "yes"], "pass_when": true}, "inference_params": {"frequency_penalty": 0.0, "max_tokens": 1024, "presence_penalty": 0.0, "temperature": 0.7, "top_k": 50, "top_p": 1.0}, "last_used_library_prompt_template_name": "sentiment-analysis-v1", "modified_library_prompt_template": false, "output_schema": null, "parsing_type": "structured_output", "prompt_template": [{"content": "Rate the quality of the following response:", "contents": [{"type": "text", "value": {"text": "What is the sentiment of this review?", "tool_call": {"arguments": "{\"location\": \"San Francisco\"}", "id": "call_abc123", "name": "get_weather", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "sunny, 72F", "tool_id": "call_abc123", "type": "function"}}}], "role": "user"}]}, "llm_provider": {"bedrock": {"region": "us-east-1"}, "integration_account_id": "my-account-id", "integration_provider": "openai", "model_name": "gpt-4o", "vertex_ai": {"location": "us-central1", "project": "my-gcp-project"}}, "target": {"application_name": "my-llm-app", "enabled": true, "eval_scope": "span", "filter": "@service:my-service", "root_spans_only": true, "sampling_percentage": 50.0}}, "id": "my-custom-evaluator", "type": "evaluator_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create or update a custom evaluator configuration returns "OK" response
    Given operation "UpdateLLMObsCustomEvalConfig" enabled
    And new "UpdateLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "Custom", "eval_name": "my-custom-evaluator", "llm_judge_config": {"assessment_criteria": {"max_threshold": 1.0, "min_threshold": 0.7, "pass_values": ["pass", "yes"], "pass_when": true}, "inference_params": {"frequency_penalty": 0.0, "max_tokens": 1024, "presence_penalty": 0.0, "temperature": 0.7, "top_k": 50, "top_p": 1.0}, "last_used_library_prompt_template_name": "sentiment-analysis-v1", "modified_library_prompt_template": false, "output_schema": null, "parsing_type": "structured_output", "prompt_template": [{"content": "Rate the quality of the following response:", "contents": [{"type": "text", "value": {"text": "What is the sentiment of this review?", "tool_call": {"arguments": "{\"location\": \"San Francisco\"}", "id": "call_abc123", "name": "get_weather", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "sunny, 72F", "tool_id": "call_abc123", "type": "function"}}}], "role": "user"}]}, "llm_provider": {"bedrock": {"region": "us-east-1"}, "integration_account_id": "my-account-id", "integration_provider": "openai", "model_name": "gpt-4o", "vertex_ai": {"location": "us-central1", "project": "my-gcp-project"}}, "target": {"application_name": "my-llm-app", "enabled": true, "eval_scope": "span", "filter": "@service:my-service", "root_spans_only": true, "sampling_percentage": 50.0}}, "id": "my-custom-evaluator", "type": "evaluator_config"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Create or update a custom evaluator configuration returns "Unprocessable Entity" response
    Given operation "UpdateLLMObsCustomEvalConfig" enabled
    And new "UpdateLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "Custom", "eval_name": "my-custom-evaluator", "llm_judge_config": {"assessment_criteria": {"max_threshold": 1.0, "min_threshold": 0.7, "pass_values": ["pass", "yes"], "pass_when": true}, "inference_params": {"frequency_penalty": 0.0, "max_tokens": 1024, "presence_penalty": 0.0, "temperature": 0.7, "top_k": 50, "top_p": 1.0}, "last_used_library_prompt_template_name": "sentiment-analysis-v1", "modified_library_prompt_template": false, "output_schema": null, "parsing_type": "structured_output", "prompt_template": [{"content": "Rate the quality of the following response:", "contents": [{"type": "text", "value": {"text": "What is the sentiment of this review?", "tool_call": {"arguments": "{\"location\": \"San Francisco\"}", "id": "call_abc123", "name": "get_weather", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "sunny, 72F", "tool_id": "call_abc123", "type": "function"}}}], "role": "user"}]}, "llm_provider": {"bedrock": {"region": "us-east-1"}, "integration_account_id": "my-account-id", "integration_provider": "openai", "model_name": "gpt-4o", "vertex_ai": {"location": "us-central1", "project": "my-gcp-project"}}, "target": {"application_name": "my-llm-app", "enabled": true, "eval_scope": "span", "filter": "@service:my-service", "root_spans_only": true, "sampling_percentage": 50.0}}, "id": "my-custom-evaluator", "type": "evaluator_config"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability data returns "Accepted" response
    Given operation "DeleteLLMObsData" enabled
    And new "DeleteLLMObsData" request
    And body with value {"data": {"attributes": {"delay": 0, "from": 1705314600000, "query": {"query": "@trace_id:abc123def456"}, "to": 1705315200000}, "type": "create_deletion_req"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability data returns "Bad Request" response
    Given operation "DeleteLLMObsData" enabled
    And new "DeleteLLMObsData" request
    And body with value {"data": {"attributes": {"delay": 0, "from": 1705314600000, "query": {"query": "@trace_id:abc123def456"}, "to": 1705315200000}, "type": "create_deletion_req"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability dataset records returns "Bad Request" response
    Given operation "DeleteLLMObsDatasetRecords" enabled
    And new "DeleteLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"record_ids": ["rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c"]}, "type": "records"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability dataset records returns "No Content" response
    Given operation "DeleteLLMObsDatasetRecords" enabled
    And new "DeleteLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"record_ids": ["rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c"]}, "type": "records"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability dataset records returns "Not Found" response
    Given operation "DeleteLLMObsDatasetRecords" enabled
    And new "DeleteLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"record_ids": ["rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c"]}, "type": "records"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability datasets returns "Bad Request" response
    Given operation "DeleteLLMObsDatasets" enabled
    And new "DeleteLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_ids": ["9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d"]}, "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability datasets returns "No Content" response
    Given operation "DeleteLLMObsDatasets" enabled
    And new "DeleteLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_ids": ["9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d"]}, "type": "datasets"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability datasets returns "Not Found" response
    Given operation "DeleteLLMObsDatasets" enabled
    And new "DeleteLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_ids": ["9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d"]}, "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability experiments returns "Bad Request" response
    Given operation "DeleteLLMObsExperiments" enabled
    And new "DeleteLLMObsExperiments" request
    And body with value {"data": {"attributes": {"experiment_ids": ["3fd6b5e0-8910-4b1c-a7d0-5b84de329012"]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability experiments returns "No Content" response
    Given operation "DeleteLLMObsExperiments" enabled
    And new "DeleteLLMObsExperiments" request
    And body with value {"data": {"attributes": {"experiment_ids": ["3fd6b5e0-8910-4b1c-a7d0-5b84de329012"]}, "type": "experiments"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability projects returns "Bad Request" response
    Given operation "DeleteLLMObsProjects" enabled
    And new "DeleteLLMObsProjects" request
    And body with value {"data": {"attributes": {"project_ids": ["a33671aa-24fd-4dcd-9b33-a8ec7dde7751"]}, "type": "projects"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete LLM Observability projects returns "No Content" response
    Given operation "DeleteLLMObsProjects" enabled
    And new "DeleteLLMObsProjects" request
    And body with value {"data": {"attributes": {"project_ids": ["a33671aa-24fd-4dcd-9b33-a8ec7dde7751"]}, "type": "projects"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete a custom evaluator configuration returns "Bad Request" response
    Given operation "DeleteLLMObsCustomEvalConfig" enabled
    And new "DeleteLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete a custom evaluator configuration returns "No Content" response
    Given operation "DeleteLLMObsCustomEvalConfig" enabled
    And new "DeleteLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete a custom evaluator configuration returns "Not Found" response
    Given operation "DeleteLLMObsCustomEvalConfig" enabled
    And new "DeleteLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete an LLM Observability annotation queue returns "No Content" response
    Given operation "DeleteLLMObsAnnotationQueue" enabled
    And new "DeleteLLMObsAnnotationQueue" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete an LLM Observability annotation queue returns "Not Found" response
    Given operation "DeleteLLMObsAnnotationQueue" enabled
    And new "DeleteLLMObsAnnotationQueue" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete annotation queue interactions returns "Bad Request" response
    Given operation "DeleteLLMObsAnnotationQueueInteractions" enabled
    And new "DeleteLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interaction_ids": ["00000000-0000-0000-0000-000000000000", "00000000-0000-0000-0000-000000000001"]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete annotation queue interactions returns "No Content" response
    Given operation "DeleteLLMObsAnnotationQueueInteractions" enabled
    And new "DeleteLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interaction_ids": ["00000000-0000-0000-0000-000000000000", "00000000-0000-0000-0000-000000000001"]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete annotation queue interactions returns "Not Found" response
    Given operation "DeleteLLMObsAnnotationQueueInteractions" enabled
    And new "DeleteLLMObsAnnotationQueueInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interaction_ids": ["00000000-0000-0000-0000-000000000000", "00000000-0000-0000-0000-000000000001"]}, "type": "interactions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Export an LLM Observability dataset returns "Bad Request" response
    Given operation "ExportLLMObsDataset" enabled
    And new "ExportLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Export an LLM Observability dataset returns "Not Found" response
    Given operation "ExportLLMObsDataset" enabled
    And new "ExportLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Export an LLM Observability dataset returns "OK" response
    Given operation "ExportLLMObsDataset" enabled
    And new "ExportLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get LLM Observability dataset draft state returns "Bad Request" response
    Given operation "GetLLMObsDatasetDraftState" enabled
    And new "GetLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get LLM Observability dataset draft state returns "Not Found" response
    Given operation "GetLLMObsDatasetDraftState" enabled
    And new "GetLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get LLM Observability dataset draft state returns "OK" response
    Given operation "GetLLMObsDatasetDraftState" enabled
    And new "GetLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get a custom evaluator configuration returns "Bad Request" response
    Given operation "GetLLMObsCustomEvalConfig" enabled
    And new "GetLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get a custom evaluator configuration returns "Not Found" response
    Given operation "GetLLMObsCustomEvalConfig" enabled
    And new "GetLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get a custom evaluator configuration returns "OK" response
    Given operation "GetLLMObsCustomEvalConfig" enabled
    And new "GetLLMObsCustomEvalConfig" request
    And request contains "eval_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotated interactions by content IDs returns "Bad Request" response
    Given operation "GetLLMObsAnnotatedInteractionsByTraceIDs" enabled
    And new "GetLLMObsAnnotatedInteractionsByTraceIDs" request
    And request contains "contentIds" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotated interactions by content IDs returns "OK" response
    Given operation "GetLLMObsAnnotatedInteractionsByTraceIDs" enabled
    And new "GetLLMObsAnnotatedInteractionsByTraceIDs" request
    And request contains "contentIds" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotated queue interactions returns "Bad Request" response
    Given operation "GetLLMObsAnnotatedInteractions" enabled
    And new "GetLLMObsAnnotatedInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotated queue interactions returns "Not Found" response
    Given operation "GetLLMObsAnnotatedInteractions" enabled
    And new "GetLLMObsAnnotatedInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotated queue interactions returns "OK" response
    Given operation "GetLLMObsAnnotatedInteractions" enabled
    And new "GetLLMObsAnnotatedInteractions" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotation queue label schema returns "Not Found" response
    Given operation "GetLLMObsAnnotationQueueLabelSchema" enabled
    And new "GetLLMObsAnnotationQueueLabelSchema" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get annotation queue label schema returns "OK" response
    Given operation "GetLLMObsAnnotationQueueLabelSchema" enabled
    And new "GetLLMObsAnnotationQueueLabelSchema" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability annotation queues returns "Bad Request" response
    Given operation "ListLLMObsAnnotationQueues" enabled
    And new "ListLLMObsAnnotationQueues" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability annotation queues returns "OK" response
    Given operation "ListLLMObsAnnotationQueues" enabled
    And new "ListLLMObsAnnotationQueues" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset records returns "Bad Request" response
    Given operation "ListLLMObsDatasetRecords" enabled
    And new "ListLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset records returns "Not Found" response
    Given operation "ListLLMObsDatasetRecords" enabled
    And new "ListLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset records returns "OK" response
    Given operation "ListLLMObsDatasetRecords" enabled
    And new "ListLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset versions returns "Bad Request" response
    Given operation "ListLLMObsDatasetVersions" enabled
    And new "ListLLMObsDatasetVersions" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset versions returns "Not Found" response
    Given operation "ListLLMObsDatasetVersions" enabled
    And new "ListLLMObsDatasetVersions" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability dataset versions returns "OK" response
    Given operation "ListLLMObsDatasetVersions" enabled
    And new "ListLLMObsDatasetVersions" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability datasets returns "Bad Request" response
    Given operation "ListLLMObsDatasets" enabled
    And new "ListLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability datasets returns "Not Found" response
    Given operation "ListLLMObsDatasets" enabled
    And new "ListLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability datasets returns "OK" response
    Given operation "ListLLMObsDatasets" enabled
    And new "ListLLMObsDatasets" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment events (v2) returns "Bad Request" response
    Given operation "ListLLMObsExperimentEventsV2" enabled
    And new "ListLLMObsExperimentEventsV2" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment events (v2) returns "Not Found" response
    Given operation "ListLLMObsExperimentEventsV2" enabled
    And new "ListLLMObsExperimentEventsV2" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment events (v2) returns "OK" response
    Given operation "ListLLMObsExperimentEventsV2" enabled
    And new "ListLLMObsExperimentEventsV2" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment spans (v1) returns "Bad Request" response
    Given operation "ListLLMObsExperimentEventsV1" enabled
    And new "ListLLMObsExperimentEventsV1" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment spans (v1) returns "Not Found" response
    Given operation "ListLLMObsExperimentEventsV1" enabled
    And new "ListLLMObsExperimentEventsV1" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiment spans (v1) returns "OK" response
    Given operation "ListLLMObsExperimentEventsV1" enabled
    And new "ListLLMObsExperimentEventsV1" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiments returns "Bad Request" response
    Given operation "ListLLMObsExperiments" enabled
    And new "ListLLMObsExperiments" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability experiments returns "OK" response
    Given operation "ListLLMObsExperiments" enabled
    And new "ListLLMObsExperiments" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability projects returns "Bad Request" response
    Given operation "ListLLMObsProjects" enabled
    And new "ListLLMObsProjects" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability projects returns "OK" response
    Given operation "ListLLMObsProjects" enabled
    And new "ListLLMObsProjects" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability spans returns "Bad Request" response
    Given operation "ListLLMObsSpans" enabled
    And new "ListLLMObsSpans" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM Observability spans returns "OK" response
    Given operation "ListLLMObsSpans" enabled
    And new "ListLLMObsSpans" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM integration accounts returns "Bad Request" response
    Given operation "ListLLMObsIntegrationAccounts" enabled
    And new "ListLLMObsIntegrationAccounts" request
    And request contains "integration" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM integration accounts returns "OK" response
    Given operation "ListLLMObsIntegrationAccounts" enabled
    And new "ListLLMObsIntegrationAccounts" request
    And request contains "integration" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM integration models returns "Bad Request" response
    Given operation "ListLLMObsIntegrationModels" enabled
    And new "ListLLMObsIntegrationModels" request
    And request contains "integration" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List LLM integration models returns "OK" response
    Given operation "ListLLMObsIntegrationModels" enabled
    And new "ListLLMObsIntegrationModels" request
    And request contains "integration" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List events for an LLM Observability experiment returns "Bad Request" response
    Given operation "ListLLMObsExperimentEvents" enabled
    And new "ListLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List events for an LLM Observability experiment returns "Not Found" response
    Given operation "ListLLMObsExperimentEvents" enabled
    And new "ListLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: List events for an LLM Observability experiment returns "OK" response
    Given operation "ListLLMObsExperimentEvents" enabled
    And new "ListLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Lock LLM Observability dataset draft state returns "Bad Request" response
    Given operation "LockLLMObsDatasetDraftState" enabled
    And new "LockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Lock LLM Observability dataset draft state returns "Not Found" response
    Given operation "LockLLMObsDatasetDraftState" enabled
    And new "LockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Lock LLM Observability dataset draft state returns "OK" response
    Given operation "LockLLMObsDatasetDraftState" enabled
    And new "LockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Push events for an LLM Observability experiment returns "Accepted" response
    Given operation "CreateLLMObsExperimentEvents" enabled
    And new "CreateLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"assessment": "pass", "error": {}, "label": "faithfulness", "metric_type": "score", "span_id": "span-7a1b2c3d", "tags": [], "timestamp_ms": 1705314600000}], "spans": [{"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "duration": 1500000000, "meta": {"error": {"message": "Model response timed out", "stack": "Traceback (most recent call last):\n  File \"main.py\", line 10, in <module>\n    response = model.generate(input)\n  File \"model.py\", line 45, in generate\n    raise TimeoutError(\"Model response timed out\")\nTimeoutError: Model response timed out", "type": "TimeoutError"}, "input": null, "output": null}, "name": "llm_call", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751", "span_id": "span-7a1b2c3d", "start_ns": 1705314600000000000, "status": "ok", "tags": [], "trace_id": "abc123def456"}]}, "type": "events"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/ml-observability
  Scenario: Push events for an LLM Observability experiment returns "Bad Request" response
    Given operation "CreateLLMObsExperimentEvents" enabled
    And new "CreateLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"assessment": "pass", "error": {}, "label": "faithfulness", "metric_type": "score", "span_id": "span-7a1b2c3d", "tags": [], "timestamp_ms": 1705314600000}], "spans": [{"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "duration": 1500000000, "meta": {"error": {"message": "Model response timed out", "stack": "Traceback (most recent call last):\n  File \"main.py\", line 10, in <module>\n    response = model.generate(input)\n  File \"model.py\", line 45, in generate\n    raise TimeoutError(\"Model response timed out\")\nTimeoutError: Model response timed out", "type": "TimeoutError"}, "input": null, "output": null}, "name": "llm_call", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751", "span_id": "span-7a1b2c3d", "start_ns": 1705314600000000000, "status": "ok", "tags": [], "trace_id": "abc123def456"}]}, "type": "events"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Push events for an LLM Observability experiment returns "Not Found" response
    Given operation "CreateLLMObsExperimentEvents" enabled
    And new "CreateLLMObsExperimentEvents" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"metrics": [{"assessment": "pass", "error": {}, "label": "faithfulness", "metric_type": "score", "span_id": "span-7a1b2c3d", "tags": [], "timestamp_ms": 1705314600000}], "spans": [{"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "duration": 1500000000, "meta": {"error": {"message": "Model response timed out", "stack": "Traceback (most recent call last):\n  File \"main.py\", line 10, in <module>\n    response = model.generate(input)\n  File \"model.py\", line 45, in generate\n    raise TimeoutError(\"Model response timed out\")\nTimeoutError: Model response timed out", "type": "TimeoutError"}, "input": null, "output": null}, "name": "llm_call", "project_id": "a33671aa-24fd-4dcd-9b33-a8ec7dde7751", "span_id": "span-7a1b2c3d", "start_ns": 1705314600000000000, "status": "ok", "tags": [], "trace_id": "abc123def456"}]}, "type": "events"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Restore an LLM Observability dataset version returns "Bad Request" response
    Given operation "RestoreLLMObsDatasetVersion" enabled
    And new "RestoreLLMObsDatasetVersion" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_version": 1}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Restore an LLM Observability dataset version returns "Not Found" response
    Given operation "RestoreLLMObsDatasetVersion" enabled
    And new "RestoreLLMObsDatasetVersion" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_version": 1}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Restore an LLM Observability dataset version returns "OK" response
    Given operation "RestoreLLMObsDatasetVersion" enabled
    And new "RestoreLLMObsDatasetVersion" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_version": 1}, "id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "type": "datasets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Run an LLM inference returns "Bad Request" response
    Given operation "CreateLLMObsIntegrationInference" enabled
    And new "CreateLLMObsIntegrationInference" request
    And request contains "integration" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"anthropic_metadata": {"effort": "medium", "thinking": {"budget_tokens": 1024, "type": "enabled"}}, "azure_openai_metadata": {"deployment_id": "my-gpt4-deployment", "model_version": "0613", "resource_name": "my-azure-resource"}, "bedrock_metadata": {"region": "us-east-1"}, "frequency_penalty": 0.0, "json_schema": "{\"type\":\"object\",\"properties\":{\"answer\":{\"type\":\"string\"}}}", "max_completion_tokens": 1024, "max_tokens": 1024, "messages": [{"content": "What is the capital of France?", "contents": [{"type": "text", "value": {"text": "Hello, how can I help you?", "tool_call": {"arguments": {"location": "San Francisco"}, "name": "get_weather", "tool_id": "call_abc123", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "The weather in San Francisco is 68\u00b0F and sunny.", "tool_id": "call_abc123", "type": "function"}}}], "id": "msg_001", "role": "user", "tool_calls": [{"arguments": {"location": "San Francisco"}, "name": "get_weather", "tool_id": "call_abc123", "type": "function"}], "tool_results": [{"name": "get_weather", "result": "The weather in San Francisco is 68\u00b0F and sunny.", "tool_id": "call_abc123", "type": "function"}]}], "model_id": "gpt-4o", "openai_metadata": {"reasoning_effort": "medium", "reasoning_summary": "auto"}, "presence_penalty": 0.0, "temperature": 0.7, "tools": [{"function": {"description": "Get the current weather for a location.", "name": "get_weather", "parameters": {"properties": {"location": {"type": "string"}}, "type": "object"}}, "type": "function"}], "top_k": 50, "top_p": 1.0, "vertex_ai_metadata": {"location": "us-central1", "project": "my-gcp-project", "project_ids": ["my-gcp-project"]}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Run an LLM inference returns "OK" response
    Given operation "CreateLLMObsIntegrationInference" enabled
    And new "CreateLLMObsIntegrationInference" request
    And request contains "integration" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"anthropic_metadata": {"effort": "medium", "thinking": {"budget_tokens": 1024, "type": "enabled"}}, "azure_openai_metadata": {"deployment_id": "my-gpt4-deployment", "model_version": "0613", "resource_name": "my-azure-resource"}, "bedrock_metadata": {"region": "us-east-1"}, "frequency_penalty": 0.0, "json_schema": "{\"type\":\"object\",\"properties\":{\"answer\":{\"type\":\"string\"}}}", "max_completion_tokens": 1024, "max_tokens": 1024, "messages": [{"content": "What is the capital of France?", "contents": [{"type": "text", "value": {"text": "Hello, how can I help you?", "tool_call": {"arguments": {"location": "San Francisco"}, "name": "get_weather", "tool_id": "call_abc123", "type": "function"}, "tool_call_result": {"name": "get_weather", "result": "The weather in San Francisco is 68\u00b0F and sunny.", "tool_id": "call_abc123", "type": "function"}}}], "id": "msg_001", "role": "user", "tool_calls": [{"arguments": {"location": "San Francisco"}, "name": "get_weather", "tool_id": "call_abc123", "type": "function"}], "tool_results": [{"name": "get_weather", "result": "The weather in San Francisco is 68\u00b0F and sunny.", "tool_id": "call_abc123", "type": "function"}]}], "model_id": "gpt-4o", "openai_metadata": {"reasoning_effort": "medium", "reasoning_summary": "auto"}, "presence_penalty": 0.0, "temperature": 0.7, "tools": [{"function": {"description": "Get the current weather for a location.", "name": "get_weather", "parameters": {"properties": {"location": {"type": "string"}}, "type": "object"}}, "type": "function"}], "top_k": 50, "top_p": 1.0, "vertex_ai_metadata": {"location": "us-central1", "project": "my-gcp-project", "project_ids": ["my-gcp-project"]}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Search LLM Observability experimentation entities returns "Bad Request" response
    Given operation "SearchLLMObsExperimentation" enabled
    And new "SearchLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"content_preview": {"limit": 500}, "filter": {"include_deleted": false, "is_deleted": false, "query": "my experiment", "scope": ["experiments"], "version": null}, "include": {"user_data": false}, "page": {"limit": 100}}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Search LLM Observability experimentation entities returns "OK — all results returned in a single page." response
    Given operation "SearchLLMObsExperimentation" enabled
    And new "SearchLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"content_preview": {"limit": 500}, "filter": {"include_deleted": false, "is_deleted": false, "query": "my experiment", "scope": ["experiments"], "version": null}, "include": {"user_data": false}, "page": {"limit": 100}}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 200 OK — all results returned in a single page.

  @generated @skip @team:DataDog/ml-observability
  Scenario: Search LLM Observability experimentation entities returns "Partial Content — more results are available. Use `meta.after` as the next `page.cursor`." response
    Given operation "SearchLLMObsExperimentation" enabled
    And new "SearchLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"content_preview": {"limit": 500}, "filter": {"include_deleted": false, "is_deleted": false, "query": "my experiment", "scope": ["experiments"], "version": null}, "include": {"user_data": false}, "page": {"limit": 100}}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 206 Partial Content — more results are available. Use `meta.after` as the next `page.cursor`.

  @generated @skip @team:DataDog/ml-observability
  Scenario: Search LLM Observability spans returns "Bad Request" response
    Given operation "SearchLLMObsSpans" enabled
    And new "SearchLLMObsSpans" request
    And body with value {"data": {"attributes": {"filter": {"from": "now-900s", "ml_app": "my-llm-app", "query": "@session_id:abc123def456", "span_id": "abc123def456", "span_kind": "llm", "span_name": "llm_call", "to": "now", "trace_id": "trace-9a8b7c6d5e4f"}, "options": {"include_attachments": true, "time_offset": 0}, "page": {"cursor": "eyJzdGFydCI6MTAwfQ==", "limit": 10}, "sort": "-start_ns"}, "type": "spans"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Search LLM Observability spans returns "OK" response
    Given operation "SearchLLMObsSpans" enabled
    And new "SearchLLMObsSpans" request
    And body with value {"data": {"attributes": {"filter": {"from": "now-900s", "ml_app": "my-llm-app", "query": "@session_id:abc123def456", "span_id": "abc123def456", "span_kind": "llm", "span_name": "llm_call", "to": "now", "trace_id": "trace-9a8b7c6d5e4f"}, "options": {"include_attachments": true, "time_offset": 0}, "page": {"cursor": "eyJzdGFydCI6MTAwfQ==", "limit": 10}, "sort": "-start_ns"}, "type": "spans"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Simple search experimentation entities returns "Bad Request" response
    Given operation "SimpleSearchLLMObsExperimentation" enabled
    And new "SimpleSearchLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"content_preview": {"limit": 500}, "filter": {"include_deleted": false, "is_deleted": false, "query": "my experiment", "scope": ["experiments"], "version": null}, "include": {"user_data": false}, "page": {"limit": 50, "number": 1}, "sort": [{"direction": "desc", "field": "created_at"}]}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Simple search experimentation entities returns "OK" response
    Given operation "SimpleSearchLLMObsExperimentation" enabled
    And new "SimpleSearchLLMObsExperimentation" request
    And body with value {"data": {"attributes": {"content_preview": {"limit": 500}, "filter": {"include_deleted": false, "is_deleted": false, "query": "my experiment", "scope": ["experiments"], "version": null}, "include": {"user_data": false}, "page": {"limit": 50, "number": 1}, "sort": [{"direction": "desc", "field": "created_at"}]}, "type": "experimentation"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Unlock LLM Observability dataset draft state returns "Bad Request" response
    Given operation "UnlockLLMObsDatasetDraftState" enabled
    And new "UnlockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Unlock LLM Observability dataset draft state returns "Not Found" response
    Given operation "UnlockLLMObsDatasetDraftState" enabled
    And new "UnlockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Unlock LLM Observability dataset draft state returns "OK" response
    Given operation "UnlockLLMObsDatasetDraftState" enabled
    And new "UnlockLLMObsDatasetDraftState" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update LLM Observability dataset records returns "Bad Request" response
    Given operation "UpdateLLMObsDatasetRecords" enabled
    And new "UpdateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update LLM Observability dataset records returns "Not Found" response
    Given operation "UpdateLLMObsDatasetRecords" enabled
    And new "UpdateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update LLM Observability dataset records returns "OK" response
    Given operation "UpdateLLMObsDatasetRecords" enabled
    And new "UpdateLLMObsDatasetRecords" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"records": [{"expected_output": null, "id": "rec-7c3f5a1b-9e2d-4f8a-b1c6-3d7e9f0a2b4c", "input": null}]}, "type": "records"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability annotation queue returns "Bad Request" response
    Given operation "UpdateLLMObsAnnotationQueue" enabled
    And new "UpdateLLMObsAnnotationQueue" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}, "description": "Updated description", "name": "Updated queue name"}, "type": "queues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability annotation queue returns "Not Found" response
    Given operation "UpdateLLMObsAnnotationQueue" enabled
    And new "UpdateLLMObsAnnotationQueue" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}, "description": "Updated description", "name": "Updated queue name"}, "type": "queues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability annotation queue returns "OK" response
    Given operation "UpdateLLMObsAnnotationQueue" enabled
    And new "UpdateLLMObsAnnotationQueue" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}, "description": "Updated description", "name": "Updated queue name"}, "type": "queues"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability dataset returns "Bad Request" response
    Given operation "UpdateLLMObsDataset" enabled
    And new "UpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "datasets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability dataset returns "Not Found" response
    Given operation "UpdateLLMObsDataset" enabled
    And new "UpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "datasets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability dataset returns "OK" response
    Given operation "UpdateLLMObsDataset" enabled
    And new "UpdateLLMObsDataset" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "datasets"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability experiment returns "Bad Request" response
    Given operation "UpdateLLMObsExperiment" enabled
    And new "UpdateLLMObsExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "status": "completed"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability experiment returns "Not Found" response
    Given operation "UpdateLLMObsExperiment" enabled
    And new "UpdateLLMObsExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "status": "completed"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability experiment returns "OK" response
    Given operation "UpdateLLMObsExperiment" enabled
    And new "UpdateLLMObsExperiment" request
    And request contains "experiment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"dataset_id": "9f64e5c7-dc5a-45c8-a17c-1b85f0bec97d", "status": "completed"}, "type": "experiments"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability project returns "Bad Request" response
    Given operation "UpdateLLMObsProject" enabled
    And new "UpdateLLMObsProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "projects"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability project returns "Not Found" response
    Given operation "UpdateLLMObsProject" enabled
    And new "UpdateLLMObsProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "projects"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update an LLM Observability project returns "OK" response
    Given operation "UpdateLLMObsProject" enabled
    And new "UpdateLLMObsProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "projects"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update annotation queue label schema returns "Bad Request" response
    Given operation "UpdateLLMObsAnnotationQueueLabelSchema" enabled
    And new "UpdateLLMObsAnnotationQueueLabelSchema" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}}, "type": "queues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update annotation queue label schema returns "Not Found" response
    Given operation "UpdateLLMObsAnnotationQueueLabelSchema" enabled
    And new "UpdateLLMObsAnnotationQueueLabelSchema" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}}, "type": "queues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Update annotation queue label schema returns "OK" response
    Given operation "UpdateLLMObsAnnotationQueueLabelSchema" enabled
    And new "UpdateLLMObsAnnotationQueueLabelSchema" request
    And request contains "queue_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"annotation_schema": {"label_schemas": [{"description": "Rating of the response quality.", "has_assessment": false, "has_reasoning": false, "id": "abc-123", "is_assessment": false, "is_integer": false, "is_required": true, "max": 5.0, "min": 0.0, "name": "quality", "type": "score", "values": ["good", "bad", "neutral"]}]}}, "type": "queues"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Upload records to an LLM Observability dataset returns "Bad Request" response
    Given operation "UploadLLMObsDatasetRecordsFile" enabled
    And new "UploadLLMObsDatasetRecordsFile" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Upload records to an LLM Observability dataset returns "Not Found" response
    Given operation "UploadLLMObsDatasetRecordsFile" enabled
    And new "UploadLLMObsDatasetRecordsFile" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Upload records to an LLM Observability dataset returns "OK" response
    Given operation "UploadLLMObsDatasetRecordsFile" enabled
    And new "UploadLLMObsDatasetRecordsFile" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
