# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.llm_obs_experiments_response import LLMObsExperimentsResponse
from datadog_api_client.v2.model.llm_obs_experiment_response import LLMObsExperimentResponse
from datadog_api_client.v2.model.llm_obs_experiment_request import LLMObsExperimentRequest
from datadog_api_client.v2.model.llm_obs_delete_experiments_request import LLMObsDeleteExperimentsRequest
from datadog_api_client.v2.model.llm_obs_experiment_update_request import LLMObsExperimentUpdateRequest
from datadog_api_client.v2.model.llm_obs_experiment_events_request import LLMObsExperimentEventsRequest
from datadog_api_client.v2.model.llm_obs_projects_response import LLMObsProjectsResponse
from datadog_api_client.v2.model.llm_obs_project_response import LLMObsProjectResponse
from datadog_api_client.v2.model.llm_obs_project_request import LLMObsProjectRequest
from datadog_api_client.v2.model.llm_obs_delete_projects_request import LLMObsDeleteProjectsRequest
from datadog_api_client.v2.model.llm_obs_project_update_request import LLMObsProjectUpdateRequest
from datadog_api_client.v2.model.llm_obs_datasets_response import LLMObsDatasetsResponse
from datadog_api_client.v2.model.llm_obs_dataset_response import LLMObsDatasetResponse
from datadog_api_client.v2.model.llm_obs_dataset_request import LLMObsDatasetRequest
from datadog_api_client.v2.model.llm_obs_delete_datasets_request import LLMObsDeleteDatasetsRequest
from datadog_api_client.v2.model.llm_obs_dataset_update_request import LLMObsDatasetUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_records_list_response import LLMObsDatasetRecordsListResponse
from datadog_api_client.v2.model.llm_obs_dataset_records_mutation_response import LLMObsDatasetRecordsMutationResponse
from datadog_api_client.v2.model.llm_obs_dataset_records_update_request import LLMObsDatasetRecordsUpdateRequest
from datadog_api_client.v2.model.llm_obs_dataset_records_request import LLMObsDatasetRecordsRequest
from datadog_api_client.v2.model.llm_obs_delete_dataset_records_request import LLMObsDeleteDatasetRecordsRequest


class LLMObservabilityApi:
    """
    Manage LLM Observability projects, datasets, dataset records, and experiments via the Experiments API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

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
        :param page_cursor: Pagination cursor for the next page of results.
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
        :param page_cursor: Pagination cursor for the next page of results.
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
        :param page_cursor: Pagination cursor for the next page of results.
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
        :param page_cursor: Pagination cursor for the next page of results.
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
