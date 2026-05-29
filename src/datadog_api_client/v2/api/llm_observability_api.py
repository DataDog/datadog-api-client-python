# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.llm_obs_custom_eval_config_response import LLMObsCustomEvalConfigResponse
from datadog_api_client.v2.model.llm_obs_custom_eval_config_update_request import LLMObsCustomEvalConfigUpdateRequest
from datadog_api_client.v2.model.llm_obs_data_deletion_response import LLMObsDataDeletionResponse
from datadog_api_client.v2.model.llm_obs_data_deletion_request import LLMObsDataDeletionRequest
from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_response import (
    LLMObsAnnotatedInteractionsByTraceResponse,
)
from datadog_api_client.v2.model.llm_obs_annotation_queues_response import LLMObsAnnotationQueuesResponse
from datadog_api_client.v2.model.llm_obs_annotation_queue_response import LLMObsAnnotationQueueResponse
from datadog_api_client.v2.model.llm_obs_annotation_queue_request import LLMObsAnnotationQueueRequest
from datadog_api_client.v2.model.llm_obs_annotation_queue_update_request import LLMObsAnnotationQueueUpdateRequest
from datadog_api_client.v2.model.llm_obs_annotated_interactions_response import LLMObsAnnotatedInteractionsResponse
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_response import (
    LLMObsAnnotationQueueInteractionsResponse,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_request import (
    LLMObsAnnotationQueueInteractionsRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_annotation_queue_interactions_request import (
    LLMObsDeleteAnnotationQueueInteractionsRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_label_schema_response import (
    LLMObsAnnotationQueueLabelSchemaResponse,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_label_schema_update_request import (
    LLMObsAnnotationQueueLabelSchemaUpdateRequest,
)
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_response import (
    LLMObsExperimentationAnalyticsResponse,
)
from datadog_api_client.v2.model.llm_obs_experimentation_analytics_request import LLMObsExperimentationAnalyticsRequest
from datadog_api_client.v2.model.llm_obs_experimentation_search_response import LLMObsExperimentationSearchResponse
from datadog_api_client.v2.model.llm_obs_experimentation_search_request import LLMObsExperimentationSearchRequest
from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_response import (
    LLMObsExperimentationSimpleSearchResponse,
)
from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_request import (
    LLMObsExperimentationSimpleSearchRequest,
)
from datadog_api_client.v2.model.llm_obs_experiments_response import LLMObsExperimentsResponse
from datadog_api_client.v2.model.llm_obs_experiment_response import LLMObsExperimentResponse
from datadog_api_client.v2.model.llm_obs_experiment_request import LLMObsExperimentRequest
from datadog_api_client.v2.model.llm_obs_delete_experiments_request import LLMObsDeleteExperimentsRequest
from datadog_api_client.v2.model.llm_obs_experiment_update_request import LLMObsExperimentUpdateRequest
from datadog_api_client.v2.model.llm_obs_experiment_events_request import LLMObsExperimentEventsRequest
from datadog_api_client.v2.model.llm_obs_integration_account import LLMObsIntegrationAccount
from datadog_api_client.v2.model.llm_obs_integration_name import LLMObsIntegrationName
from datadog_api_client.v2.model.llm_obs_integration_inference_response import LLMObsIntegrationInferenceResponse
from datadog_api_client.v2.model.llm_obs_integration_inference_request import LLMObsIntegrationInferenceRequest
from datadog_api_client.v2.model.llm_obs_integration_model import LLMObsIntegrationModel
from datadog_api_client.v2.model.llm_obs_projects_response import LLMObsProjectsResponse
from datadog_api_client.v2.model.llm_obs_project_response import LLMObsProjectResponse
from datadog_api_client.v2.model.llm_obs_project_request import LLMObsProjectRequest
from datadog_api_client.v2.model.llm_obs_delete_projects_request import LLMObsDeleteProjectsRequest
from datadog_api_client.v2.model.llm_obs_project_update_request import LLMObsProjectUpdateRequest
from datadog_api_client.v2.model.llm_obs_spans_response import LLMObsSpansResponse
from datadog_api_client.v2.model.llm_obs_search_spans_request import LLMObsSearchSpansRequest
from datadog_api_client.v2.model.llm_obs_datasets_response import LLMObsDatasetsResponse
from datadog_api_client.v2.model.llm_obs_dataset_response import LLMObsDatasetResponse
from datadog_api_client.v2.model.llm_obs_dataset_request import LLMObsDatasetRequest
from datadog_api_client.v2.model.llm_obs_delete_datasets_request import LLMObsDeleteDatasetsRequest
from datadog_api_client.v2.model.llm_obs_dataset_update_request import LLMObsDatasetUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_records_mutation_response import LLMObsDatasetRecordsMutationResponse
from datadog_api_client.v2.model.llm_obs_dataset_batch_update_request import LLMObsDatasetBatchUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_clone_request import LLMObsDatasetCloneRequest
from datadog_api_client.v2.model.llm_obs_dataset_draft_state_response import LLMObsDatasetDraftStateResponse
from datadog_api_client.v2.model.llm_obs_dataset_export_format import LLMObsDatasetExportFormat
from datadog_api_client.v2.model.llm_obs_dataset_records_list_response import LLMObsDatasetRecordsListResponse
from datadog_api_client.v2.model.llm_obs_dataset_records_update_request import LLMObsDatasetRecordsUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_records_request import LLMObsDatasetRecordsRequest
from datadog_api_client.v2.model.llm_obs_delete_dataset_records_request import LLMObsDeleteDatasetRecordsRequest
from datadog_api_client.v2.model.llm_obs_dataset_restore_version_request import LLMObsDatasetRestoreVersionRequest
from datadog_api_client.v2.model.llm_obs_dataset_versions_response import LLMObsDatasetVersionsResponse
from datadog_api_client.v2.model.llm_obs_experiment_events_v2_response import LLMObsExperimentEventsV2Response


class LLMObservabilityApi:
    """
    Manage LLM Observability spans, data, projects, datasets, dataset records, experiments, and annotations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._aggregate_llm_obs_experimentation_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentationAnalyticsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experimentation/analytics",
                "operation_id": "aggregate_llm_obs_experimentation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentationAnalyticsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._batch_update_llm_obs_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetRecordsMutationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/batch_update",
                "operation_id": "batch_update_llm_obs_dataset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetBatchUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._clone_llm_obs_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/clone",
                "operation_id": "clone_llm_obs_dataset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetCloneRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_annotation_queue_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues",
                "operation_id": "create_llm_obs_annotation_queue",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsAnnotationQueueRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_annotation_queue_interactions_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueueInteractionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}/interactions",
                "operation_id": "create_llm_obs_annotation_queue_interactions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsAnnotationQueueInteractionsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets",
                "operation_id": "create_llm_obs_dataset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_dataset_records_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetRecordsMutationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/records",
                "operation_id": "create_llm_obs_dataset_records",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetRecordsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_experiment_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experiments",
                "operation_id": "create_llm_obs_experiment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_experiment_events_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experiments/{experiment_id}/events",
                "operation_id": "create_llm_obs_experiment_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentEventsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_integration_inference_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsIntegrationInferenceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/integrations/{integration}/{account_id}/inference",
                "operation_id": "create_llm_obs_integration_inference",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "integration": {
                    "required": True,
                    "openapi_types": (LLMObsIntegrationName,),
                    "attribute": "integration",
                    "location": "path",
                },
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsIntegrationInferenceRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_llm_obs_project_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/projects",
                "operation_id": "create_llm_obs_project",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsProjectRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_annotation_queue_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}",
                "operation_id": "delete_llm_obs_annotation_queue",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_llm_obs_annotation_queue_interactions_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}/interactions/delete",
                "operation_id": "delete_llm_obs_annotation_queue_interactions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDeleteAnnotationQueueInteractionsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_custom_eval_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/llm-obs/config/evaluators/custom/{eval_name}",
                "operation_id": "delete_llm_obs_custom_eval_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "eval_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "eval_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_llm_obs_data_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDataDeletionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/deletion/data/llmobs",
                "operation_id": "delete_llm_obs_data",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDataDeletionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_dataset_records_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/records/delete",
                "operation_id": "delete_llm_obs_dataset_records",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDeleteDatasetRecordsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_datasets_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/delete",
                "operation_id": "delete_llm_obs_datasets",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDeleteDatasetsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_experiments_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experiments/delete",
                "operation_id": "delete_llm_obs_experiments",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDeleteExperimentsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_llm_obs_projects_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/projects/delete",
                "operation_id": "delete_llm_obs_projects",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDeleteProjectsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._export_llm_obs_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (str,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/export",
                "operation_id": "export_llm_obs_dataset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "format": {
                    "openapi_types": (LLMObsDatasetExportFormat,),
                    "attribute": "format",
                    "location": "query",
                },
                "version": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "version",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["text/csv", "application/json"],
            },
            api_client=api_client,
        )

        self._get_llm_obs_annotated_interactions_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotatedInteractionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}/annotated-interactions",
                "operation_id": "get_llm_obs_annotated_interactions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_llm_obs_annotated_interactions_by_trace_i_ds_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotatedInteractionsByTraceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotated-interactions",
                "operation_id": "get_llm_obs_annotated_interactions_by_trace_i_ds",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "content_ids": {
                    "required": True,
                    "openapi_types": ([str],),
                    "attribute": "contentIds",
                    "location": "query",
                    "collection_format": "multi",
                },
                "offset": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_llm_obs_annotation_queue_label_schema_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueueLabelSchemaResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}/label-schema",
                "operation_id": "get_llm_obs_annotation_queue_label_schema",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_llm_obs_custom_eval_config_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsCustomEvalConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/llm-obs/config/evaluators/custom/{eval_name}",
                "operation_id": "get_llm_obs_custom_eval_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "eval_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "eval_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_llm_obs_dataset_draft_state_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetDraftStateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/draft_state",
                "operation_id": "get_llm_obs_dataset_draft_state",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_annotation_queues_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueuesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues",
                "operation_id": "list_llm_obs_annotation_queues",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "openapi_types": (str,),
                    "attribute": "projectId",
                    "location": "query",
                },
                "queue_ids": {
                    "openapi_types": ([str],),
                    "attribute": "queueIds",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_dataset_records_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetRecordsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/records",
                "operation_id": "list_llm_obs_dataset_records",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "filter_version": {
                    "openapi_types": (int,),
                    "attribute": "filter[version]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_datasets_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets",
                "operation_id": "list_llm_obs_datasets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
                "filter_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[id]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_dataset_versions_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetVersionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/versions",
                "operation_id": "list_llm_obs_dataset_versions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_experiment_events_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentEventsV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v3/experiments/{experiment_id}/events",
                "operation_id": "list_llm_obs_experiment_events",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_experiments_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experiments",
                "operation_id": "list_llm_obs_experiments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_project_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[project_id]",
                    "location": "query",
                },
                "filter_dataset_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[dataset_id]",
                    "location": "query",
                },
                "filter_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[id]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": ([LLMObsIntegrationAccount],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/integrations/{integration}/accounts",
                "operation_id": "list_llm_obs_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration": {
                    "required": True,
                    "openapi_types": (LLMObsIntegrationName,),
                    "attribute": "integration",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_integration_models_endpoint = _Endpoint(
            settings={
                "response_type": ([LLMObsIntegrationModel],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/integrations/{integration}/{account_id}/models",
                "operation_id": "list_llm_obs_integration_models",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration": {
                    "required": True,
                    "openapi_types": (LLMObsIntegrationName,),
                    "attribute": "integration",
                    "location": "path",
                },
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_projects_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsProjectsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/projects",
                "operation_id": "list_llm_obs_projects",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[id]",
                    "location": "query",
                },
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_llm_obs_spans_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsSpansResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/spans/events",
                "operation_id": "list_llm_obs_spans",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_from": {
                    "openapi_types": (str,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (str,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_span_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[span_id]",
                    "location": "query",
                },
                "filter_trace_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[trace_id]",
                    "location": "query",
                },
                "filter_span_kind": {
                    "openapi_types": (str,),
                    "attribute": "filter[span_kind]",
                    "location": "query",
                },
                "filter_span_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[span_name]",
                    "location": "query",
                },
                "filter_ml_app": {
                    "openapi_types": (str,),
                    "attribute": "filter[ml_app]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "include_attachments": {
                    "openapi_types": (bool,),
                    "attribute": "include_attachments",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._lock_llm_obs_dataset_draft_state_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetDraftStateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/draft_state/lock",
                "operation_id": "lock_llm_obs_dataset_draft_state",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._restore_llm_obs_dataset_version_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/restore",
                "operation_id": "restore_llm_obs_dataset_version",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetRestoreVersionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_llm_obs_experimentation_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentationSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experimentation/search",
                "operation_id": "search_llm_obs_experimentation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentationSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_llm_obs_spans_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsSpansResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/spans/events/search",
                "operation_id": "search_llm_obs_spans",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsSearchSpansRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._simple_search_llm_obs_experimentation_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentationSimpleSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experimentation/simple-search",
                "operation_id": "simple_search_llm_obs_experimentation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentationSimpleSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._unlock_llm_obs_dataset_draft_state_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/draft_state/unlock",
                "operation_id": "unlock_llm_obs_dataset_draft_state",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._update_llm_obs_annotation_queue_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}",
                "operation_id": "update_llm_obs_annotation_queue",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsAnnotationQueueUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_annotation_queue_label_schema_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsAnnotationQueueLabelSchemaResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/annotation-queues/{queue_id}/label-schema",
                "operation_id": "update_llm_obs_annotation_queue_label_schema",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "queue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "queue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsAnnotationQueueLabelSchemaUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_custom_eval_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/llm-obs/config/evaluators/custom/{eval_name}",
                "operation_id": "update_llm_obs_custom_eval_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "eval_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "eval_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsCustomEvalConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}",
                "operation_id": "update_llm_obs_dataset",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_dataset_records_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsDatasetRecordsMutationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/{project_id}/datasets/{dataset_id}/records",
                "operation_id": "update_llm_obs_dataset_records",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsDatasetRecordsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_experiment_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsExperimentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/experiments/{experiment_id}",
                "operation_id": "update_llm_obs_experiment",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsExperimentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_llm_obs_project_endpoint = _Endpoint(
            settings={
                "response_type": (LLMObsProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v1/projects/{project_id}",
                "operation_id": "update_llm_obs_project",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LLMObsProjectUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_llm_obs_dataset_records_file_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/llm-obs/v2/{project_id}/datasets/{dataset_id}/records/upload",
                "operation_id": "upload_llm_obs_dataset_records_file",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "deduplicate": {
                    "openapi_types": (bool,),
                    "attribute": "deduplicate",
                    "location": "query",
                },
                "overwrite": {
                    "openapi_types": (bool,),
                    "attribute": "overwrite",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": ([str],),
                    "attribute": "tags",
                    "location": "query",
                    "collection_format": "multi",
                },
                "include_user_data": {
                    "openapi_types": (bool,),
                    "attribute": "include[user_data]",
                    "location": "query",
                },
                "file": {
                    "openapi_types": (file_type,),
                    "attribute": "file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def aggregate_llm_obs_experimentation(
        self,
        body: LLMObsExperimentationAnalyticsRequest,
    ) -> LLMObsExperimentationAnalyticsResponse:
        """Aggregate LLM Observability experimentation.

        Execute an analytics aggregation over LLM Observability experimentation data.
        Use this endpoint to compute metrics (for example average eval scores) grouped by fields such as ``span_id`` or ``experiment_id``.

        At least one ``compute`` definition and one ``index`` must be provided.

        :param body: Analytics payload.
        :type body: LLMObsExperimentationAnalyticsRequest
        :rtype: LLMObsExperimentationAnalyticsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._aggregate_llm_obs_experimentation_endpoint.call_with_http_info(**kwargs)

    def batch_update_llm_obs_dataset(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetBatchUpdateRequest,
    ) -> LLMObsDatasetRecordsMutationResponse:
        """Batch update LLM Observability dataset records.

        Insert, update, and delete records in a single dataset operation. By default, a new dataset version is created when the batch is applied.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Batch update payload.
        :type body: LLMObsDatasetBatchUpdateRequest
        :rtype: LLMObsDatasetRecordsMutationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._batch_update_llm_obs_dataset_endpoint.call_with_http_info(**kwargs)

    def clone_llm_obs_dataset(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetCloneRequest,
    ) -> LLMObsDatasetResponse:
        """Clone an LLM Observability dataset.

        Clone a dataset, copying its current records into a new dataset within the same project.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the source LLM Observability dataset to clone.
        :type dataset_id: str
        :param body: Clone dataset payload.
        :type body: LLMObsDatasetCloneRequest
        :rtype: LLMObsDatasetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._clone_llm_obs_dataset_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_annotation_queue(
        self,
        body: LLMObsAnnotationQueueRequest,
    ) -> LLMObsAnnotationQueueResponse:
        """Create an LLM Observability annotation queue.

        Create an annotation queue. The ``name`` and ``project_id`` fields are required.
        An optional ``annotation_schema`` can be provided to define the labels for the queue.
        Fields such as ``created_by`` , ``owned_by`` , ``created_at`` , ``modified_by`` ,
        and ``modified_at`` are inferred by the backend.

        :param body: Create annotation queue payload.
        :type body: LLMObsAnnotationQueueRequest
        :rtype: LLMObsAnnotationQueueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_llm_obs_annotation_queue_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_annotation_queue_interactions(
        self,
        queue_id: str,
        body: LLMObsAnnotationQueueInteractionsRequest,
    ) -> LLMObsAnnotationQueueInteractionsResponse:
        """Add annotation queue interactions.

        Add one or more interactions to an annotation queue. At least one
        interaction must be provided. Each interaction has a ``type`` :

        * ``trace`` , ``experiment_trace`` , ``session`` : ``content_id`` references the
          upstream entity; the server fetches the actual content.
        * ``display_block`` : omit ``content_id`` and provide the rendered content
          in ``display_block``. The server generates ``content_id`` as a
          deterministic hash of the block list.

        Items of different types can be mixed in a single request.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :param body: Add interactions payload.
        :type body: LLMObsAnnotationQueueInteractionsRequest
        :rtype: LLMObsAnnotationQueueInteractionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        kwargs["body"] = body

        return self._create_llm_obs_annotation_queue_interactions_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_dataset(
        self,
        project_id: str,
        body: LLMObsDatasetRequest,
    ) -> LLMObsDatasetResponse:
        """Create an LLM Observability dataset.

        Create a new LLM Observability dataset within the specified project.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param body: Create dataset payload.
        :type body: LLMObsDatasetRequest
        :rtype: LLMObsDatasetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._create_llm_obs_dataset_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_dataset_records(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetRecordsRequest,
    ) -> LLMObsDatasetRecordsMutationResponse:
        """Append records to an LLM Observability dataset.

        Append one or more records to an LLM Observability dataset.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Append records payload.
        :type body: LLMObsDatasetRecordsRequest
        :rtype: LLMObsDatasetRecordsMutationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._create_llm_obs_dataset_records_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_experiment(
        self,
        body: LLMObsExperimentRequest,
    ) -> LLMObsExperimentResponse:
        """Create an LLM Observability experiment.

        Create a new LLM Observability experiment.

        :param body: Create experiment payload.
        :type body: LLMObsExperimentRequest
        :rtype: LLMObsExperimentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_llm_obs_experiment_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_experiment_events(
        self,
        experiment_id: str,
        body: LLMObsExperimentEventsRequest,
    ) -> None:
        """Push events for an LLM Observability experiment.

        Push spans and metrics for an LLM Observability experiment.

        :param experiment_id: The ID of the LLM Observability experiment.
        :type experiment_id: str
        :param body: Experiment events payload.
        :type body: LLMObsExperimentEventsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._create_llm_obs_experiment_events_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_integration_inference(
        self,
        integration: LLMObsIntegrationName,
        account_id: str,
        body: LLMObsIntegrationInferenceRequest,
    ) -> LLMObsIntegrationInferenceResponse:
        """Run an LLM inference.

        Run an LLM inference request through the specified integration and account, returning the model response and token usage.

        :param integration: The name of the LLM integration.
        :type integration: LLMObsIntegrationName
        :param account_id: The ID of the integration account.
        :type account_id: str
        :param body: Inference request parameters.
        :type body: LLMObsIntegrationInferenceRequest
        :rtype: LLMObsIntegrationInferenceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration"] = integration

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._create_llm_obs_integration_inference_endpoint.call_with_http_info(**kwargs)

    def create_llm_obs_project(
        self,
        body: LLMObsProjectRequest,
    ) -> LLMObsProjectResponse:
        """Create an LLM Observability project.

        Create a new LLM Observability project. Returns the existing project if a name conflict occurs.

        :param body: Create project payload.
        :type body: LLMObsProjectRequest
        :rtype: LLMObsProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_llm_obs_project_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_annotation_queue(
        self,
        queue_id: str,
    ) -> None:
        """Delete an LLM Observability annotation queue.

        Delete an annotation queue by its ID.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        return self._delete_llm_obs_annotation_queue_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_annotation_queue_interactions(
        self,
        queue_id: str,
        body: LLMObsDeleteAnnotationQueueInteractionsRequest,
    ) -> None:
        """Delete annotation queue interactions.

        Delete one or more interactions from an annotation queue.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :param body: Delete interactions payload.
        :type body: LLMObsDeleteAnnotationQueueInteractionsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        kwargs["body"] = body

        return self._delete_llm_obs_annotation_queue_interactions_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_custom_eval_config(
        self,
        eval_name: str,
    ) -> None:
        """Delete a custom evaluator configuration.

        Delete a custom LLM Observability evaluator configuration by its name.

        :param eval_name: The name of the custom LLM Observability evaluator configuration.
        :type eval_name: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["eval_name"] = eval_name

        return self._delete_llm_obs_custom_eval_config_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_data(
        self,
        body: LLMObsDataDeletionRequest,
    ) -> LLMObsDataDeletionResponse:
        """Delete LLM Observability data.

        Submit a request to delete LLM Observability span data matching a trace ID filter within a specified time range.

        :param body: Data deletion request payload.
        :type body: LLMObsDataDeletionRequest
        :rtype: LLMObsDataDeletionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_llm_obs_data_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_dataset_records(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDeleteDatasetRecordsRequest,
    ) -> None:
        """Delete LLM Observability dataset records.

        Delete one or more records from an LLM Observability dataset.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Delete records payload.
        :type body: LLMObsDeleteDatasetRecordsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._delete_llm_obs_dataset_records_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_datasets(
        self,
        project_id: str,
        body: LLMObsDeleteDatasetsRequest,
    ) -> None:
        """Delete LLM Observability datasets.

        Delete one or more LLM Observability datasets within the specified project.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param body: Delete datasets payload.
        :type body: LLMObsDeleteDatasetsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._delete_llm_obs_datasets_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_experiments(
        self,
        body: LLMObsDeleteExperimentsRequest,
    ) -> None:
        """Delete LLM Observability experiments.

        Delete one or more LLM Observability experiments.

        :param body: Delete experiments payload.
        :type body: LLMObsDeleteExperimentsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_llm_obs_experiments_endpoint.call_with_http_info(**kwargs)

    def delete_llm_obs_projects(
        self,
        body: LLMObsDeleteProjectsRequest,
    ) -> None:
        """Delete LLM Observability projects.

        Delete one or more LLM Observability projects.

        :param body: Delete projects payload.
        :type body: LLMObsDeleteProjectsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_llm_obs_projects_endpoint.call_with_http_info(**kwargs)

    def export_llm_obs_dataset(
        self,
        project_id: str,
        dataset_id: str,
        *,
        format: Union[LLMObsDatasetExportFormat, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
    ) -> str:
        """Export an LLM Observability dataset.

        Download the contents of a dataset as a CSV file. The download is streamed and includes one row per dataset record.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param format: Export format for the dataset contents. Only ``csv`` is currently supported.
        :type format: LLMObsDatasetExportFormat, optional
        :param version: Version of the dataset to export. If omitted, the current version is used. Must be between 0 and the current version of the dataset, inclusive.
        :type version: int, optional
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        if format is not unset:
            kwargs["format"] = format

        if version is not unset:
            kwargs["version"] = version

        return self._export_llm_obs_dataset_endpoint.call_with_http_info(**kwargs)

    def get_llm_obs_annotated_interactions(
        self,
        queue_id: str,
    ) -> LLMObsAnnotatedInteractionsResponse:
        """Get annotated queue interactions.

        Retrieve all interactions (traces and sessions) and their annotations for a given annotation queue.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :rtype: LLMObsAnnotatedInteractionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        return self._get_llm_obs_annotated_interactions_endpoint.call_with_http_info(**kwargs)

    def get_llm_obs_annotated_interactions_by_trace_i_ds(
        self,
        content_ids: List[str],
        *,
        offset: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> LLMObsAnnotatedInteractionsByTraceResponse:
        """Get annotated interactions by content IDs.

        Returns annotated interactions across all annotation queues for the given content IDs. Results include queue metadata (ID and name) for each interaction.

        :param content_ids: One or more content IDs to retrieve annotated interactions for. At least one is required.
        :type content_ids: [str]
        :param offset: Pagination offset. Must be >= 0. Defaults to 0.
        :type offset: int, optional
        :param limit: Maximum number of results to return. Must be > 0. Defaults to 100.
        :type limit: int, optional
        :rtype: LLMObsAnnotatedInteractionsByTraceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["content_ids"] = content_ids

        if offset is not unset:
            kwargs["offset"] = offset

        if limit is not unset:
            kwargs["limit"] = limit

        return self._get_llm_obs_annotated_interactions_by_trace_i_ds_endpoint.call_with_http_info(**kwargs)

    def get_llm_obs_annotation_queue_label_schema(
        self,
        queue_id: str,
    ) -> LLMObsAnnotationQueueLabelSchemaResponse:
        """Get annotation queue label schema.

        Retrieve the label schema for a given annotation queue.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :rtype: LLMObsAnnotationQueueLabelSchemaResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        return self._get_llm_obs_annotation_queue_label_schema_endpoint.call_with_http_info(**kwargs)

    def get_llm_obs_custom_eval_config(
        self,
        eval_name: str,
    ) -> LLMObsCustomEvalConfigResponse:
        """Get a custom evaluator configuration.

        Retrieve a custom LLM Observability evaluator configuration by its name.

        :param eval_name: The name of the custom LLM Observability evaluator configuration.
        :type eval_name: str
        :rtype: LLMObsCustomEvalConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["eval_name"] = eval_name

        return self._get_llm_obs_custom_eval_config_endpoint.call_with_http_info(**kwargs)

    def get_llm_obs_dataset_draft_state(
        self,
        project_id: str,
        dataset_id: str,
    ) -> LLMObsDatasetDraftStateResponse:
        """Get LLM Observability dataset draft state.

        Retrieve the draft state of a dataset, including whether it is currently locked for editing and which user holds the lock.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :rtype: LLMObsDatasetDraftStateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        return self._get_llm_obs_dataset_draft_state_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_annotation_queues(
        self,
        *,
        project_id: Union[str, UnsetType] = unset,
        queue_ids: Union[List[str], UnsetType] = unset,
    ) -> LLMObsAnnotationQueuesResponse:
        """List LLM Observability annotation queues.

        List annotation queues. Optionally filter by project ID or queue IDs. These parameters are mutually exclusive.
        If neither is provided, all queues in the organization are returned.

        :param project_id: Filter annotation queues by project ID. Cannot be used together with ``queueIds``.
        :type project_id: str, optional
        :param queue_ids: Filter annotation queues by queue IDs (comma-separated). Cannot be used together with ``projectId``.
        :type queue_ids: [str], optional
        :rtype: LLMObsAnnotationQueuesResponse
        """
        kwargs: Dict[str, Any] = {}
        if project_id is not unset:
            kwargs["project_id"] = project_id

        if queue_ids is not unset:
            kwargs["queue_ids"] = queue_ids

        return self._list_llm_obs_annotation_queues_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_dataset_records(
        self,
        project_id: str,
        dataset_id: str,
        *,
        filter_version: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> LLMObsDatasetRecordsListResponse:
        """List LLM Observability dataset records.

        List all records in an LLM Observability dataset, sorted by creation date, newest first.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param filter_version: Retrieve records from a specific dataset version. Defaults to the current version.
        :type filter_version: int, optional
        :param page_cursor: Use the Pagination cursor to retrieve the next page of results.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of results to return per page.
        :type page_limit: int, optional
        :rtype: LLMObsDatasetRecordsListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_llm_obs_dataset_records_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_datasets(
        self,
        project_id: str,
        *,
        filter_name: Union[str, UnsetType] = unset,
        filter_id: Union[str, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> LLMObsDatasetsResponse:
        """List LLM Observability datasets.

        List all LLM Observability datasets for a project, sorted by creation date, newest first.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param filter_name: Filter datasets by name.
        :type filter_name: str, optional
        :param filter_id: Filter datasets by dataset ID.
        :type filter_id: str, optional
        :param page_cursor: Use the Pagination cursor to retrieve the next page of results.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of results to return per page.
        :type page_limit: int, optional
        :rtype: LLMObsDatasetsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_llm_obs_datasets_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_dataset_versions(
        self,
        project_id: str,
        dataset_id: str,
    ) -> LLMObsDatasetVersionsResponse:
        """List LLM Observability dataset versions.

        List the active versions of a dataset. A version is created each time a dataset is referenced by an experiment run.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :rtype: LLMObsDatasetVersionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        return self._list_llm_obs_dataset_versions_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_experiment_events(
        self,
        experiment_id: str,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> LLMObsExperimentEventsV2Response:
        """List events for an LLM Observability experiment.

        Retrieve spans and experiment-level summary metrics for a given experiment with cursor-based pagination.

        :param experiment_id: The ID of the LLM Observability experiment.
        :type experiment_id: str
        :param page_limit: Maximum number of spans to return per page. Defaults to 5000.
        :type page_limit: int, optional
        :param page_cursor: Opaque cursor from a previous response to fetch the next page of results.
        :type page_cursor: str, optional
        :rtype: LLMObsExperimentEventsV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_llm_obs_experiment_events_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_experiments(
        self,
        *,
        filter_project_id: Union[str, UnsetType] = unset,
        filter_dataset_id: Union[str, UnsetType] = unset,
        filter_id: Union[str, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> LLMObsExperimentsResponse:
        """List LLM Observability experiments.

        List all LLM Observability experiments sorted by creation date, newest first.

        :param filter_project_id: Filter experiments by project ID. Required if ``filter[dataset_id]`` is not provided.
        :type filter_project_id: str, optional
        :param filter_dataset_id: Filter experiments by dataset ID.
        :type filter_dataset_id: str, optional
        :param filter_id: Filter experiments by experiment ID. Can be specified multiple times.
        :type filter_id: str, optional
        :param page_cursor: Use the Pagination cursor to retrieve the next page of results.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of results to return per page.
        :type page_limit: int, optional
        :rtype: LLMObsExperimentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_project_id is not unset:
            kwargs["filter_project_id"] = filter_project_id

        if filter_dataset_id is not unset:
            kwargs["filter_dataset_id"] = filter_dataset_id

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_llm_obs_experiments_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_integration_accounts(
        self,
        integration: LLMObsIntegrationName,
    ) -> List[LLMObsIntegrationAccount]:
        """List LLM integration accounts.

        Retrieve the list of configured accounts for the specified LLM provider integration.

        :param integration: The name of the LLM integration.
        :type integration: LLMObsIntegrationName
        :rtype: [LLMObsIntegrationAccount]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration"] = integration

        return self._list_llm_obs_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_integration_models(
        self,
        integration: LLMObsIntegrationName,
        account_id: str,
    ) -> List[LLMObsIntegrationModel]:
        """List LLM integration models.

        Retrieve the list of models available for the specified LLM provider integration and account.

        :param integration: The name of the LLM integration.
        :type integration: LLMObsIntegrationName
        :param account_id: The ID of the integration account.
        :type account_id: str
        :rtype: [LLMObsIntegrationModel]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration"] = integration

        kwargs["account_id"] = account_id

        return self._list_llm_obs_integration_models_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_projects(
        self,
        *,
        filter_id: Union[str, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> LLMObsProjectsResponse:
        """List LLM Observability projects.

        List all LLM Observability projects sorted by creation date, newest first.

        :param filter_id: Filter projects by project ID.
        :type filter_id: str, optional
        :param filter_name: Filter projects by name.
        :type filter_name: str, optional
        :param page_cursor: Use the Pagination cursor to retrieve the next page of results.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of results to return per page.
        :type page_limit: int, optional
        :rtype: LLMObsProjectsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_llm_obs_projects_endpoint.call_with_http_info(**kwargs)

    def list_llm_obs_spans(
        self,
        *,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        filter_span_id: Union[str, UnsetType] = unset,
        filter_trace_id: Union[str, UnsetType] = unset,
        filter_span_kind: Union[str, UnsetType] = unset,
        filter_span_name: Union[str, UnsetType] = unset,
        filter_ml_app: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        include_attachments: Union[bool, UnsetType] = unset,
    ) -> LLMObsSpansResponse:
        """List LLM Observability spans.

        List LLM Observability spans matching the specified filters.

        :param filter_from: Start of the time range. Accepts ISO 8601 or relative format (e.g., ``now-15m`` ). Defaults to ``now-15m``.
        :type filter_from: str, optional
        :param filter_to: End of the time range. Accepts ISO 8601 or relative format. Defaults to ``now``.
        :type filter_to: str, optional
        :param filter_query: Search query using LLM Observability query syntax. Supports attribute filters using the field:value syntax (e.g. session_id, trace_id, ml_app, meta.span.kind). When provided, structured field filters ( ``filter[span_id]`` , ``filter[trace_id]`` , etc.) are ignored.
        :type filter_query: str, optional
        :param filter_span_id: Filter by exact span ID.
        :type filter_span_id: str, optional
        :param filter_trace_id: Filter by exact trace ID.
        :type filter_trace_id: str, optional
        :param filter_span_kind: Filter by span kind (e.g., llm, agent, tool, task, workflow).
        :type filter_span_kind: str, optional
        :param filter_span_name: Filter by span name.
        :type filter_span_name: str, optional
        :param filter_ml_app: Filter by ML application name.
        :type filter_ml_app: str, optional
        :param page_limit: Maximum number of spans to return. Defaults to ``10``.
        :type page_limit: int, optional
        :param page_cursor: Cursor from the previous response to retrieve the next page.
        :type page_cursor: str, optional
        :param sort: Sort order for the results.
        :type sort: str, optional
        :param include_attachments: Whether to include attachment data in the response. Defaults to ``true``.
        :type include_attachments: bool, optional
        :rtype: LLMObsSpansResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_span_id is not unset:
            kwargs["filter_span_id"] = filter_span_id

        if filter_trace_id is not unset:
            kwargs["filter_trace_id"] = filter_trace_id

        if filter_span_kind is not unset:
            kwargs["filter_span_kind"] = filter_span_kind

        if filter_span_name is not unset:
            kwargs["filter_span_name"] = filter_span_name

        if filter_ml_app is not unset:
            kwargs["filter_ml_app"] = filter_ml_app

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if sort is not unset:
            kwargs["sort"] = sort

        if include_attachments is not unset:
            kwargs["include_attachments"] = include_attachments

        return self._list_llm_obs_spans_endpoint.call_with_http_info(**kwargs)

    def lock_llm_obs_dataset_draft_state(
        self,
        project_id: str,
        dataset_id: str,
    ) -> LLMObsDatasetDraftStateResponse:
        """Lock LLM Observability dataset draft state.

        Acquire the draft lock on a dataset for the calling user. The lock prevents other users from concurrently editing the dataset draft.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :rtype: LLMObsDatasetDraftStateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        return self._lock_llm_obs_dataset_draft_state_endpoint.call_with_http_info(**kwargs)

    def restore_llm_obs_dataset_version(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetRestoreVersionRequest,
    ) -> None:
        """Restore an LLM Observability dataset version.

        Restore a dataset to a previous version. The dataset's current version is bumped, and its records are replaced with the records from the specified prior version.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Restore dataset version payload.
        :type body: LLMObsDatasetRestoreVersionRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._restore_llm_obs_dataset_version_endpoint.call_with_http_info(**kwargs)

    def search_llm_obs_experimentation(
        self,
        body: LLMObsExperimentationSearchRequest,
    ) -> LLMObsExperimentationSearchResponse:
        """Search LLM Observability experimentation entities.

        Search across LLM Observability experimentation entities — projects, datasets, dataset records, experiments, and experiment runs — using cursor-based pagination.

        The ``filter.scope`` field controls which entity types are returned. At least one valid scope must be provided.

        Returns ``200 OK`` when all results fit in a single page. Returns ``206 Partial Content`` with a cursor in ``meta.after`` when additional pages are available.

        :param body: Experimentation search payload.
        :type body: LLMObsExperimentationSearchRequest
        :rtype: LLMObsExperimentationSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._search_llm_obs_experimentation_endpoint.call_with_http_info(**kwargs)

    def search_llm_obs_spans(
        self,
        body: LLMObsSearchSpansRequest,
    ) -> LLMObsSpansResponse:
        """Search LLM Observability spans.

        Search LLM Observability spans using structured filters in the request body.

        :param body: Search spans payload.
        :type body: LLMObsSearchSpansRequest
        :rtype: LLMObsSpansResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._search_llm_obs_spans_endpoint.call_with_http_info(**kwargs)

    def simple_search_llm_obs_experimentation(
        self,
        body: LLMObsExperimentationSimpleSearchRequest,
    ) -> LLMObsExperimentationSimpleSearchResponse:
        """Simple search experimentation entities.

        Search across LLM Observability experimentation entities using offset-based (page-number) pagination.
        Use this endpoint when you need total page count or want to navigate to a specific page number.

        The ``filter.scope`` field controls which entity types are returned. At least one valid scope must be provided.

        :param body: Simple search payload.
        :type body: LLMObsExperimentationSimpleSearchRequest
        :rtype: LLMObsExperimentationSimpleSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._simple_search_llm_obs_experimentation_endpoint.call_with_http_info(**kwargs)

    def unlock_llm_obs_dataset_draft_state(
        self,
        project_id: str,
        dataset_id: str,
    ) -> None:
        """Unlock LLM Observability dataset draft state.

        Release the draft lock on a dataset held by the calling user, allowing other users to edit the dataset draft.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        return self._unlock_llm_obs_dataset_draft_state_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_annotation_queue(
        self,
        queue_id: str,
        body: LLMObsAnnotationQueueUpdateRequest,
    ) -> LLMObsAnnotationQueueResponse:
        """Update an LLM Observability annotation queue.

        Partially update an annotation queue. The ``name`` , ``description`` , and ``annotation_schema`` fields can be updated.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :param body: Update annotation queue payload.
        :type body: LLMObsAnnotationQueueUpdateRequest
        :rtype: LLMObsAnnotationQueueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        kwargs["body"] = body

        return self._update_llm_obs_annotation_queue_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_annotation_queue_label_schema(
        self,
        queue_id: str,
        body: LLMObsAnnotationQueueLabelSchemaUpdateRequest,
    ) -> LLMObsAnnotationQueueLabelSchemaResponse:
        """Update annotation queue label schema.

        Create or replace the label schema for a given annotation queue.
        The label schema defines the labels annotators can apply to interactions in the queue.
        Label names must be unique within the queue and match the pattern ``^[a-zA-Z0-9_-]+$``.
        Each label must have a valid type: score, categorical, boolean, or text.

        :param queue_id: The ID of the LLM Observability annotation queue.
        :type queue_id: str
        :param body: Update label schema payload.
        :type body: LLMObsAnnotationQueueLabelSchemaUpdateRequest
        :rtype: LLMObsAnnotationQueueLabelSchemaResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["queue_id"] = queue_id

        kwargs["body"] = body

        return self._update_llm_obs_annotation_queue_label_schema_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_custom_eval_config(
        self,
        eval_name: str,
        body: LLMObsCustomEvalConfigUpdateRequest,
    ) -> None:
        """Create or update a custom evaluator configuration.

        Create or update a custom LLM Observability evaluator configuration by its name.

        :param eval_name: The name of the custom LLM Observability evaluator configuration.
        :type eval_name: str
        :param body: Custom evaluator configuration payload.
        :type body: LLMObsCustomEvalConfigUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["eval_name"] = eval_name

        kwargs["body"] = body

        return self._update_llm_obs_custom_eval_config_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_dataset(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetUpdateRequest,
    ) -> LLMObsDatasetResponse:
        """Update an LLM Observability dataset.

        Partially update an existing LLM Observability dataset within the specified project.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Update dataset payload.
        :type body: LLMObsDatasetUpdateRequest
        :rtype: LLMObsDatasetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._update_llm_obs_dataset_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_dataset_records(
        self,
        project_id: str,
        dataset_id: str,
        body: LLMObsDatasetRecordsUpdateRequest,
    ) -> LLMObsDatasetRecordsMutationResponse:
        """Update LLM Observability dataset records.

        Update one or more existing records in an LLM Observability dataset.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param body: Update records payload.
        :type body: LLMObsDatasetRecordsUpdateRequest
        :rtype: LLMObsDatasetRecordsMutationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._update_llm_obs_dataset_records_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_experiment(
        self,
        experiment_id: str,
        body: LLMObsExperimentUpdateRequest,
    ) -> LLMObsExperimentResponse:
        """Update an LLM Observability experiment.

        Partially update an existing LLM Observability experiment.

        :param experiment_id: The ID of the LLM Observability experiment.
        :type experiment_id: str
        :param body: Update experiment payload.
        :type body: LLMObsExperimentUpdateRequest
        :rtype: LLMObsExperimentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._update_llm_obs_experiment_endpoint.call_with_http_info(**kwargs)

    def update_llm_obs_project(
        self,
        project_id: str,
        body: LLMObsProjectUpdateRequest,
    ) -> LLMObsProjectResponse:
        """Update an LLM Observability project.

        Partially update an existing LLM Observability project.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param body: Update project payload.
        :type body: LLMObsProjectUpdateRequest
        :rtype: LLMObsProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._update_llm_obs_project_endpoint.call_with_http_info(**kwargs)

    def upload_llm_obs_dataset_records_file(
        self,
        project_id: str,
        dataset_id: str,
        *,
        deduplicate: Union[bool, UnsetType] = unset,
        overwrite: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        include_user_data: Union[bool, UnsetType] = unset,
        file: Union[file_type, UnsetType] = unset,
    ) -> None:
        """Upload records to an LLM Observability dataset.

        Upload records to a dataset from a file. The request is a ``multipart/form-data`` upload containing a single ``file`` part.
        Currently only CSV is supported. The CSV must include an ``input`` column. Optional columns are ``id`` , ``expected_output`` , ``metadata`` , and ``tags``.

        The response is a Server-Sent Events stream ( ``text/event-stream`` ) emitting progress updates while records are processed. The stream emits the following named events:

        * ``progress`` : incremental record counts written so far.
        * ``completed`` : terminal event with a JSON body containing ``records_created``.
        * ``error`` : terminal event with a JSON body containing an error ``message``.

        :param project_id: The ID of the LLM Observability project.
        :type project_id: str
        :param dataset_id: The ID of the LLM Observability dataset.
        :type dataset_id: str
        :param deduplicate: Whether to skip records whose ``input`` already exists in the dataset. Defaults to ``false``.
        :type deduplicate: bool, optional
        :param overwrite: Whether to overwrite existing records that share the same user-provided ``id``. Defaults to ``true``.
        :type overwrite: bool, optional
        :param tags: Tags to apply to every uploaded record, in addition to any tags defined on individual rows. Can be repeated, e.g. ``tags=env:prod&tags=team:ai``.
        :type tags: [str], optional
        :param include_user_data: Whether to enrich the response with user metadata.
        :type include_user_data: bool, optional
        :param file: The records file to upload. Currently only CSV is supported. The file must include an ``input`` column. Optional columns include ``id`` , ``expected_output`` , ``metadata`` , and ``tags``.
        :type file: file_type, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["dataset_id"] = dataset_id

        if deduplicate is not unset:
            kwargs["deduplicate"] = deduplicate

        if overwrite is not unset:
            kwargs["overwrite"] = overwrite

        if tags is not unset:
            kwargs["tags"] = tags

        if include_user_data is not unset:
            kwargs["include_user_data"] = include_user_data

        if file is not unset:
            kwargs["file"] = file

        return self._upload_llm_obs_dataset_records_file_endpoint.call_with_http_info(**kwargs)
